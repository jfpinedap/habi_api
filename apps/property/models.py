"""Property models"""

# Django imports
from django.db import models

# Manager imports
from apps.property.managers import PropertyManager


class Status(models.Model) :
    """
    Status Class Model
    """
    name = models.CharField(max_length=32, null=False)
    label = models.CharField(max_length=64, null=False)

    def __str__(self):
        """
        Shows up in the admin list.
        """
        return self.name

    class Meta:
        """
        Meta Class to define the name of the database table
        to use for the Status model.
        """
        db_table = 'status'
        unique_together = (("id", "name"),)


class Property(models.Model):
    """
    Property Class Model
    """
    address = models.CharField(max_length=120, null=False)
    city = models.CharField(max_length=32, null=True)
    price = models.BigIntegerField()
    description = models.TextField()
    year = models.SmallIntegerField()

    # Status
    status = models.ManyToManyField(Status, through='StatusHistory', related_name='status_histories')

    objects = PropertyManager()

    def __str__(self):
        """
        Shows up in the admin list.
        """
        return str(self.year)

    class Meta:
        """
        Meta Class to define the name of the database table
        to use for the Property model.
        """
        db_table = 'property'


class StatusHistory(models.Model):
    """
    StatusHistory Class Model
    """
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    update_date = models.DateTimeField()

    def __str__(self):
        """
        Shows up in the admin list.
        """
        return 'Property {_prop} is {_stat} at {_date}'.format(
            _prop=self.property_id,
            _stat=self.status_id.name,
            _date=self.updated_date.strftime('%Y%m%d')
        )

    class Meta:
        """
        Meta Class to define the name of the database table
        to use for the StatusHistory model.
        """
        db_table = 'status_history'
