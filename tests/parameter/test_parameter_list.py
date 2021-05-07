# -*- coding: utf-8 -*-
from flask import url_for


def test_parameter_get_all(test_client):
    response = test_client.get_json(url=url_for("api.parameters"))
    assert response.status_code == 200
    assert response.json == [
        {"id": 1, "name": "project-name", "value": "Flask Template"}
    ]


def test_parameter_get_by_id_not_exists(test_client):
    response = test_client.get_json(
        url=url_for("api.parameter_by_id", identifier=9999)
    )
    assert response.status_code == 404
    assert "Parâmetro não encontrado." in response.json["message"]


def test_parameter_get_by_id_exist(test_client):
    response = test_client.get_json(
        url=url_for("api.parameter_by_id", identifier=1)
    )
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "name": "project-name",
        "value": "Flask Template",
    }
