from model.contact import Contact
import time


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname"))
    app.contact.modify_first_contact(Contact(firstname="new firstname"))


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname"))
    app.contact.modify_first_contact(Contact(lastname="new lastname"))


def test_modify_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname"))
    app.contact.modify_first_contact(Contact(bday="1"))
