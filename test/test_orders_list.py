import allure

import helpers


class TestOrdersList:
    @allure.title('В теле ответа возвращается список заказов')
    def test_get_orders_returns_list(self):
        response = helpers.get_orders()
        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)
