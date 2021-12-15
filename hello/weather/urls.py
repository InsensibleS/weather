from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Weather


urlpatterns = [
    path('find', Weather.as_view()),
]
