#Created to automatically update profile of new users
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): #This will help create a profile
    if created: #if account is created
        Profile.objects.create(user=instance) # then create its profile by taking all the info of user
@receiver(post_save, sender=User)        
def save_profile(sender, instance, **kwargs): #Save the profile
    instance.profile.save()         