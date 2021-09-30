from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(default="default_user_profile.png", upload_to="profile_pictures")
    profession      = models.CharField(max_length=100, null=True, blank=False)
    phone_number    = models.CharField(max_length=32, null=True, blank=False)
    website_url     = models.URLField(max_length=255, null=True, blank=True)
    
    address        = models.CharField(max_length=255, null=True, blank=False)
    latitude       = models.FloatField(null=True, blank=True)
    longitude      = models.FloatField(null=True, blank=True)

    class Meta: 
        verbose_name        = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return "{}'s profile".format(self.user.username)