"""
Data for Property Tests
"""

# Base imports
from datetime import datetime


DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
STATUS_NAMES = ['comprando', 'comprado', 'pre_venta', 'en_venta', 'vendido',]

properties_test_data = [
    {
        'address': 'address_%d'%_id,
        'city': 'city_%d'%_c,
        'price': _id * 100000,
        'description': 'house_%d'%_id,
        'year': 2000 + _id,
    }
    for _id, _c in zip(
        range(1,7),
        [1 if i < 4 else 2 for i in range(1,7)]
    )
]


status_test_data = [
    {
        'name': name,
        'label': label
    }
    for name, label in zip(
        STATUS_NAMES,
        [
            "Imueble en proceso de compra",
            "Inmueble en propiedad de Habi",
            "Inmueble publicado en preventa",
            "Inmueble publicado en venta",
            "Inmueble vendido",
        ]
    )
]


status_history_test_data = [
    {
        'property': prop,
        'status': status,
        'update_date': datetime.strptime(up_date, DATE_FORMAT),
    }
    for prop, status, up_date in zip(
        [2000+i for i in [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]],
        [STATUS_NAMES[i-1] for i in [1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5]],
        [
            '2021-04-10 22:23:56',
            '2021-04-11 22:23:56',
            '2021-04-12 22:23:56',
            '2021-04-09 22:23:56',
            '2021-04-10 22:23:56',
            '2021-04-11 22:23:56',
            '2021-04-12 22:23:56',
            '2021-04-12 22:26:25',
            '2021-04-12 22:26:34',
            '2021-04-12 22:26:54',
            '2021-04-12 22:27:06',
            '2021-04-12 22:27:20',
            '2021-04-10 22:23:56',
            '2021-04-11 22:23:56',
            '2021-04-12 22:23:56',
            '2021-04-09 22:23:56',
            '2021-04-10 22:23:56',
            '2021-04-11 22:23:56',
            '2021-04-12 22:23:56',
            '2021-04-12 22:26:25',
            '2021-04-12 22:26:34',
            '2021-04-12 22:26:54',
            '2021-04-12 22:27:06',
            '2021-04-12 22:27:20',
        ]
    )
]


expected_filter_1 = [{
    "address": "address_1",
    "city": "city_1",
    "status": "pre_venta",
    "price": 100000,
    "description": "house_1"
}]


expected_filter_2 = []


expected_filter_3 = [{
    "address": "address_3",
    "city": "city_1",
    "status": "vendido",
    "price": 300000,
    "description": "house_3"
}]


expected_filter_4 = [{
    "address": "address_5",
    "city": "city_2",
    "status": "en_venta",
    "price": 500000,
    "description": "house_5"
}]


expected_filter_5 = [{
    "address": "address_1",
    "city": "city_1",
    "status": "pre_venta",
    "price": 100000,
    "description": "house_1"
},
{
    "address": "address_2",
    "city": "city_1",
    "status": "en_venta",
    "price": 200000,
    "description": "house_2"
},
{
    "address": "address_3",
    "city": "city_1",
    "status": "vendido",
    "price": 300000,
    "description": "house_3"
},
{
    "address": "address_4",
    "city": "city_2",
    "status": "pre_venta",
    "price": 400000,
    "description": "house_4"
},
{
    "address": "address_5",
    "city": "city_2",
    "status": "en_venta",
    "price": 500000,
    "description": "house_5"
},
{
    "address": "address_6",
    "city": "city_2",
    "status": "vendido",
    "price": 600000,
    "description": "house_6"
}]


expected_filter_6 = [{
    "address": "address_4",
    "city": "city_2",
    "status": "pre_venta",
    "price": 400000,
    "description": "house_4"
}]


expected_filter_7 = [{
    "address": "address_4",
    "city": "city_2",
    "status": "pre_venta",
    "price": 400000,
    "description": "house_4"
},
{
    "address": "address_5",
    "city": "city_2",
    "status": "en_venta",
    "price": 500000,
    "description": "house_5"
},
{
    "address": "address_6",
    "city": "city_2",
    "status": "vendido",
    "price": 600000,
    "description": "house_6"
}]


expected_filter_8 = [{
    "address": "address_5",
    "city": "city_2",
    "status": "en_venta",
    "price": 500000,
    "description": "house_5"
}]


expected_filter_9 = [{
    "address": "address_6",
    "city": "city_2",
    "status": "vendido",
    "price": 600000,
    "description": "house_6"
}]


expected_filter_10 = [{
    "address": "address_1",
    "city": "city_1",
    "status": "pre_venta",
    "price": 100000,
    "description": "house_1"
}]


expected_filter_11 = [{
    "address": "address_2",
    "city": "city_1",
    "status": "en_venta",
    "price": 200000,
    "description": "house_2"
},
{
    "address": "address_5",
    "city": "city_2",
    "status": "en_venta",
    "price": 500000,
    "description": "house_5"
}]
