# -*- coding: utf-8 -*-
import json

import pytest
from flask.testing import FlaskClient

from flask_template.app import create_app


class TestClient(FlaskClient):
    def post_json(self, url, data, follow_redirects=False):
        response = self.post(
            url,
            data=json.dumps(data),
            headers={"content-type": "application/json"},
            follow_redirects=follow_redirects,
        )
        return response


@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.test_client_class = TestClient
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
