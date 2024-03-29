# -*- coding: utf-8 -*-
from flask import request, url_for


def test_parameter_create_without_data(test_client):
    data = {}
    response = test_client.post_json(url=url_for("api.parameters"), data=data)
    assert response.status_code == 400
    assert (
        "'name': ['Missing data for required field.']"
        in response.json["message"]
    )
    assert (
        "'value': ['Missing data for required field.']"
        in response.json["message"]
    )


def test_parameter_create_without_value(test_client):
    data = {"name": "project-name"}
    expected_response = {
        "message": "{'value': ['Missing data for required field.']}"
    }
    response = test_client.post_json(url=url_for("api.parameters"), data=data)
    assert response.status_code == 400
    assert response.json == expected_response


def test_parameter_create_without_name(test_client):
    data = {"value": "Flask Template"}
    expected_response = {
        "message": "{'name': ['Missing data for required field.']}"
    }
    response = test_client.post_json(url=url_for("api.parameters"), data=data)
    assert response.status_code == 400
    assert response.json == expected_response


def test_parameter_create_new(test_client):
    data = {"name": "project-name", "value": "Flask Template"}
    expected_response = {
        "id": 1,
        "name": "project-name",
        "value": "Flask Template",
        "_links": {
            "self": "/api/v1/parameters/1",
            "collection": "/api/v1/parameters/",
        },
    }
    response = test_client.post_json(url=url_for("api.parameters"), data=data)
    assert response.status_code == 201
    assert response.json == expected_response
    assert response.headers.get("Location") == request.url_root[:-1] + url_for(
        "api.parameter_by_id", identifier=response.json["id"]
    )


def test_parameter_create_unique_name(test_client):
    data = {"name": "project-name", "value": "Flask Template"}
    response = test_client.post_json(url=url_for("api.parameters"), data=data)
    assert response.status_code == 422
    assert "UNIQUE constraint failed: parameter.name" in str(
        response.json["message"]
    )
