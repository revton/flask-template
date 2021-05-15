Feature: Update Parameter in Swagger-UI

  Scenario: Update a parameter
    Given open the page swagger-ui
    When execute PUT /parameters/1
    """
      {
        "name": "Parameter-Name update",
        "value": "Parameter-Value update"
      }
    """
    Then return json valid of POST /parameters/1
    """
      {
        "id": 1,
        "name": "Parameter-Name update",
        "value": "Parameter-Value update",
        "_links": {
            "self": "/api/v1/parameters/1",
            "collection": "/api/v1/parameters/"
        }
      }
    """

  Scenario: Update a parameter without data
    Given open the page swagger-ui
    When execute PUT /parameters/1
    """
      {}
    """
    Then return json error message with status code 400 of PUT /parameters/1
    """
      {
        "message": "{'value': ['Missing data for required field.'], 'name': ['Missing data for required field.']}"
      }
    """