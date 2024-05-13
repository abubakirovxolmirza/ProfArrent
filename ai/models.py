from django.db import models
from users.models import User
# Create your models here.


class AI(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.TextField()
    gpt_result = models.TextField(blank=True, null=True)