import unittest
from src.api_consumer import ApiConsumer

class TestApis(unittest.TestCase):

    api_consumer = None

    def setUp(self) -> None:
        self.api_consumer = ApiConsumer()
        self.api_consumer.read_config()
        self.api_consumer.login()
        return super().setUp()

    def tearDown(self) -> None:
        self.api_consumer.logout()
        return super().tearDown()

    def test_read_config(self):
        assert self.api_consumer.config["key"] == "value"