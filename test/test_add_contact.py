# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("Darwin", "Iago", "Ast", "Arctic lemming",
                               "Dr", "Thoughtmix", "PO Box 20674", "427-565-7932",
                               "846-844-2236", "269-616-5785", "-", "iast2@wp.com",
                               "iast2@1und1.de", "iast3@gmail.com", "test", "5",
                               "October", "1990", "21", "December"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("", "", "", "", "", "",
                               "", "", "", "", "", "", "",
                               "", "", "", "-", "", "", "-"))
    app.session.logout()
