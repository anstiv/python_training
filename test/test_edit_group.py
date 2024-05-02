from model.group import Group


def test_edit_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group("group_name2", "logo2", "comment2"))
    app.session.logout()
