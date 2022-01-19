from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
# Create your models here.
class PersonDetails(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        subject = 'generated token'
        message = str(f'{instance}\ngenerated token is: {token}')
        email_from = settings.EMAIL_HOST_USER
        send_To = ['amjad.ansari@datenwissen.com']
        send_mail(subject, message, email_from, send_To, fail_silently=True)