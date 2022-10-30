import unittest
from src.api_consumer import ApiConsumer

class TestApis(unittest.TestCase):

    def ntest_get_forgery_token(self):
        api_consumer = ApiConsumer()
        api_consumer.read_config()
        api_consumer.login()
        json = api_consumer.get_forgery_token()
        api_consumer.logout()
        assert len(json["token"]) > 1

    def test_get_doctors_and_facilities(self):
        api_consumer = ApiConsumer()
        api_consumer.read_config()
        api_consumer.login()
        api_consumer.get_forgery_token()
        json = api_consumer.get_doctors_and_facilities()
        api_consumer.logout()
        #print(json)
        assert len(json["doctors"]) > 1