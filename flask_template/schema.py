# -*- coding: utf-8 -*-
"""Module Schemas."""
from marshmallow import ValidationError, validates

from flask_template.extensions.serializer import ma
from flask_template.model import Parameter


class ParameterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Parameter
        load_instance = True

    @validates("name")
    def validate_empty_name(self, value):
        if not value:
            raise ValidationError("Campo não pode ser vazio.")

    @validates("value")
    def validate_empty_value(self, value):
        if not value:
            raise ValidationError("Campo não pode ser vazio.")
