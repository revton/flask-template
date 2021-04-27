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
    text_step = loads(context.text)
    columns = context.browser.find_elements(*name)
    contains = False
    for i in columns:
        if i.text.strip() == text_step["name"]:
            contains = True
    assert contains
