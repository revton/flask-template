# -*- coding: utf-8 -*-
from flask import url_for


def test_parameter_get_all_when_empty(test_client):
    response = test_client.get_json(url=url_for("api.parameter"))
    assert response.status_code == 200
    assert response.json == [{'id': 1, 'name': 'project-name', 'value': 'Flask Template'}]
