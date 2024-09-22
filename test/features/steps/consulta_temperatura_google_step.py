from behave import given, when, then

@given(u'que eu estou no site do google')
def step_impl(context):
    pass


@when(u'eu pesquiso a temperatura de hoje')
def step_impl(context):
    pass


@then(u'o navegador deve trazer a temperatura de hoje')
def step_impl(context):
    pass


@then(u'Fecho o navegador')
def step_impl(context):
    pass
