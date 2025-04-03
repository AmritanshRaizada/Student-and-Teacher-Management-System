from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Student

@receiver(pre_save, sender=Student)
def lowercase_email(sender, instance, **kwargs):
    if instance.email:
        instance.email = instance.email.lower()
