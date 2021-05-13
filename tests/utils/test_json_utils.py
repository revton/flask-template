# -*- coding: utf-8 -*-
from flask_template.utils.json_utils import ordered


def test_json_utils_simple():
    dict_1 = {"a": "1", "b": "2"}
    dict_2 = {"b": "2", "a": "1"}
    assert dict_1 == dict_2


def test_json_utils_complex_diff():
    dict_1 = {
        "errors": [
            {"error": "invalid", "field": "email"},
            {"error": "required", "field": "name"},
        ],
        "success": False,
    }
    dict_2 = {
        "success": False,
        "errors": [
            {"error": "required", "field": "name"},
            {"error": "invalid", "field": "email"},
        ],
    }
    assert dict_1 != dict_2


def test_json_utils_complex_diff_ordered():
    dict_1 = {
        "errors": [
            {"error": "invalid", "field": "email"},
            {"error": "required", "field": "name"},
        ],
        "success": False,
    }
    dict_2 = {
        "success": False,
        "errors": [
            {"error": "required", "field": "name"},
            {"error": "invalid", "field": "email"},
        ],
    }
    assert ordered(dict_1) == ordered(dict_2)
