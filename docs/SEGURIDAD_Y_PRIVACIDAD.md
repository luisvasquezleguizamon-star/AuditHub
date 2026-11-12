# Seguridad y privacidad

- **Aislamiento por empresa** a nivel de base de datos (un esquema por cliente).
- **Roles y permisos** en cada pantalla; el menú de administración solo aparece a quien puede usarlo.
- **Contraseña temporal** en el primer ingreso y cambio obligatorio; aceptación de términos.
- **Validación de archivos** subidos y **sanitización de HTML** (bleach).
- **Credenciales fuera del código** (variables de entorno); las claves expuestas durante el desarrollo se rotaron.
- **IA:** el modelo se llama desde n8n. En pruebas solo se usan datos de demostración; para datos reales se recomienda un proveedor con retención cero (p. ej. Vertex AI) o enviar códigos en vez de nombres.
- **Pendiente:** revisión por un abogado de la política de privacidad.
