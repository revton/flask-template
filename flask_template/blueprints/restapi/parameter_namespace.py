# -*- coding: utf-8 -*-
"""Parameter namespace."""
from flask import request
from flask_restx import Namespace, Resource
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

from flask_template.business import parameter_business
from flask_template.schema import ParameterSchema

ns_parameter = Namespace(
    "parameter", description="Routes to manager parameters"
)


@ns_parameter.route("/", endpoint="parameter")
class ParameterResource(Resource):
    """Routes to manager parameters."""

    def post(self):
        """Create parameter."""
        parameter_schema = ParameterSchema()
        try:
            parameter = parameter_schema.load(request.json)
            parameter_business.create(parameter)
        except ValidationError as error:
            self.api.abort(400, error.messages)
        except IntegrityError as error:
            self.api.abort(400, error.args[0])
        return parameter_schema.dump(parameter), 201
