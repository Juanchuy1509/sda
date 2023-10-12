from django.contrib import admin
from .models import Bd3_Ps, Bd2_Area, Bd1_Requerimiento, Bd4_User,Ticket_Formato


class Psistema(admin.ModelAdmin):
    list_display = ('nombre', 'correo')
    search_fields = ('nombre',)

    # Definición de campos y relaciones
class DeptosAreaAdmi(admin.ModelAdmin):
    list_display = ('area',)
    search_fields = ('area',)

class RequeAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class Personal(admin.ModelAdmin):
    list_display = ('nombre','correo')
    search_fields = ('nombre',)

class Tickets(admin.ModelAdmin):
    list_display = ('explicacion_breve', 'area', 'asignacion', 'estatus', 'prioridad',)
    readonly_fields_default = ()
    def get_readonly_fields(self, request, obj=None):
        # Comprobar si el usuario es un superusuario (administrador)
        if request.user.is_superuser:
            # Si es un superusuario, permite que todos los campos sean de solo lectura
            return self.readonly_fields_default
        else:
            # Si no es un superusuario, excluye los campos "area" y "asignacion" de solo lectura
            return self.readonly_fields_default + ('asignacion','prioridad','estatus','fecha_Vencimiento','fecha_solicitud')

admin.site.register(Bd3_Ps, Psistema)
admin.site.register(Bd2_Area,DeptosAreaAdmi)
admin.site.register(Bd1_Requerimiento,RequeAdmin)
admin.site.register(Bd4_User,Personal)
admin.site.register(Ticket_Formato, Tickets)
