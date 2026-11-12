# Prueba de carga

Herramientas: **Locust** (personas simuladas) y **Waitress** (servidor), sobre una base **separada** de la real.

Cada persona simulada inicia sesión y recorre las pantallas con la frecuencia de un uso real
(dashboard, auditorías, hallazgos, planes, reportes, mapa de riesgos…); el auditado usa su propio panel.

## Resultado (equipo de escritorio, un solo servidor)

| | |
|---|---|
| Empresas / usuarios sembrados | 5 / 205 |
| Personas simultáneas | 50 |
| Peticiones | 2 208 |
| **Errores** | **0** |
| Mediana | **170 ms** |
| Percentil 95 | **410 ms** |
| Percentil 99 | 830 ms |
| Iniciar sesión (mediana) | 820 ms — es lo más lento porque se cifra la contraseña |

Esta prueba aún no es el límite del sistema; se continúa por escalones de 100, 200 y 400 personas simultáneas.
La muestra de [`prueba_de_carga_locust.py`](../muestras_de_codigo/prueba_de_carga_locust.py) es el guion que se usó.

> Cifras de un computador de escritorio con datos sintéticos; no son una garantía de producción.
