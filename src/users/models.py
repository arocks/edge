from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
import urllib.request
from django.core.files.base import ContentFile
import hashlib
from urllib.parse import urlencode
import uuid
from django.urls import reverse

# Defining a minimal custom user with no username. Instead their email
# address will be the unique identifier. There is no `is_staff` attribute
# just the `is_admin` attribute since most projects don't need the Group
# permission models. If you are admin then you have access to everything.
#
# Code is heavily based on Django docs on Custom Users.


class EdgeUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class EdgeUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # User's properties that are NOT for authentication purposes. Used
    # to be stored in a separate user profile but that's not
    # recommended anymore. Make sure these fields are nullable or blank.
    name = models.CharField(
        verbose_name="Full name of user", blank=True, max_length=255
    )
    picture = models.ImageField(
        "Profile picture", upload_to="profile_pics/", null=True, blank=True
    )
    # Slugs are needed to hide the primary key from the public URLs
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)

    objects = EdgeUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("users:show_user", args=[str(self.slug)])

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = "user"  # Hide the prefix Edge from Edge User


# Signals
@receiver(user_signed_up)
def retrieve_user_profile(request, user, **kwargs):
    print("Inside retrieve_user_profile")
    # Check if the login was using a social account
    sociallogin = kwargs.get("sociallogin", None)
    if sociallogin:
        # Django all-auth provides socialogin param which contains the
        # metadata of the user's social account. For e.g.
        #
        # sociallogin.account.provider           # for e.g. 'google'
        # sociallogin.account.get_avatar_url()   # profile picture
        # sociallogin.account.get_profile_url()  # URL to profile
        # sociallogin.account.get_avatar_url()   # profile picture
        #
        # See the socialaccount_socialaccount table for more info
        # inside the 'extra_data' field
        avatar_url = None
        if sociallogin.account.provider == "google":
            print("Inside google")
            user.name = sociallogin.account.extra_data["name"]
            avatar_url = sociallogin.account.get_avatar_url()
            avatar_filename = f"{sociallogin.account.uid}.jpg"
        if avatar_url is not None:
            content = save_image_from_url(avatar_url)
            user.picture.save(avatar_filename, content, save=True)
    else:
        # Non-social signups section, you only get their email
        #
        # So extract the user name from email (some have embarassing
        # emails like coolkid1976@yahoo.com but names can be changed
        # later)
        user.name = user.email.split("@")[0].capitalize()
        user.save()
        # Get the url from Gravatars
        gravatar_url = get_gravatar_image(user.email)
        print(f"Inside gravatar_url: {gravatar_url}")
        content = save_image_from_url(gravatar_url)
        avatar_filename = f"{user.id}.jpg"
        user.picture.save(avatar_filename, content, save=True)


def save_image_from_url(url):
    with urllib.request.urlopen(url) as u:
        raw_image = u.read()
        # TODO verify the raw image for security issues - verify_image
        return ContentFile(raw_image)


def get_gravatar_image(email, size=200, default="robohash"):
    gravatar_url = (
        "https://www.gravatar.com/avatar/"
        + hashlib.md5(email.encode("utf-8").lower()).hexdigest()
        + ".jpg?"
    )
    gravatar_url += urlencode({"d": default, "s": str(size)})
    return gravatar_url
