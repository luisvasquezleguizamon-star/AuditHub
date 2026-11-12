"""
Muestra: límite de usuarios por empresa (multiempresa).

"Ocupa cupo" = usuario con la cuenta habilitada y activa. Los desactivados y las solicitudes
pendientes NO cuentan; el cupo se revisa al crear un usuario activo, aprobar una solicitud o reactivar a alguien.
(Fragmento ilustrativo: el resto del sistema no se publica.)
"""
from django.core.exceptions import ValidationError


class LimiteUsuariosExcedido(ValidationError):
    def __init__(self, limite):
        self.limite = limite
        super().__init__(
            f'La empresa alcanzó su límite de {limite} usuarios activos. '
            'Desactiva a alguien o pide ampliar el límite.',
            code='limite_usuarios',
        )


def usuarios_que_ocupan_cupo(Usuario):
    """Usuarios del esquema actual que cuentan para el límite."""
    return Usuario.objects.filter(activo_sistema=True, is_active=True)


def limite_actual(empresa):
    """Límite de la empresa, o None si no tiene (0 = sin límite)."""
    if not empresa or not empresa.limite_usuarios:
        return None
    return empresa.limite_usuarios
