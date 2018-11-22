from model.project import Project

def test_add_project(app, json_projects):
    project = json_projects
    app.navigation.open_login_page()
    app.session.login("administrator", "root")
    app.project.add_project(project)


