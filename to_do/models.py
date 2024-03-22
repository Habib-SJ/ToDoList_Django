from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class to_do(models.Model):
    task = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def check_item(self):
        self.checked = True

    def __str__(self):
        return self.task
