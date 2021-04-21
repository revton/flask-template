# -*- coding: utf-8 -*-
""" Setup environment of behave """
from behave import fixture, use_fixture
from ipdb import spost_mortem

from flask_template.app import create_app


@fixture
def flask_client(context, *args, **kwargs):
    """ Setting flask cliente to test """
    app = create_app()
    app.testing = True
    context.client = app.test_client()
    yield context.client


def before_feature(context, feature):
    """ Setup to create flask client before each feature is executed """
    use_fixture(flask_client, context)


def after_step(context, step):
    """ Setup to debug after each step is executed """
    if context.config.userdata.getbool("debug") and step.status == "failed":
        spost_mortem(step.exc_traceback)
