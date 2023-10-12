
from django.db import models
from django.utils import timezone
fecha_estimada_default = timezone.now


def fecha_estimada_default():
    return timezone.now()

class Bd1_Requerimiento(models.Model):
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return f'Requerimiento {self.id}: {self.descripcion}'
    class Meta:
        verbose_name = 'Requerimiento'
        verbose_name_plural = 'Requerimientos'
        db_table = 'Requerimientos'
        ordering = ['id']

class Bd2_Area(models.Model):
    area = models.CharField(max_length=100)
    def __str__(self):
        return f'Area {self.id}: {self.area}'
    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        db_table = 'Areas'
        ordering = ['id']

class Bd3_Ps(models.Model):
    nombre = models.CharField(max_length=252)
    correo = models.EmailField()
    def __str__(self):
        return f'Personal de sistemas {self.id}: {self.nombre} {self.correo}'
    class Meta:
        verbose_name = 'Personal sistema'
        verbose_name_plural = 'Personal de sistemas'
        db_table = 'Personal de sistemas'
        ordering=['id']
class Bd4_User(models.Model):
    nombre = models.CharField(max_length=252)
    correo = models.EmailField('Correo', blank=True, null=True)
    area = models.ForeignKey(Bd2_Area, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return f'Usuarios {self.id}: {self.nombre} {self.correo}'
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuarios'
        ordering = ['id']
class Ticket_Formato(models.Model):
    explicacion_breve = models.CharField(max_length=255)
    explicacion_larga = models.TextField()
    fecha_solicitud = models.DateField(default=fecha_estimada_default)  # ADMIN
    area = models.ForeignKey('BD2_Area',
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True)

    usuario_solicitante = models.ForeignKey(
        'Bd4_User',
        on_delete=models.SET_NULL,
        blank=True,
        null=True)

    requerimiento = models.ForeignKey('Bd1_Requerimiento',
                                      on_delete=models.SET_NULL,
                                      blank=True,
                                      null=True)
    asignacion = models.ForeignKey('Bd3_Ps', on_delete=models.SET_NULL, blank=True, null=True, default=None)

    estatus1 = 'EA'
    estatus2 = 'PT'
    estatus3 = 'EP'
    estatus4 = 'OK'
    SELECCIONA_ESTATUS=[(estatus1, 'En espera de asignación'),
                        (estatus2, 'Pendiente'),
                        (estatus3, 'En proceso'),
                        (estatus4,'Realizado'),
    ]
    estatus = models.CharField(max_length=25, choices=SELECCIONA_ESTATUS, default=estatus1)
    fecha_Vencimiento = models.DateField(default=fecha_estimada_default)
    prioridad1 = 'A'
    prioridad2 = 'B'
    prioridad3 = 'C'

    SELECCIONA_PRIORIDAD = [(prioridad1, 'Alta'),
                            (prioridad2, 'Media'),
                            (prioridad3, 'Baja'),]

    prioridad = models.CharField(max_length=10,choices=SELECCIONA_PRIORIDAD, default=prioridad2)  # ADMIN

    def __str__(self):
        return f' Ticket {self.id}: {self.explicacion_breve} {self.fecha_solicitud} {self.estatus}'
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        db_table = 'Tickets'
        ordering = ['id']

