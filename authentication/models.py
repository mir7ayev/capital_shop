from django.db import models
from django.contrib.auth.models import User
from config.base_models import BaseModel


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    avatar = models.ImageField('auth/user/')

    def __str__(self):
        return self.user.username
