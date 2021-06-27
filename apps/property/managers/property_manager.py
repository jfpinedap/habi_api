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

    visible_fields = ['address', 'city', 'status', 'price', 'description']
    visible_status = ['pre_venta', 'en_venta', 'vendido']


    def filtered_properties(self, year: str=None, city: str=None, status: str=None) -> list:
        """
        Return properties list filtered by year of construction, city and status.
        """
        data = []
        year_filter = '' if year is None else 'p.year = %s'%year
        city_filter = '' if city is None else "p.city = '%s'"%city

        status_filter = (
            " AND ps1.status = '%s' "%status
            if status in self.visible_status
            else ''
        )

        visible_status_filter = 's.name IN (%s)'%', '.join(
            ["'%s'"%vs for vs in self.visible_status]
        )

        filters = [year_filter, city_filter, visible_status_filter]
        filters = list(filter(('').__ne__, filters))
        filters = ' and '.join(filters)
        filters = '' if filters == '' else 'WHERE %s'%filters
        with connection.cursor() as cursor:

            sql = """
                SELECT {_fields}
                FROM
                    (SELECT p.id,
                           p.address,
                           p.city,
                           p.price,
                           p.description,
                           p.year,
                           sh.update_date,
                           s.name AS status,
                           s.label AS label
                    FROM   property p
                           INNER JOIN status_history AS sh
                                   ON p.id = sh.property_id
                           INNER JOIN status AS s
                                   ON sh.status_id = s.id
                    {_filters} -- WHERE statement
                    ) AS ps1
                LEFT JOIN (SELECT p.id,
                                  p.address,
                                  p.city,
                                  p.price,
                                  p.description,
                                  p.year,
                                  sh.update_date,
                                  s.name AS status,
                                  s.label AS label
                           FROM   property p
                                  INNER JOIN status_history AS sh
                                          ON p.id = sh.property_id
                                  INNER JOIN status AS s
                                          ON sh.status_id = s.id
                           {_filters} -- WHERE statement
                           ) AS  ps2
                ON ( ps1.id = ps2.id AND ps1.update_date < ps2.update_date )
                WHERE  ps2.id IS NULL {_status_filter}
                """.format(
                    _fields=', '.join('ps1.%s'%vf for vf in self.visible_fields),
                    _filters=filters,
                    _status_filter=status_filter
                )

            cursor.execute(sql)

            data = [{
                field:row[i] for i, field in enumerate(self.visible_fields)
            } for row in cursor.fetchall()]

        return data