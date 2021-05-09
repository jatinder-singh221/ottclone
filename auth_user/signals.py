from django.dispatch import receiver
from .models import user_extend
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# signals
@receiver(post_save, sender=User)
def created(sender, instance, created, **kwargs):
    if created:
        user_extend.objects.create(user = instance)

