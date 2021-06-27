"""
Views of Property
"""

# Libraries
from django.conf import settings
from django.utils.decorators import method_decorator
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from . import models


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class PropertyView(APIView):
    """
    Property View
    """
    model = models.Property

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request):
        year = request.GET.get('year', None)
        city = request.GET.get('city', None)
        status = request.GET.get('status', None)

        properties = models.Property.objects.filtered_properties(
            year=year, city=city, status=status
        )

        return Response(
            data={
                'Response': properties
            }
        )
