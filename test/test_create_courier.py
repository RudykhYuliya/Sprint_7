import allure
import pytest

import helpers


class TestCreateCourier:
    @allure.title('Можно создать курьера')
    def test_create_courier_success(self, courier_payload):
        response = helpers.register_courier(courier_payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_two_identical_couriers_conflict(self, courier_payload):
        helpers.register_courier(courier_payload)
        response = helpers.register_courier(courier_payload)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Нельзя создать курьера без обязательного поля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_required_field(self, courier_payload, field):
        payload = courier_payload.copy()
        payload.pop(field)
        response = helpers.register_courier(payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'
