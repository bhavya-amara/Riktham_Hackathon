from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Posts(models.Model):
    profile=models.ForeignKey(MyProfile,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images/",null=True,verbose_name="")
    likes=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
class comments(models.Model):
    user=models.ForeignKey(MyProfile,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    messages=models.CharField(max_length=100)
    
    