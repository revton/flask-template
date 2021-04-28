Feature: Admin

    Scenario: Open the index page of admin
        Given flask-template is setup
        When open the page index of admin
        Then should see the link to "Admin"

    Scenario: Open the user screen of Admin
        Given flask-template is setup
        When open the page index of admin
        Then should see the link to "User" and click
        Then go to url "admin/user/"

    Scenario: Create user in Admin
        Given that is on url "admin/user/new/"
        When create user
        """
            {
                "name": "Revton",
                "email": "revtonbr@gmail.com"
            }
        """
        Then See user created
        """
            {
                "name": "Revton",
                "email": "revtonbr@gmail.com"
            }
        """

    Scenario: Edit user in Admin
        Given that is on url "admin/user/"
        When click in link to edit user
        """
            {
                "name": "Revton editado",
                "email": "revtonbr_atualizado@gmail.com"
            }
        """
        Then See user created
        """
            {
                "name": "Revton editado",
                "email": "revtonbr_atualizado@gmail.com"
            }
        """

    Scenario: Remove user in Admin
        Given that is on url "admin/user/"
        When click in button to remove user
            | name           | email                         |
            | Revton editado | revtonbr_atualizado@gmail.com |
        Then Not see user removed
            | name           | email                         |
            | Revton editado | revtonbr_atualizado@gmail.com |
