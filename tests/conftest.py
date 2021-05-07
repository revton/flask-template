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

    def get_json(self, url, follow_redirects=False):
        response = self.get(
            url,
            headers={"content-type": "application/json"},
            follow_redirects=follow_redirects,
        )
        return response

    def delete_json(self, url, follow_redirects=False):
        response = self.delete(
            url,
            headers={"content-type": "application/json"},
            follow_redirects=follow_redirects,
        )
        return response

    def put_json(self, url, data, follow_redirects=False):
        response = self.put(
            url,
            data=json.dumps(data),
            headers={"content-type": "application/json"},
            follow_redirects=follow_redirects,
        )
        return response

    def patch_json(self, url, data, follow_redirects=False):
        response = self.patch(
            url,
            data=json.dumps(data),
            headers={"content-type": "application/json"},
            follow_redirects=follow_redirects,
        )
        return response


@pytest.fixture(scope="session")
def test_client():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    app.test_client_class = TestClient
    with app.test_client() as testing_client:
        with app.app_context():
            app.extensions["sqlalchemy"].db.create_all()
            yield testing_client
            app.extensions["sqlalchemy"].db.drop_all()
