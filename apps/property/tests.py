"""Property tests"""

# Libraries
import copy
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from .models import Property, Status, StatusHistory

# Data
from .test_data.data import *


class PropertyTestCase(APITestCase):

    def setUp(self):
        [Property.objects.create(**data) for data in properties_test_data]
        [Status.objects.create(**data) for data in status_test_data]

        sh_data = copy.deepcopy(status_history_test_data)
        for i, data in enumerate(sh_data):
            pro_ = Property.objects.get(year=int(str(data['property'])))
            sta_ = Status.objects.get(name=data['status'])
            new_data = {
                'property': pro_,
                'status': sta_,
            }
            status_history_test_data[i].update(new_data)

        [StatusHistory.objects.create(**data)
        for data in status_history_test_data]

    def test_case(self):
        """
        Ensure that test are runing
        """
        self.assertEqual(1, 1)

    def test_property_model(self):
        property_1 = Property.objects.get(description="house_1")
        property_2 = Property.objects.get(description="house_2")
        self.assertEqual(property_1.price, 100000)
        self.assertEqual(property_2.price, 200000)


    def test_status_model(self):
        status_1 = Status.objects.get(label="Inmueble vendido")
        status_2 = Status.objects.get(name="pre_venta")
        self.assertEqual(status_1.name, "vendido")
        self.assertEqual(status_2.label, "Inmueble publicado en preventa")

    def test_status_history_model(self):
        property = Property.objects.get(description="house_3")
        status_1 = Status.objects.get(name="comprado")
        status_2 = Status.objects.get(name="en_venta")
        status_history_1 = StatusHistory.objects.filter(
            property_id=property.id
        ).filter(status_id=status_1.id)
        status_history_2 = StatusHistory.objects.filter(
            property_id=property.id
        ).filter(status_id=status_2.id)
        self.assertEqual(
            status_history_1[0].update_date.strftime(DATE_FORMAT),
            '2021-04-12 22:26:34'
        )
        self.assertEqual(
            status_history_2[0].update_date.strftime(DATE_FORMAT),
            '2021-04-12 22:27:06'
        )

    def test_property_manager(self):
        properties_1 = Property.objects.filtered_properties(year='2001', city='city_1')
        properties_2 = Property.objects.filtered_properties(year='2002', city='city_2')
        properties_3 = Property.objects.filtered_properties(year='2003', city='city_1')
        properties_4 = Property.objects.filtered_properties(year='2005', city='city_2')
        properties_5 = Property.objects.filtered_properties()
        properties_6 = Property.objects.filtered_properties(year='2004')
        properties_7 = Property.objects.filtered_properties(city='city_2')
        properties_8 = Property.objects.filtered_properties(year='2005', city='city_2', status='en_venta')
        properties_9 = Property.objects.filtered_properties(city='city_2', status='vendido')
        properties_10 = Property.objects.filtered_properties(city='city_1', status='pre_venta')
        properties_11 = Property.objects.filtered_properties(status='en_venta')

        self.assertEqual(properties_1, expected_filter_1)
        self.assertEqual(properties_2, expected_filter_2)
        self.assertEqual(properties_3, expected_filter_3)
        self.assertEqual(properties_4, expected_filter_4)
        self.assertEqual(properties_5, expected_filter_5)
        self.assertEqual(properties_6, expected_filter_6)
        self.assertEqual(properties_7, expected_filter_7)
        self.assertEqual(properties_8, expected_filter_8)
        self.assertEqual(properties_9, expected_filter_9)
        self.assertEqual(properties_10, expected_filter_10)
        self.assertEqual(properties_11, expected_filter_11)

    def test_get_valid_property_endpoint(self):
        """
        Ensure that property endpoint works.
        """
        url = '/property?city=city_1&year=2000'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
