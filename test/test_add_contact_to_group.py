from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='new_group_name'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname"))
    available_items = orm.get_available_contact_and_group()
    if not available_items:
        app.contact.create(Contact(firstname="firstname"))
        available_items = orm.get_available_contact_and_group()
    contact = available_items["contact"]
    group = available_items["group"]
    assert not orm.is_contact_in_group(contact, group)
    app.contact.add_contact_to_group(contact, group)
    assert orm.is_contact_in_group(contact, group)
