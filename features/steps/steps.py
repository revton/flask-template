from behave import given, then, when


@given(u"flask-template is setup")
def step_impl(context):
    assert context.server


@when(u"open the page")
def step_impl(context):
    context.browser.get("http://127.0.0.1:5001/")
    assert context.browser.current_url == "http://127.0.0.1:5001/"


@then(u'should see the message "{message}"')
def step_impl(context, message):
    assert context.browser.current_url == "http://127.0.0.1:5001/"
    assert message in context.browser.page_source
