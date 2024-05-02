from model.contact import Contact


def test_edit_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact("firstname", "middlename", "lastname", "nickname", "", "",
                                           "address", "home", "mobile", "work", "fax", "email", "",
                                           "", "", "1", "December", "1998", "-", "-"))
    app.session.logout()
