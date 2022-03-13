from email.mime import image

from django.contrib.auth.models import User

from django.db import models

class Post(models.Model):

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    caption=models.CharField(max_length=150)
    description=models.TextField(max_length=150)
    image=models.ImageField(upload_to="media",blank=True , null=True)

    def __str__(self):
        return self.caption


# Create your models here.
