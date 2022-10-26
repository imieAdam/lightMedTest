
import unittest
from src.api_consumer import ApiConsumer

class TestLoginLogout(unittest.TestCase):
    def test_login_logout(self):
        test_apis = ApiConsumer()
        test_apis.read_config()
        you_were_logged_out = test_apis.config["logged_out"]
        response = test_apis.login()
        assert len(response.history) == 2
        assert response.history[0].status_code == 302
        assert response.history[1].status_code == 302
        assert response.status_code == 200
        assert (test_apis.config["logged_in"] in response.content.decode("utf-8"))
        response = test_apis.logout()
        assert response.status_code == 200
        assert (you_were_logged_out in response.content.decode("utf-8"))