from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import logging
from . import models

logger = logging.getLogger("project")


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, **kwargs):
    if not created:
        return
    # Create the profile object, only if it is newly created
    profile = models.Profile(user=instance)
    profile.save()
    logger.info('New user profile for {} created'.format(instance))
