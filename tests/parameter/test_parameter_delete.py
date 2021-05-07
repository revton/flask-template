# -*- coding: utf-8 -*-
from flask import url_for


def test_paramter_delete_without_id(test_client):
    response = test_client.delete_json(
        url=url_for("api.parameter_by_id", identifier=999)
    )
    assert response.status_code == 404
    assert "Parâmetro não encontrado." in response.json["message"]


def test_parameter_delete_ok(test_client):
    data = {"name": "param-name", "value": "param-value"}
    expected_response = {
        "id": 2,
        "name": "param-name",
        "value": "param-value",
    }
    response = test_client.post_json(url=url_for("api.parameter"), data=data)
    assert response.status_code == 201
    assert response.json == expected_response

    parameter_id = response.json["id"]
    response = test_client.delete_json(
        url=url_for("api.parameter_by_id", identifier=parameter_id)
    )
    assert response.status_code == 204
