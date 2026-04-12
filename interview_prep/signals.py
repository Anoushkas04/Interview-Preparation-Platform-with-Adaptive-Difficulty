from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # get_or_create is safer to prevent duplicates
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Use hasattr to check if the profile exists before saving
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
    else:
        # If it doesn't exist for some reason, create it now
        UserProfile.objects.get_or_create(user=instance)
