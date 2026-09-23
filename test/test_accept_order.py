import allure

import helpers


class TestAcceptOrder:
    @allure.title('Заказ можно принять')
    def test_accept_order_success(self, courier, order):
        response = helpers.accept_order(order['id'], courier['id'])
        assert response.status_code == 200
        assert response.json() == {'ok': True}

    @allure.title('Нельзя принять заказ без id курьера')
    def test_accept_order_without_courier_id(self, order):
        response = helpers.accept_order(order['id'])
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Нельзя принять заказ с неверным id курьера')
    def test_accept_order_wrong_courier_id(self, order):
        response = helpers.accept_order(order['id'], 999999999)
        assert response.status_code == 404
        assert response.json()['message'] == 'Курьера с таким id не существует'

    @allure.title('Нельзя принять заказ без id заказа')
    def test_accept_order_without_order_id(self, courier):
        response = helpers.accept_order('', courier['id'])
        assert response.status_code == 404
        assert response.json()['message'] == 'Not Found.'

    @allure.title('Нельзя принять заказ с неверным id заказа')
    def test_accept_order_wrong_order_id(self, courier):
        response = helpers.accept_order(999999999, courier['id'])
        assert response.status_code == 404
        assert response.json()['message'] == 'Заказа с таким id не существует'
