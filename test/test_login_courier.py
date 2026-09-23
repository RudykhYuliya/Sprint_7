import allure
import pytest

import helpers


class TestLoginCourier:
    @allure.title('Курьер может авторизоваться')
    def test_login_courier_success(self, courier):
        response = helpers.login_courier(courier['login'], courier['password'])
        assert response.status_code == 200
        assert response.json()['id'] == courier['id']

    @allure.title('Нельзя авторизоваться без обязательного поля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_login_courier_without_required_field(self, courier, field):
        login = '' if field == 'login' else courier['login']
        password = '' if field == 'password' else courier['password']
        response = helpers.login_courier(login, password)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Нельзя авторизоваться с неверным логином или паролем')
    @pytest.mark.parametrize('login_key, password_key', [
        ('wrong', 'password'),
        ('login', 'wrong'),
    ])
    def test_login_courier_wrong_credentials(self, courier, login_key, password_key):
        login = courier['login'] if login_key == 'login' else courier['login'] + 'x'
        password = courier['password'] if password_key == 'password' else courier['password'] + 'x'
        response = helpers.login_courier(login, password)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Нельзя авторизоваться под несуществующим пользователем')
    def test_login_nonexistent_courier(self):
        payload = helpers.generate_courier()
        response = helpers.login_courier(payload['login'], payload['password'])
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'
