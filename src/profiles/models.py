from django.db import models
from django.conf import settings


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    homepage = models.URLField("Personal homepage", blank=True, null=True)

    class Meta:
        abstract = True


class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
