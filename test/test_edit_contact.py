from model.contact import Contact


def test_edit_contact(app):

    app.contact.edit_first_contact(Contact("firstname", "middlename", "lastname", "nickname", "", "",
                                           "address", "home", "mobile", "work", "fax", "email", "",
                                           "", "", "1", "December", "1998", "-", "-"))
