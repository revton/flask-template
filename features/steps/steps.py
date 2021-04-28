# -*- coding: utf-8 -*-
""" Steps to test behave"""
from json import loads

from behave import given, then, when
from selenium.webdriver.common.by import By


@given("flask-template is setup")
def step_impl(context):
    assert context.server


@given('that is on url "{url_destination}"')
def step_impl(context, url_destination):
    context.browser.get(f"http://127.0.0.1:5001/{url_destination}")
    assert (
        context.browser.current_url
        == f"http://127.0.0.1:5001/{url_destination}"
    )


@when("open the page index")
def step_impl(context):
    context.browser.get("http://127.0.0.1:5001/")
    assert context.browser.current_url == "http://127.0.0.1:5001/"


@when("open the page index of admin")
def step_impl(context):
    context.browser.get("http://127.0.0.1:5001/admin")
    assert context.browser.current_url == "http://127.0.0.1:5001/admin/"


@when("create user")
def step_impl(context):
    name = (By.ID, "name")
    email = (By.ID, "email")
    text_step = loads(context.text)
    context.browser.find_element(*name).send_keys(text_step["name"])
    context.browser.find_element(*email).send_keys(text_step["email"])
    context.browser.find_element_by_xpath("//input[@value='Save']").click()


@when("click in link to edit user")
def step_impl(context):
    context.browser.current_url == "http://127.0.0.1:5001/admin/user/"
    # TODO: Check if row is in context.text
    link_edit = context.browser.find_element_by_xpath(
        "//*[@id='no-more-tables']/table/tbody/tr/td[2]/a"
    )
    assert link_edit
    link_edit.click()
    "http://127.0.0.1:5001/admin/user/edit/" in context.browser.current_url
    name = (By.ID, "name")
    email = (By.ID, "email")
    text_step = loads(context.text)

    el_name = context.browser.find_element(*name)
    el_name.clear()
    el_name.send_keys(text_step["name"])

    el_email = context.browser.find_element(*email)
    el_email.clear()
    el_email.send_keys(text_step["email"])

    context.browser.find_element_by_xpath("//input[@value='Save']").click()


@when("click in button to remove user")
def step_impl(context):
    context.browser.current_url == "http://127.0.0.1:5001/admin/user/"

    table = (
        By.CLASS_NAME,
        "table",
    )
    table_elem = context.browser.find_element(*table)
    assert table_elem

    # TODO: Check if row is in context.table
    table_row = (By.TAG_NAME, "tr")
    rows_elem = table_elem.find_element(*table_row)
    assert rows_elem

    btn_remove = rows_elem.find_element_by_xpath("//td[2]/form/button")
    btn_remove.click()
    context.browser.switch_to_alert().accept()


@then('should see the message "{message}"')
def step_impl(context, message):
    assert context.browser.current_url == "http://127.0.0.1:5001/"
    assert message in context.browser.page_source


@then('should see the link to "{text_link}" and click')
def step_impl(context, text_link):
    link = context.browser.find_element_by_xpath(f"//a[text()='{text_link}']")
    assert link
    link.click()


@then('should see the link to "{text_link}"')
def step_impl(context, text_link):
    assert context.browser.find_element_by_xpath(
        f"//a[text()[normalize-space()]='{text_link}']"
    )


@then('go to url "{url_destination}"')
def step_impl(context, url_destination):
    assert (
        context.browser.current_url
        == f"http://127.0.0.1:5001/{url_destination}"
    )


@then("See user created")
def step_impl(context):
    name = (By.CSS_SELECTOR, "td.col-name")
    email = (By.CSS_SELECTOR, "td.col-email")
    text_step = loads(context.text)

    columns_name = context.browser.find_elements(*name)
    columns_email = context.browser.find_elements(*email)

    list_contains_name = [
        x for x in columns_name if x.text.strip() == text_step["name"]
    ]
    assert len(list_contains_name) > 0

    list_contains_email = [
        x for x in columns_email if x.text.strip() == text_step["email"]
    ]
    assert len(list_contains_email) > 0


@then("Not see user removed")
def step_impl(context):
    name = (By.CSS_SELECTOR, "td.col-name")
    email = (By.CSS_SELECTOR, "td.col-email")
    text_step = context.table

    columns_name = context.browser.find_elements(*name)
    columns_email = context.browser.find_elements(*email)

    list_contains_name = [
        x for x in columns_name if x.text.strip() == text_step["name"]
    ]
    assert len(list_contains_name) == 0

    list_contains_email = [
        x for x in columns_email if x.text.strip() == text_step["email"]
    ]
    assert len(list_contains_email) == 0
