"""
Simula personas usando AuditHub a la vez (inician sesion y recorren pantallas).

Uso (con el servidor y la base de pruebas encendidos):
   locust -f herramientas_carga/locustfile.py --host http://127.0.0.1:8000 --csv resultado --headless -u 50 -r 5 -t 2m
     -u = personas a la vez · -r = cuantas entran por segundo · -t = duracion
Lee usuarios_carga.csv (lo crea `manage.py sembrar_carga`) y usa el nombre de cada empresa como "Host".
"""
import csv
import random
import re

from locust import HttpUser, between, task

with open('usuarios_carga.csv', encoding='utf8') as f:
    USUARIOS = list(csv.DictReader(f))

PANTALLAS_GESTION = [
    ('/dashboard/', 5), ('/auditorias/', 4), ('/hallazgos/', 4), ('/biblioteca-riesgos/', 2),
    ('/auditorias/plan-anual/', 2), ('/planes-accion/', 3), ('/reportes/', 1), ('/auditorias/mapa-riesgos/', 1),
    ('/auditorias/cronograma/', 1), ('/notificaciones/', 2),
]
PANTALLAS_AUDITADO = [('/dashboard/', 5), ('/planes-accion/mi-panel/', 5), ('/notificaciones/', 2)]


class Persona(HttpUser):
    wait_time = between(1, 4)       # una persona real lee unos segundos entre pantalla y pantalla

    def on_start(self):
        self.u = random.choice(USUARIOS)
        self.client.headers['Host'] = self.u['host']
        r = self.client.get('/accounts/login/', name='login (formulario)')
        token = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', r.text)
        r = self.client.post('/accounts/login/', name='login (entrar)', data={
            'username': self.u['usuario'], 'password': self.u['clave'],
            'csrfmiddlewaretoken': token.group(1) if token else ''}, headers={'Referer': f'http://{self.u["host"]}/accounts/login/'})
        pant = PANTALLAS_AUDITADO if self.u['rol'] == 'AUDITADO' else PANTALLAS_GESTION
        self.rutas = [p for p, _ in pant]
        self.pesos = [w for _, w in pant]

    @task
    def recorrer(self):
        ruta = random.choices(self.rutas, weights=self.pesos)[0]
        with self.client.get(ruta, name=ruta, catch_response=True) as r:
            if r.status_code != 200 or '/accounts/login' in r.url:
                r.failure(f'{r.status_code} -> {r.url}')
