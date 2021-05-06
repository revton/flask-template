# -*- coding: utf-8 -*-
"""Parameter namespace."""
from flask import request
from flask_restx import Namespace, Resource
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError, NoResultFound

from flask_template.business import parameter_business
from flask_template.schema import ParameterSchema

ns_parameter = Namespace(
    "parameter", description="Routes to manager parameters"
)


@ns_parameter.route("/", endpoint="parameter")
class ParameterCreateAndList(Resource):
    """Routes to create and list parameters."""

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
        else:
            return parameter_schema.dump(parameter), 201

    def get(self):
        """List parameters"""
        parameter_schema = ParameterSchema(many=True)
        parameters = parameter_business.list_all()
        return parameter_schema.dump(parameters), 200


@ns_parameter.route("/<int:identifier>", endpoint="parameter_by_id")
class ParameterGetAndUpdate(Resource):
    """Route to get and update parameter."""

    def get(self, identifier):
        """Get parameter by id."""
        parameter = parameter_business.get_by_id(identifier=identifier)
        if parameter:
            parameter_schema = ParameterSchema()
            return parameter_schema.dump(parameter), 200
        else:
            self.api.abort(404, "Parâmetro não encontrado.")

    def post(self, identifier):
        """Update parameter by id."""
        try:
            parameter_schema = ParameterSchema()
            parameter_schema.load(request.json)
            parameter_update = parameter_business.update(
                identifier, request.json
            )
        except ValidationError as error:
            self.api.abort(400, error.messages)
        except NoResultFound as error:
            self.api.abort(404, error.args[0])
        except IntegrityError as error:
            self.api.abort(400, error.args[0])
        else:
            return parameter_schema.dump(parameter_update)
