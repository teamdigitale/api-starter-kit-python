import logging

import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder

from throttling_quota import ThrottlingQuota


class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.App(__name__, specification_dir="../swagger/")
        app.app.json_encoder = JSONEncoder
        app.add_api("swagger.yaml")
        app.app.config["quota-store"] = ThrottlingQuota(20, 10, dict())

        return app.app
