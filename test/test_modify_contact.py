from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="new firstname")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="new lastname")
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#
# def test_modify_contact_bday(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="firstname"))
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(bday="1")
#     contact.id = old_contacts[0].id
#     app.contact.modify_first_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[0] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
