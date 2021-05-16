# -*- coding: utf-8 -*-
"""Module with functions utils of json."""


def ordered(obj):
    """Sort dict or list"""
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj
