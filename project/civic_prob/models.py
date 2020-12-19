from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Posts(models.Model):
    profile=models.ForeignKey(MyProfile,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="static/images/",null=True,verbose_name="")
    likes=models.IntegerField()
    date=models.DateTimeField()
    time=models.TimeField()

class comments(models.Model):
    messages=models.CharField(max_length=100)
    user=models.ForeignKey(MyProfile,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)