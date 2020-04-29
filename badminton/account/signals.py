from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import profile
from django.dispatch import receiver

@receiver(post_save , sender=User)
def profile_s(sender , instance , created , **kwargs):
    if created:
        profile.objects.create(user=instance)
        print("profile created")

#post_save.connect(profile_s , sender=User)