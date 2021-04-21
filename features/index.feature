Feature: Index Screen

  Scenario: Open the index screen
    Given flask-template is setup
    When open the page
    Then should see the message "FLASK-TEMPLATE"