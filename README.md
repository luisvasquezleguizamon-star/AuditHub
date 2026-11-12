<p align="center"><img src="marca/logo_audithub_horizontal.png" alt="AuditHub" width="320"></p>

# AuditHub — Plataforma multiempresa de auditorías internas

> **Este repositorio es una vitrina del proyecto**: describe qué construí, cómo está diseñado y cómo lo probé.
> El código completo del producto es **privado**. Aquí solo hay documentación, números y unas pocas muestras de código.

AuditHub gestiona el ciclo completo de una auditoría interna, alineado con los principios de **ISO 27001**:
desde el plan anual hasta el seguimiento de los planes de acción, con un asistente de IA y alertas automáticas.
Cada empresa cliente vive aislada de las demás (**multiempresa**).

## Qué hace

| Módulo | Qué resuelve |
|---|---|
| **Plan anual y cronograma** | Planificación de auditorías por año; es requisito para abrir una auditoría |
| **Auditorías, riesgos y controles** | Matriz de riesgos, controles ISO 27001, mapa de riesgos, encuestas y requerimientos |
| **Hallazgos** | Registro con flujo de aceptación/rechazo por parte del auditado |
| **Planes de acción** | Actividades, avances (25/50/75/100 %) con evidencia y aprobación del auditor |
| **Biblioteca de riesgos** | Catálogo reutilizable, con carga masiva desde Excel y plantilla descargable |
| **Reportes** | Informes en PDF y Excel |
| **Dashboard** | Vista ejecutiva y panel propio para el auditado |
| **Amenazas globales** | Mapa interactivo de amenazas |
| **Asistente de IA** | Chat de ayuda y alertas/resumen semanal por correo y Telegram (automatizado con n8n + Gemini) |
| **Plataforma** | Panel de super administrador: crea empresas, fija límites de usuarios y ve la actividad |

Roles: super administrador, administrador, auditor, líder y auditado, además de roles personalizados.

## En números

| | |
|---|---|
| Pruebas automatizadas | **más de 1 000**, sin fallos |
| Migraciones de base de datos | **87** |
| Aplicaciones (módulos) Django | **12** |
| Aislamiento de datos | un **esquema de PostgreSQL por empresa** (~59 tablas cada una) |
| Prueba de carga (equipo de escritorio) | 5 empresas, 205 usuarios, 50 simultáneos → **0 errores**, mediana **170 ms**, p95 **410 ms** |

## Tecnología

- **Backend:** Python 3.13, Django 5.0, django-tenants (multiempresa), APScheduler
- **Base de datos:** PostgreSQL 16
- **Frontend:** plantillas de Django, Tailwind CSS, Chart.js, Quill, jsVectorMap
- **Reportes:** ReportLab (PDF), openpyxl (Excel)
- **IA y automatización:** n8n + Gemini; alertas por correo y Telegram
- **Pruebas:** suite de Django (más de 1 000) y pruebas de carga con Locust

## Documentación

- [Arquitectura multiempresa](docs/ARQUITECTURA.md)
- [Flujo de una auditoría](docs/FLUJO_DE_AUDITORIA.md)
- [Calidad y pruebas](docs/CALIDAD_Y_PRUEBAS.md)
- [Prueba de carga](docs/PRUEBA_DE_CARGA.md)
- [Seguridad y privacidad](docs/SEGURIDAD_Y_PRIVACIDAD.md)
- [Muestras de código](muestras_de_codigo/)
- [Capturas de pantalla](capturas/) (datos de demostración)

## Estado y siguientes pasos

Funcional y probado. Pendiente: integración continua (GitHub Actions), contenedores (Docker) y revisión legal de la política de privacidad.

## Licencia y contacto

© Todos los derechos reservados. El contenido de este repositorio se publica solo para mostrar el trabajo realizado.
Contacto: *(agrega aquí tu correo o LinkedIn)*
