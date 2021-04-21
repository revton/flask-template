from behave import given, then, when


@given(u"flask-template is setup")
def step_impl(context):
    assert context.server


@when(u"open the page index")
def step_impl(context):
    context.browser.get("http://127.0.0.1:5001/")
    assert context.browser.current_url == "http://127.0.0.1:5001/"


@when(u'open the page index of admin')
def step_impl(context):
    context.browser.get("http://127.0.0.1:5001/admin")
    assert context.browser.current_url == "http://127.0.0.1:5001/admin/"


@then(u'should see the message "{message}"')
def step_impl(context, message):
    assert context.browser.current_url == "http://127.0.0.1:5001/"
    assert message in context.browser.page_source


@then(u'should see the link to "{text_link}"')
def step_impl(context, text_link):
    assert context.browser.current_url == "http://127.0.0.1:5001/admin/"
    assert context.browser.find_element_by_link_text(text_link)

