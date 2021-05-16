Feature: Delete Parameter in Swagger-UI

  Scenario: Delete a parameter not exists
    Given open the page swagger-ui
    When execute DELETE /parameters/999
    Then return json error message with status code 404 of DELETE /parameters/999
    """
      {
        "message": "Parâmetro não encontrado."
      }
    """

  Scenario: Delete a parameter
    Given open the page swagger-ui
    When execute DELETE /parameters/2
    Then return status code 204 of DELETE /parameters/2