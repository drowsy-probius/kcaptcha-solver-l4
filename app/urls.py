"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from solver import captchar_solver

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kcaptchar/', captchar_solver)
]

"""
kcaptchar API usage example in python

import os
url = 'http://host:port/kcaptchar'

with open(path_img, 'rb') as img:
  name_img= os.path.basename(path_img)
  files= {'image': (name_img, img, 'multipart/form-data',{'Expires': '0'}) }
  with requests.Session() as s:
    r = s.post(url, files=files)
    print(r.status_code)



import requests
url = 'http://host:port/kcaptchar'
files = {'image': open('test.jpg', 'rb')}
requests.post(url, files=files)


curl -F image=@test.jpg 'http://host:port/kcaptchar'
"""
