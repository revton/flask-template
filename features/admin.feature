Feature: Admin

  Scenario: Open the index page of admin
    Given flask-template is setup
    When open the page index of admin
    Then should see the link to "Admin"