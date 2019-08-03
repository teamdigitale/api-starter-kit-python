# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.problem import Problem  # noqa: E501
from swagger_server.models.timestamps import Timestamps  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPublicController(BaseTestCase):
    """PublicController integration test stubs"""

    def test_get_echo(self):
        """Test case for get_echo

        Ritorna un timestamp in formato RFC5424.
        """
        response = self.client.open("/datetime/v1/echo", method="GET")
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))
        assert "x-ratelimit-limit" in response.headers

    def test_get_status(self):
        """Test case for get_status

        Ritorna lo stato dell'applicazione.
        """
        response = self.client.open("/datetime/v1/status", method="GET")
        if response.status_code == 200:
            self.assert200(
                response, "Response body is : " + response.data.decode("utf-8")
            )
        elif response.status_code == 503:
            self.assertTrue("random" in response.data.decode("utf-8"))

        assert 'no-store' == response.headers.get('cache-control')


if __name__ == "__main__":
    import unittest

    unittest.main()
