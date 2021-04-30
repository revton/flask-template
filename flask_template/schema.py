# -*- coding: utf-8 -*-
"""Module Schemas."""
from flask_template.extensions.serializer import ma
from flask_template.model import Parameter


class ParameterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Parameter
        load_instance = True
