from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    
    ROLES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLES, default='user')
    sold = models.IntegerField(default = 24)
    
    def __str__(self):
        return self.username