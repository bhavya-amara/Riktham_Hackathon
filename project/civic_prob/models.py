from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Posts(models.Model):
    profile=models.ForeignKey(MyProfile,on_delete=models.CASCADE)
    image=models.ImageField()
    likes=models.IntegerField()
    date=models.DateTimeField()
    time=models.TimeField()

class comments(models.Model):
    message=models.CharField()
    user=models.ForeignKey(MyProfile,on_delete=models.CASCADE)
    post=models.ForiegnKey(Posts,on_delete=models.CASCADE)