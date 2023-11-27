from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model

@receiver(post_save, sender=SocialAccount)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        print('hello from signal')
        # Perform actions to update the user profile in the database
        # For example, update user fields based on the social account details
        # user.first_name = instance.extra_data.get('given_name', '')
        # user.last_name = instance.extra_data.get('family_name', '')
        user.is_verified = True
        user.save()