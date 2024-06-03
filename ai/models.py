from django.db import models
from users.models import User, CustomUser
# Create your models here.


class AI(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    result = models.TextField()
    first = models.TextField(blank=True, null=True)
    second = models.TextField(blank=True, null=True)
    third = models.TextField(blank=True, null=True) 

class Text(models.Model):
    system = models.TextField()
    text = models.TextField()
    text2 = models.TextField()
