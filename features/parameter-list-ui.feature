Feature: Parameter in Swagger-UI

  Scenario: List all parameter
    Given open the page swagger-ui
    When execute GET /parameters/
    Then return json valid of GET /parameters/
    """
      [{
        "id": 1,
        "name": "Parameter-Name",
        "value": "Parameter-Value"
      }]
    """