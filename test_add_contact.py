# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_new_contact(Contact("Darwin", "Iago", "Ast", "Arctic lemming",
                                   "Dr", "Thoughtmix", "PO Box 20674", "427-565-7932",
                                   "846-844-2236", "269-616-5785", "-", "iast2@wp.com",
                                   "iast2@1und1.de", "iast3@gmail.com", "test", "5",
                                   "October", "1990", "21", "December"))
    app.logout()


def test_add_empty_contact(app):
    app.login("admin", "secret")
    app.create_new_contact(Contact("", "", "", "", "", "",
                                   "", "", "", "", "", "", "",
                                   "", "", "", "-", "", "", "-"))
    app.logout()
