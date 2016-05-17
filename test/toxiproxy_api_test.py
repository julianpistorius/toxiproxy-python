from unittest import TestCase
from toxiproxy.api import validate_response
from toxiproxy.exceptions import NotFound

import requests


class IntoxicatedTest(TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8474/"

    def test_not_found(self):
        """ Test an invalid url """

        url_to_test = "%s/%s" % (self.base_url, "not_found")

        with self.assertRaises(NotFound) as context:
            validate_response(requests.get(url_to_test))
            self.assertTrue("404 page not found\n" in context.exception)