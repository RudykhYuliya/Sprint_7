import pytest

import data
import helpers


@pytest.fixture
def courier_payload():
    payload = helpers.generate_courier()
    yield payload
    login = payload.get('login')
    password = payload.get('password')
    if not login or not password:
        return
    response = helpers.login_courier(login, password)
    if response.status_code == 200:
        helpers.delete_courier(response.json()['id'])


@pytest.fixture
def courier(courier_payload):
    helpers.register_courier(courier_payload)
    response = helpers.login_courier(courier_payload['login'], courier_payload['password'])
    courier_payload['id'] = response.json()['id']
    return courier_payload


@pytest.fixture
def order_tracks():
    tracks = []
    yield tracks
    for track in tracks:
        order = helpers.get_order(track)
        order_id = None
        if order.status_code == 200:
            order_id = order.json()['order']['id']
        cancelled = helpers.cancel_order(track)
        if cancelled.status_code != 200 and order_id is not None:
            helpers.finish_order(order_id)


@pytest.fixture
def order(order_tracks):
    response = helpers.create_order(data.ORDER)
    track = response.json()['track']
    order_tracks.append(track)
    body = helpers.get_order(track).json()['order']
    return body
