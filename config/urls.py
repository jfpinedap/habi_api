"""
habiapi URL Configuration
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # URL applications
    path('property', include('apps.property.urls')),
]
