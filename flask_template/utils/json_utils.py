# -*- coding: utf-8 -*-
"""Module with functions utils of json."""
import ast


def ordered(obj):
    """Sort dict or list"""
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    if isinstance(obj, str):
        _converter_string_to_dict(obj)
    else:
        return obj


def _converter_string_to_dict(obj: str) -> dict:
    try:
        obj_dict = ast.literal_eval(obj)
        return ordered(obj_dict)
    except SyntaxError:
        return obj
    except ValueError:
        return obj
