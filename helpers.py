import random
import string

import requests

import data

TIMEOUT = 30


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_courier():
    return {
        'login': generate_random_string(10),
        'password': generate_random_string(10),
        'firstName': generate_random_string(10),
    }


def register_courier(payload):
    return requests.post(data.BASE_URL + data.CREATE_COURIER, json=payload, timeout=TIMEOUT)


def login_courier(login, password):
    return requests.post(
        data.BASE_URL + data.LOGIN_COURIER,
        json={'login': login, 'password': password},
        timeout=TIMEOUT,
    )


def delete_courier(courier_id):
    return requests.delete(
        data.BASE_URL + data.DELETE_COURIER + str(courier_id),
        timeout=TIMEOUT,
    )


def create_order(payload):
    return requests.post(data.BASE_URL + data.CREATE_ORDER, json=payload, timeout=TIMEOUT)


def cancel_order(track):
    return requests.put(data.BASE_URL + data.CANCEL_ORDER, json={'track': track}, timeout=TIMEOUT)


def finish_order(order_id):
    return requests.put(data.BASE_URL + data.FINISH_ORDER + str(order_id), timeout=TIMEOUT)


def get_order(track):
    params = None if track is None else {'t': track}
    return requests.get(data.BASE_URL + data.GET_ORDER, params=params, timeout=TIMEOUT)


def get_orders():
    return requests.get(data.BASE_URL + data.ORDERS_LIST, timeout=TIMEOUT)


def accept_order(order_id, courier_id=None):
    params = None if courier_id is None else {'courierId': courier_id}
    return requests.put(
        data.BASE_URL + data.ACCEPT_ORDER + str(order_id),
        params=params,
        timeout=TIMEOUT,
    )
