# Calidad y pruebas

Más de **1 000 pruebas automatizadas**, todas en verde, repartidas por módulo:

| Módulo | Pruebas |
|---|---|
| Auditorías (riesgos, controles, encuestas, requerimientos, mapa) | ~405 |
| Planes de acción | ~258 |
| Multiempresa | ~100 |
| Asistente de ayuda / chat | ~72 |
| Hallazgos | ~51 |
| Agente de IA y alertas | ~43 |
| Cuentas y roles | ~40 |
| Reportes | ~22 |
| Biblioteca de riesgos | ~19 |

Qué cubren:
- **Reglas de negocio** (p. ej. un plan de acción exige hallazgo aceptado).
- **Permisos por rol:** quién ve y quién puede hacer qué.
- **Aislamiento entre empresas**, sobre esquemas reales de PostgreSQL.
- **Un recorrido completo** de una empresa nueva, de punta a punta.
- **Migraciones de datos.**

Se ejecutan con `python manage.py test`. *Aún no corren automáticamente al subir cambios (integración continua pendiente).*
