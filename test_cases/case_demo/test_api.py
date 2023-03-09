import allure


@allure.feature("API Tests")
class TestAPI:

    @allure.title("Get all users")
    def test_get_all_users(self, base_url, session):
        with allure.step('请求百度'):
            response = session.get(base_url)
            assert response.status_code == 200
