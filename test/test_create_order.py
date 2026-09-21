import allure
import pytest

import data
import helpers


class TestCreateOrder:
    @allure.title('Можно создать заказ')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        None,
    ])
    def test_create_order_returns_track(self, color, order_tracks):
        payload = data.ORDER.copy()
        if color is not None:
            payload['color'] = color
        response = helpers.create_order(payload)
        assert response.status_code == 201
        assert 'track' in response.json()
        order_tracks.append(response.json()['track'])
