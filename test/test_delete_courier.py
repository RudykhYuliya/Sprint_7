import allure

import helpers


class TestDeleteCourier:
    @allure.title('Курьера можно удалить')
    def test_delete_courier_success(self, courier):
        response = helpers.delete_courier(courier['id'])
        assert response.status_code == 200
        assert response.json() == {'ok': True}

    @allure.title('Нельзя удалить курьера без id')
    def test_delete_courier_without_id(self):
        response = helpers.delete_courier('')
        assert response.status_code == 404
        assert response.json()['message'] == 'Not Found.'

    @allure.title('Нельзя удалить курьера с несуществующим id')
    def test_delete_courier_nonexistent_id(self):
        response = helpers.delete_courier(999999999)
        assert response.status_code == 404
        assert response.json()['message'] == 'Курьера с таким id нет.'
