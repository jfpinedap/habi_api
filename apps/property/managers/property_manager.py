"""
Property manager.
"""

# Base imports
from django.db import connection
from django.db.models import Manager


class PropertyManager(Manager):
    """
    Property Manager Class
    """

    def filtered_properties(self, year: str=None, city: str=None, status: str=None) -> list:
        """
        Return properties list filtered by year of construction, city and status.
        """
        data = []

        return data