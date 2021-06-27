"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FirstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('ht/',views.htmltag),
    path('usr/<str:uname>/',views.usernameprint),
    path('usa/<str:un>/<int:ag>/',views.usernameage),
    path('qw/',views.htm),
    path('registerform/',views.registerform,name='registerform'),
    path('bt',views.bt,name='bt'),
    path('register1/',views.register1),
    path('register2/',views.register2,name= "register2"),
    path('display/',views.display,name="dt"),
    path('viw/<int:y>/',views.sview,name="sv"),
    path('upu/<int:q>/',views.supt,name="sup"),
    

]
