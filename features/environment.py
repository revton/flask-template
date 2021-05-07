# -*- coding: utf-8 -*-
""" Setup environment of behave """
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler

from ipdb import spost_mortem
from selenium import webdriver

from flask_template.app import create_app


def before_all(context):
    """Setup to create flask application
    and start simple_server
    and setup Chrome Browser.
    """
    context.server = simple_server.WSGIServer(("", 5001), WSGIRequestHandler)
    context.server.set_app(create_app(FORCE_ENV_FOR_DYNACONF="testing"))

    app = context.server.get_app()
    with app.app_context():
        app.extensions["sqlalchemy"].db.create_all()

    context.thread = threading.Thread(target=context.server.serve_forever)
    context.thread.start()

    context.browser = webdriver.Chrome()
    context.browser.set_page_load_timeout(time_to_wait=200)


def after_all(context):
    """ Close Browser and shutdown simple_server."""
    context.browser.quit()
    app = context.server.get_app()
    with app.app_context():
        app.extensions["sqlalchemy"].db.drop_all()
    context.server.shutdown()
    context.thread.join()


def after_step(context, step):
    """ Setup to debug after each step is executed."""
    if context.config.userdata.getbool("debug") and step.status == "failed":
        spost_mortem(step.exc_traceback)
