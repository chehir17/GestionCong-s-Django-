from django.db import models

from core.models import CustomUser
from django.contrib.auth.models import User

class Cangees(models.Model):
    demandeur = models.ForeignKey(User, related_name= 'Cangees', on_delete=models.CASCADE)
    sujet = models.CharField(max_length=255)
    dure = models.IntegerField(max_length=24)
    certif = models.FileField(upload_to='certif', blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

