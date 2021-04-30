# -*- coding: utf-8 -*-
def teste_commands_nao_existe(test_client):
    import os

    exit_status = os.system("flask nao_existe")
    assert exit_status != 0
