# -*- coding: utf-8 -*-
""" Steps to test behave"""
import time
from json import loads

from behave import given, then, when
from selenium.webdriver.common.by import By

from flask_template.utils.json_utils import ordered


@given(u"open the page swagger-ui")
def step_impl(context):
    context.browser.get("http://127.0.0.1:5001/api/v1/")


@when(u"execute GET /parameters/")
def step_impl(context):
    _execute_request_swagger(
        context,
        div_operation="operations-parameters-get_parameter_create_and_list",
    )


@when(u"execute POST /parameters/")
def step_impl(context):
    _execute_request_swagger(
        context,
        div_operation="operations-parameters-post_parameter_create_and_list",
        has_payload=True,
    )


@then(u"return json valid of GET /parameters/")
def step_impl(context):
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-get_parameter_create_and_list",
        status_code=200,
    )


@then(u"return json valid of POST /parameters/")
def step_impl(context):
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-post_parameter_create_and_list",
        status_code=201,
    )


@then(
    u"return json error message with status code {status_code} of POST /parameters/"
)
def step_impl(context, status_code):
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-post_parameter_create_and_list",
        status_code=int(status_code),
    )


def _execute_request_swagger(
    context, div_operation: str, has_payload: bool = False
):
    time.sleep(2)
    div_post_parameter = context.browser.find_element_by_id(div_operation)
    div_post_parameter.click()
    time.sleep(2)

    class_try_out = (By.CLASS_NAME, "try-out__btn")
    btn_try_out = div_post_parameter.find_element(*class_try_out)
    btn_try_out.click()

    if has_payload:
        class_payload = (By.CLASS_NAME, "body-param__text")
        text_payload = div_post_parameter.find_element(*class_payload)
        text_payload.clear()
        text_payload.send_keys(str(context.text))

    class_execute = (By.CLASS_NAME, "execute")
    btn_execute = div_post_parameter.find_element(*class_execute)
    btn_execute.click()


def _assert_response_swagger(context, div_operation: str, status_code: int):
    time.sleep(2)
    div_post_parameter = context.browser.find_element_by_id(div_operation)

    class_tr_response = (By.CLASS_NAME, "response")
    tr_response = div_post_parameter.find_element(*class_tr_response)

    class_col_status = (By.CLASS_NAME, "response-col_status")
    td_col_status = tr_response.find_element(*class_col_status)
    assert td_col_status.text == str(status_code)

    class_col_description = (By.CLASS_NAME, "response-col_description")
    td_col_description = tr_response.find_element(*class_col_description)

    class_language_json = (By.CLASS_NAME, "language-json")
    code_language_json = td_col_description.find_element(*class_language_json)

    assert ordered(loads(context.text)) == ordered(
        loads(code_language_json.text)
    )
