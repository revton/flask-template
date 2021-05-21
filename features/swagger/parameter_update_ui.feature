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
    Then return json valid of PUT /parameters/1
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

  Scenario: Update a parameter who not exists
    Given open the page swagger-ui
    When execute PUT /parameters/9999
    """
      {
        "name": "Parameter-Name not exists",
        "value": "Parameter-Value not exists"
      }
    """
    Then return json error message with status code 404 of PUT /parameters/9999
    """
      {
        "message": "Parâmetro não encontrado."
      }
    """


  Scenario: Update a parameter only value
    Given open the page swagger-ui
    When execute PATCH /parameters/1
    """
      {
        "value": "Parameter-Value update only"
      }
    """
    Then return json valid of PATCH /parameters/1
    """
      {
        "id": 1,
        "name": "Parameter-Name update",
        "value": "Parameter-Value update only",
        "_links": {
            "self": "/api/v1/parameters/1",
            "collection": "/api/v1/parameters/"
        }
      }
    """

  Scenario: Update a parameter only value who not exists
    Given open the page swagger-ui
    When execute PATCH /parameters/9999
    """
      {
        "value": "Parameter-Value not exists"
      }
    """
    Then return json error message with status code 404 of PATCH /parameters/9999
    """
      {
        "message": "Parâmetro não encontrado."
      }
    """