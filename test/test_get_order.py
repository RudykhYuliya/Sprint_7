import allure

import helpers


class TestGetOrder:
    @allure.title('Заказ можно получить по номеру')
    def test_get_order_by_track_success(self, order):
        response = helpers.get_order(order['track'])
        assert response.status_code == 200
        assert response.json()['order']['track'] == order['track']

    @allure.title('Нельзя получить заказ без номера')
    def test_get_order_without_track(self):
        response = helpers.get_order(None)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Нельзя получить заказ с несуществующим номером')
    def test_get_order_nonexistent_track(self):
        response = helpers.get_order(999999999)
        assert response.status_code == 404
        assert response.json()['message'] == 'Заказ не найден'
