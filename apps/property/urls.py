"""
Module for use of Property urls
"""

from django.urls import path
from . import views

app_name='property'

urlpatterns = [
    path('', views.PropertyView.as_view(), name='property'),
]
