from django.contrib import admin
from .models import MyProfile,Posts,comments
# Register your models here.
admin.site.register(MyProfile)
admin.site.register(Posts)
admin.site.register(comments)