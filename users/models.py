
import datetime
import random
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from rest_framework_simplejwt.tokens import RefreshToken
from products.models import BaseCreatedModel


class User(AbstractUser, BaseCreatedModel):
    phone = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    def create_verification_code(self):
        code = "".join([str(random.randint(1, 9)) for _ in range(4)])
        UserConfirmation.objects.create(
            code=code,
            user_id=self.id,
        )

        return code

    def token(self):
        access = RefreshToken.for_user(self)
        data = {
            'access_token': str(access.access_token),
            'refresh_token': str(access)
        }
        return data


class UserConfirmation(BaseCreatedModel):
    code = models.IntegerField()
    expire_time = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(minutes=10))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='code')
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.code}'



