from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# titulo, conteudo, datetime

class PostModel(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)