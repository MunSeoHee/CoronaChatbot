"""project URL Configuration

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
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index, name='index'),
    path('<int:board_id>', app.views.read, name='read'),
    path('delete/<int:board_id>', app.views.delete, name='delete'),
    path('update/<int:board_id>', app.views.update, name='update'),
    path('up/<int:board_id>', app.views.up, name='up'),
    path('create', app.views.create, name='create'),
    path('new', app.views.new, name='new')
]
