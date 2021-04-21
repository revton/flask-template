from behave import given, then, when


@given(u"flask-template is setup")
def step_impl(context):
    assert context.client


@when(u"open the page")
def step_impl(context):
    context.page = context.client.get("/")
    assert context.page


@then(u'should see the message "{message}"')
def step_impl(context, message):
    assert message in str(context.page.data)
