from datetime import datetime
from pony.orm import *
from model.group import Group
from model.contact import Contact
import random


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups",
                       lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts",
                     lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind("mysql", host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_contact_by_id(self, id):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.id == id))[0]

    def get_available_contact_and_group(self):
        groups = self.get_group_list()
        contacts = self.get_contact_list()
        available_items = {}
        for group in groups:
            if len(self.get_contacts_in_group(group)) < len(contacts):
                contacts_ids = [i.id for i in contacts]
                contacts_in_group_ids = [i.id for i in self.get_contacts_in_group(group)]
                available_group = group
                available_contact_id = list(set(contacts_ids).difference(contacts_in_group_ids))[0]
                available_contact = self.get_contact_by_id(available_contact_id)
                available_items = {"group": available_group, "contact": available_contact}
                return available_items
        return available_items

    def get_available_contact_and_group_del(self):
        groups = self.get_group_list()
        available_items = {}
        for group in groups:
            if len(self.get_contacts_in_group(group)):
                available_contact = random.choice(self.get_contacts_in_group(group))
                available_group = group
                available_items = {"group": available_group, "contact": available_contact}
                return available_items
        return available_items

    def is_contact_in_group(self, contact, group):
        contact_ids_in_group = [i.id for i in self.get_contacts_in_group(group)]
        if contact.id in contact_ids_in_group:
            return True
        return False
