# -*- coding: utf-8 -*-
from flask import url_for


def test_parameter_update_where_id_not_exists(test_client):
    data = {"name": "project-name update", "value": "Flask Template update"}
    response = test_client.put_json(
        url=url_for("api.parameter_by_id", identifier=9999), data=data
    )
    assert response.status_code == 404
    assert "Parâmetro não encontrado." in response.json["message"]


def test_parameter_update_where_id_exists_without_data(test_client):
    data = {}
    response = test_client.put_json(
        url=url_for("api.parameter_by_id", identifier=1), data=data
    )
    assert response.status_code == 400
    assert (
        "'name': ['Missing data for required field.']"
        in response.json["message"]
    )
    assert (
        "'value': ['Missing data for required field.']"
        in response.json["message"]
    )


def test_parameter_update_where_id_exists_wihout_value(test_client):
    data = {"name": "project-name update"}
    response = test_client.put_json(
        url=url_for("api.parameter_by_id", identifier=1), data=data
    )
    assert response.status_code == 400
    assert (
        "'value': ['Missing data for required field.']"
        in response.json["message"]
    )


def test_parameter_update_where_id_exists_without_name(test_client):
    data = {"value": "Flask Template update"}
    response = test_client.put_json(
        url=url_for("api.parameter_by_id", identifier=9999), data=data
    )
    assert response.status_code == 400
    assert (
        "'name': ['Missing data for required field.']"
        in response.json["message"]
    )


def test_parameter_update_where_id_exists(test_client):
    data = {"name": "project-name update", "value": "Flask Template update"}
    response = test_client.put_json(
        url=url_for("api.parameter_by_id", identifier=1), data=data
    )
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "name": "project-name update",
        "value": "Flask Template update",
    }


def test_parameter_update_where_name_already_exists(test_client):
    data_new = {"name": "parameter_1", "value": "value_1"}
    expected_created_response = {
        "id": 2,
        "name": "parameter_1",
        "value": "value_1",
    }
    response = test_client.post_json(
        url=url_for("api.parameters"), data=data_new
    )
    assert response.status_code == 201
    assert response.json == expected_created_response

    data_exists = {
        "name": "project-name update",
        "value": "Flask Template update",
    }
    response = test_client.put_json(
        url=url_for("api.parameter_by_id", identifier=2), data=data_exists
    )
    assert response.status_code == 422
    assert "UNIQUE constraint failed: parameter.name" in str(
        response.json["message"]
    )


def test_parameter_update_only_value_not_exists(test_client):
    data = {"value": "Flask Template update"}
    response = test_client.patch_json(
        url=url_for("api.parameter_by_id", identifier=9999), data=data
    )
    assert response.status_code == 404
    assert "Parâmetro não encontrado." in response.json["message"]


def test_parameter_update_only_value_none(test_client):
    data = {"value": None}
    response = test_client.patch_json(
        url=url_for("api.parameter_by_id", identifier=2), data=data
    )
    assert response.status_code == 400
    assert response.json["message"] == "{'value': ['Field may not be null.']}"


def test_parameter_update_only_value_empty(test_client):
    data = {"value": ""}
    response = test_client.patch_json(
        url=url_for("api.parameter_by_id", identifier=2), data=data
    )
    assert response.status_code == 400
    assert "'value': ['Campo não pode ser vazio.']" in response.json["message"]


def test_parameter_update_only_name_none(test_client):
    data = {"name": None}
    response = test_client.patch_json(
        url=url_for("api.parameter_by_id", identifier=2), data=data
    )
    assert response.status_code == 400
    assert response.json["message"] == "{'name': ['Field may not be null.']}"


def test_parameter_update_only_name_empty(test_client):
    data = {"name": ""}
    response = test_client.patch_json(
        url=url_for("api.parameter_by_id", identifier=2), data=data
    )
    assert response.status_code == 400
    assert "'name': ['Campo não pode ser vazio.']" in response.json["message"]


def test_parameter_update_only_value(test_client):
    data = {"value": "Flask Template update only value"}
    expected_update_response = {
        "id": 2,
        "name": "parameter_1",
        "value": "Flask Template update only value",
    }

    response = test_client.patch_json(
        url=url_for("api.parameter_by_id", identifier=2), data=data
    )
    assert response.status_code == 200
    assert response.json == expected_update_response


def test_parameter_update_only_name(test_client):
    data = {"name": "Flask Template parameter only value"}
    expected_update_response = {
        "id": 2,
        "name": "Flask Template parameter only value",
        "value": "Flask Template update only value",
    }

    response = test_client.patch_json(
        url=url_for("api.parameter_by_id", identifier=2), data=data
    )
    assert response.status_code == 200
    assert response.json == expected_update_response


def test_parameter_update_only_name_where_name_already_exists(test_client):
    data_new = {"name": "parameter_1", "value": "value_1"}
    expected_created_response = {
        "id": 3,
        "name": "parameter_1",
        "value": "value_1",
    }
    response = test_client.post_json(
        url=url_for("api.parameters"), data=data_new
    )
    assert response.status_code == 201
    assert response.json == expected_created_response

    data_exists = {"name": "project-name update"}
    response = test_client.patch_json(
        url=url_for("api.parameter_by_id", identifier=2), data=data_exists
    )
    assert response.status_code == 422
    assert "UNIQUE constraint failed: parameter.name" in str(
        response.json["message"]
    )
