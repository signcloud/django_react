from django.db import models
from accounts.models import User


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # class Meta:
    #     fields = ('title', 'completed',)

    def __str__(self):
        return self.title
