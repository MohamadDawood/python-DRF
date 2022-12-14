"""apiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from django import template

from app import views


router = routers.DefaultRouter()
router.register(r'allusers', views.JobViewSet)

urlpatterns = [
    # use this for none standard
    path('JobListApiView', views.JobListApiView.as_view()),
    path('', include(router.urls)),
    path('allusersmethod', views.A.ideal_weight),
    # and these tow for standard
    path('basic/', views.ApiObjects.as_view()),
    path('basic/<int:pk>/', views.ApiObjectDetails.as_view()),

    path('methodfromhtml',views.methodfromhtml,name='methodfromhtml')
    ]
