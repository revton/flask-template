Feature: Create Parameter in Swagger-UI

  Scenario: Create a new parameter
    Given open the page swagger-ui
    When execute POST /parameters/
    """
      {
        "name": "Parameter-Name",
        "value": "Parameter-Value"
      }
    """
    Then return json valid of POST /parameters/
    """
      {
        "id": 1,
        "name": "Parameter-Name",
        "value": "Parameter-Value",
        "_links": {
            "self": "/api/v1/parameters/1",
            "collection": "/api/v1/parameters/"
        }
      }
    """

  Scenario: Create new parameter without data
    Given open the page swagger-ui
    When execute POST /parameters/
    """
      {}
    """
    Then return json error message with status code 400 of POST /parameters/
    """
      {
        "message": "{'value': ['Missing data for required field.'], 'name': ['Missing data for required field.']}"
      }
    """

  Scenario: Create new parameter with unique name
    Given open the page swagger-ui
    When execute POST /parameters/
    """
      {
        "name": "Parameter-Name",
        "value": "Parameter-Value"
      }
    """
    Then return json error message with status code 422 of POST /parameters/
    """
      {
        "message": "UNIQUE constraint failed: parameter.name"
      }
    """