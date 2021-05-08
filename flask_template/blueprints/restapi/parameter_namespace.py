# -*- coding: utf-8 -*-
"""Parameter namespace."""
from flask import request, url_for
from flask_restx import Namespace, Resource
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError, NoResultFound

from flask_template.business import parameter_business
from flask_template.schema import ParameterSchema

ns_parameter = Namespace(
    "parameters", description="Routes to manager parameters"
)


@ns_parameter.route("/", endpoint="parameters")
class ParameterCreateAndList(Resource):
    """Routes to create and list parameters."""

    def post(self):
        """Create a parameter."""
        parameter_schema = ParameterSchema()
        try:
            parameter = parameter_schema.load(request.json)
            parameter_business.create(parameter)
        except ValidationError as error:
            self.api.abort(400, error.messages)
        except IntegrityError as error:
            self.api.abort(422, error.args[0])
        else:
            return (
                parameter_schema.dump(parameter),
                201,
                {
                    "location": url_for(
                        "api.parameter_by_id", identifier=parameter.id
                    )
                },
            )

    def get(self):
        """List all parameters."""
        parameter_schema = ParameterSchema(many=True)
        parameters = parameter_business.list_all()
        return parameter_schema.dump(parameters), 200


@ns_parameter.route("/<int:identifier>", endpoint="parameter_by_id")
class ParameterGetAndUpdate(Resource):
    """Route to get, update and delete parameter given its identifier."""

    def get(self, identifier):
        """Get a parameter given its identifier."""
        parameter = parameter_business.get_by_id(identifier=identifier)
        if parameter:
            parameter_schema = ParameterSchema()
            return parameter_schema.dump(parameter), 200
        else:
            self.api.abort(404, "Parâmetro não encontrado.")

    def put(self, identifier):
        """Update a parameter given its identifier."""
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
            self.api.abort(422, error.args[0])
        else:
            return parameter_schema.dump(parameter_update)

    def delete(self, identifier):
        """Delete a parameter given its identifier."""
        try:
            parameter_business.delete_by_id(identifier=identifier)
        except NoResultFound as error:
            self.api.abort(404, error.args[0])
        return "", 204

    def patch(self, identifier):
        """Partially updates a parameter given its identifier."""
        try:
            parameter_schema = ParameterSchema()
            parameter_schema.load(request.json, partial=True)
            parameter_update = parameter_business.update(
                identifier, request.json
            )
        except ValidationError as error:
            self.api.abort(400, error.messages)
        except NoResultFound as error:
            self.api.abort(404, error.args[0])
        except IntegrityError as error:
            self.api.abort(422, error.args[0])
        else:
            return parameter_schema.dump(parameter_update)
