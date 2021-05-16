Feature: List Parameter in Swagger-UI

  Scenario: List all parameter
    Given open the page swagger-ui
    When execute GET /parameters/
    Then return json valid of GET /parameters/
    """
      [{
        "id": 1,
        "name": "Parameter-Name",
        "value": "Parameter-Value",
        "_links": {
            "self": "/api/v1/parameters/1",
            "collection": "/api/v1/parameters/"
        }
      },
      {
        "id": 2,
        "name": "Parameter-Name to be delete",
        "value": "Parameter-Value to be delete",
        "_links": {
            "self": "/api/v1/parameters/2",
            "collection": "/api/v1/parameters/"
        }
      }]
    """