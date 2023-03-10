import allure


@allure.feature("API Tests")
class TestAPI:

    @allure.title("test_1")
    def test_1(self, base_url, session):
        with allure.step('请求百度'):
            response = session.get(base_url)
            assert response.status_code == 200

    @allure.title("test_2")
    def test_2(self, base_url, session):
        with allure.step('请求百度'):
            response = session.get(base_url)
            assert response.status_code == 200

    @allure.title("test_3")
    def test_3(self, base_url, session):
        with allure.step('请求百度'):
            response = session.get(base_url)
            assert response.status_code == 200

    @allure.title("test_4")
    def test_4(self, base_url, session):
        with allure.step('请求百度'):
            response = session.get(base_url)
            assert response.status_code == 200

    @allure.title("test_5")
    def test_5(self, base_url, session):
        with allure.step('请求百度'):
            response = session.get(base_url)
            assert response.status_code == 200

    @allure.title("test_6")
    def test_6(self, base_url, session):
        with allure.step('请求百度'):
            response = session.get(base_url)
            assert response.status_code == 200

    @allure.title("test_7")
    def test_7(self, base_url, session):
        with allure.step('请求百度'):
            response = session.get(base_url)
            assert response.status_code == 200

    @allure.title("test_8")
    def test_8(self, base_url, session):
        with allure.step('请求百度'):
            response = session.get(base_url)
            assert response.status_code == 200

    @allure.title("test_9")
    def test_9(self, base_url, session):
        with allure.step('请求百度'):
            response = session.get(base_url)
            assert response.status_code == 200

    @allure.title("test_10")
    def test_10(self, base_url, session):
        with allure.step('请求百度'):
            response = session.get(base_url)
            assert response.status_code == 200
