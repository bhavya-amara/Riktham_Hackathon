from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    path('',views.login,name='login'),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name='login'),
    path("viewposts",views.displayposts,name="viewposts"),
    path("viewprofile",views.displaymyposts,name="viewprofile"),
    path("createissue",views.upload,name='createissue')
]
if settings.DEBUG:
    urlpatterns.append(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))