# -*- coding: utf-8 -*-
def test_app_flask(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
