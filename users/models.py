from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=False,
                                verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, verbose_name='Email')
    
    photo = models.ImageField(upload_to='users/photos/', blank=True, null=True,
                              verbose_name='Фото')
    
    USERNAME_FIELD = 'email'  # Логинимся по email
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
