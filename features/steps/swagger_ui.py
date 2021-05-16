# -*- coding: utf-8 -*-
""" Steps to test behave"""
import time
from json import loads

from behave import given, then, when
from selenium.webdriver.common.by import By

from flask_template.utils.json_utils import ordered


@given("open the page swagger-ui")
def step_impl(context):  # noqa
    context.browser.get("http://127.0.0.1:5001/api/v1/")


@when("execute GET /parameters/")
def step_impl(context):  # noqa
    _execute_request_swagger(
        context,
        div_operation="operations-parameters-get_parameter_create_and_list",
    )


@when("execute POST /parameters/")
def step_impl(context):  # noqa
    _execute_request_swagger(
        context,
        div_operation="operations-parameters-post_parameter_create_and_list",
        has_payload=True,
    )


@when("execute PUT /parameters/{identifier}")
def step_impl(context, identifier):  # noqa
    _execute_request_swagger(
        context,
        div_operation="operations-parameters-put_parameter_get_and_update",
        has_payload=True,
        table_operation="parameters",
        table_values={"identifier": identifier},
    )


@when("execute PATCH /parameters/{identifier}")
def step_impl(context, identifier):  # noqa
    _execute_request_swagger(
        context,
        div_operation="operations-parameters-patch_parameter_get_and_update",
        has_payload=True,
        table_operation="parameters",
        table_values={"identifier": identifier},
    )


@when("execute DELETE /parameters/{identifier}")
def step_impl(context, identifier):  # noqa
    _execute_request_swagger(
        context,
        div_operation="operations-parameters-delete_parameter_get_and_update",
        table_operation="parameters",
        table_values={"identifier": identifier},
    )


@when("execute GET /parameters/{identifier}")
def step_impl(context, identifier):  # noqa
    _execute_request_swagger(
        context,
        div_operation="operations-parameters-get_parameter_get_and_update",
        table_operation="parameters",
        table_values={"identifier": identifier},
    )


@then("return json valid of GET /parameters/")
def step_impl(context):  # noqa
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-get_parameter_create_and_list",
        status_code=200,
    )


@then("return json valid of POST /parameters/")
def step_impl(context):  # noqa
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-post_parameter_create_and_list",
        status_code=201,
    )


@then(
    "return json error message with status code {status_code} "
    "of POST /parameters/"
)
def step_impl(context, status_code):  # noqa
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-post_parameter_create_and_list",
        status_code=int(status_code),
    )


@then(
    "return json error message with status code {status_code} "
    "of PUT /parameters/{identifier}"
)
def step_impl(context, status_code, identifier):  # noqa
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-put_parameter_get_and_update",
        status_code=int(status_code),
    )


@then("return json valid of PUT /parameters/{identifier}")
def step_impl(context, identifier):  # noqa
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-put_parameter_get_and_update",
        status_code=200,
    )


@then("return json valid of PATCH /parameters/{identifier}")
def step_impl(context, identifier):  # noqa
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-patch_parameter_get_and_update",
        status_code=200,
    )


@then(
    "return json error message with status code {status_code} "
    "of PATCH /parameters/{identifier}"
)
def step_impl(context, status_code, identifier):  # noqa
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-patch_parameter_get_and_update",
        status_code=int(status_code),
    )


@then(
    "return json error message with status code {status_code} "
    "of DELETE /parameters/{identifier}"
)
def step_impl(context, status_code, identifier):  # noqa
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-delete_parameter_get_and_update",
        status_code=int(status_code),
    )


@then("return status code {status_code} of DELETE /parameters/{identifier}")
def step_impl(context, status_code, identifier):  # noqa
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-delete_parameter_get_and_update",
        status_code=int(status_code),
    )


@then(
    "return json error message with status code {status_code} "
    "of GET /parameters/{identifier}"
)
def step_impl(context, status_code, identifier):  # noqa
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-get_parameter_get_and_update",
        status_code=int(status_code),
    )


@then("return json valid of GET /parameters/{identifier}")
def step_impl(context, identifier):  # noqa
    _assert_response_swagger(
        context,
        div_operation="operations-parameters-get_parameter_get_and_update",
        status_code=200,
    )


def _execute_request_swagger(
    context,
    div_operation: str,
    has_payload: bool = False,
    table_operation: str = None,
    table_values: dict = {},
):
    time.sleep(2)
    div_element_operation = context.browser.find_element_by_id(div_operation)
    div_element_operation.click()
    time.sleep(2)

    class_try_out = (By.CLASS_NAME, "try-out__btn")
    btn_try_out = div_element_operation.find_element(*class_try_out)
    btn_try_out.click()

    if has_payload:
        time.sleep(2)
        class_payload = (By.CLASS_NAME, "body-param__text")
        text_payload = div_element_operation.find_element(*class_payload)
        text_payload.clear()
        text_payload.send_keys(str(context.text))

    if table_operation:
        time.sleep(2)
        class_parameters = (By.CLASS_NAME, table_operation)
        table_parameters = div_element_operation.find_element(
            *class_parameters
        )

        tag_tbody = (By.TAG_NAME, "tbody")
        tbody_parameters = table_parameters.find_element(*tag_tbody)

        for key, value in table_values.items():
            tr_identifier = tbody_parameters.find_element_by_xpath(
                f"//tr[@data-param-name='{key}']"
            )
            class_td_description = (
                By.CLASS_NAME,
                "parameters-col_description",
            )
            td_description = tr_identifier.find_element(*class_td_description)

            tag_input = (By.TAG_NAME, "input")
            input_identifier = td_description.find_element(*tag_input)
            input_identifier.clear()
            input_identifier.send_keys(str(value))

    class_execute = (By.CLASS_NAME, "execute")
    btn_execute = div_element_operation.find_element(*class_execute)
    btn_execute.click()


def _assert_response_swagger(context, div_operation: str, status_code: int):
    time.sleep(2)
    div_post_parameter = context.browser.find_element_by_id(div_operation)

    class_tr_response = (By.CLASS_NAME, "response")
    tr_response = div_post_parameter.find_element(*class_tr_response)

    class_col_status = (By.CLASS_NAME, "response-col_status")
    td_col_status = tr_response.find_element(*class_col_status)
    assert td_col_status.text == str(status_code)

    # When status code is 204 - No Content have not response description
    if status_code != 204:
        class_col_description = (By.CLASS_NAME, "response-col_description")
        td_col_description = tr_response.find_element(*class_col_description)

        class_language_json = (By.CLASS_NAME, "language-json")
        code_language_json = td_col_description.find_element(
            *class_language_json
        )

        assert ordered(loads(context.text)) == ordered(
            loads(code_language_json.text)
        )
