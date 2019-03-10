"""LikeWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from testApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('static/<path:path>',views.getImage),
    path('testApp/index',views.index),
    path('testApp/upload',views.upload),
    path('testApp/upload2',views.upload2),
    path('testApp/show',views.show),
    path('testApp/show2',views.show2),
    path('testApp/show3',views.show2),
    path('testApp/upload_file',views.upload_file),
    path('js/<path:path>', views.getJS),
    path('testApp/<path:path>', views.getPath),
]
