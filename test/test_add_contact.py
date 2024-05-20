# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("Darwin", "Iago", "Ast", "Arctic lemming",
                               "Dr", "Thoughtmix", "PO Box 20674", "427-565-7932",
                               "846-844-2236", "269-616-5785", "-", "iast2@wp.com",
                               "iast2@1und1.de", "iast3@gmail.com", "test", "5",
                               "October", "1990", "21", "December")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("", "", "", "", "", "",
                               "", "", "", "", "", "", "",
                               "", "", "", "-", "", "-", "-")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
