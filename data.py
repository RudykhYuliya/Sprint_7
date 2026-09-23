BASE_URL = 'https://qa-scooter.education-services.ru'

CREATE_COURIER = '/api/v1/courier'
LOGIN_COURIER = '/api/v1/courier/login'
DELETE_COURIER = '/api/v1/courier/'
CREATE_ORDER = '/api/v1/orders'
ORDERS_LIST = '/api/v1/orders'
CANCEL_ORDER = '/api/v1/orders/cancel'
FINISH_ORDER = '/api/v1/orders/finish/'
ACCEPT_ORDER = '/api/v1/orders/accept/'
GET_ORDER = '/api/v1/orders/track'

ORDER = {
    'firstName': 'Naruto',
    'lastName': 'Uchiha',
    'address': 'Konoha, 142 apt.',
    'metroStation': 4,
    'phone': '+7 800 355 35 35',
    'rentTime': 5,
    'deliveryDate': '2026-12-12',
    'comment': 'Saske, come back to Konoha',
}
