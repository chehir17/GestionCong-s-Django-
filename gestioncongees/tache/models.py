from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Tache(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('encours', 'EnCours'),
        ('terminer', 'Terminer')
    )
    class Meta:
        verbose_name_plural = 'tache'

    user_id = models.ForeignKey(User, related_name="tache", on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    duree = models.IntegerField()
    etat = models.CharField(choices=STATUS_CHOICES,max_length=10, default="open")
    created_at = models.DateTimeField(auto_now_add=True)

