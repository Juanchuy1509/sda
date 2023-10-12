from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Ticket_Formato
from django.conf import settings

@receiver(pre_save, sender=Ticket_Formato)
def enviar_correo_cuando_ea(sender, instance, **kwargs):
    usuario_correo = instance.usuario_solicitante.correo
    if instance.estatus == 'EA':
        subject = 'Nuevo ticket en espera de asignación'
        message = f'Se ha creado un nuevo ticket en espera de asignación:\n\n' \
                  f'Falla indicada: {instance.explicacion_breve}\n' \
                  f'Descripción: {instance.explicacion_larga}\n' \
                  f'Fecha de solicitud: {instance.fecha_solicitud}\n'
        from_email = settings.EMAIL_HOST_USER  # Cambia esto al correo del remitente
        recipient_list = [usuario_correo,'j.molina@epicland.com.mx', 'marreola@epicland.com.mx']  # Cambia esto a la dirección de correo del destinatario
        send_mail(subject, message, from_email, recipient_list)
    elif instance.estatus == 'EP':
        subject = f'El siguiente ticket se asigno a usted {instance.explicacion_breve}'
        message = 'Por favor consulta el sistema de tickets para atender la asignación, gracias por el seguimiento!'
        from_email = settings.EMAIL_HOST_USER  # Cambia esto al correo del remitente
        recipient_list = [instance.asignacion.correo]  # Cambia esto a la dirección de correo del destinatario
        send_mail(subject, message, from_email, recipient_list)
    elif instance.estatus == 'OK':
        subject = f'Ticket finalizado con exito {instance.explicacion_breve}'
        message = f'Le confirmamos que la siguiente solicitud fue realizada con exito:\n\n' \
                  f'Falla indicada: {instance.explicacion_breve}\n' \
                  f'Descripción: {instance.explicacion_larga}\n' \
                  f'Fecha de solicitud: {instance.fecha_solicitud}\n'
        from_email = settings.EMAIL_HOST_USER  # Cambia esto al correo del remitente
        recipient_list = [usuario_correo]  # Cambia esto a la dirección de correo del destinatario
        send_mail(subject, message, from_email, recipient_list)
