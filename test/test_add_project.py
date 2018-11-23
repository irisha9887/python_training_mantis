from generator.project import Project
from generator.project import random_strings

def test_add_project(app, json_projects, db):
    #project = json_projects
    app.navigation.open_manage_project_page()
    old_projects = db.get_project_list()
    #app.project.random_strings()
    #app.genarator.random_strings()
    project = [Project(name=random_strings("name", 10), status="stable", view_state="private",
             description=random_strings("description", 30))]
    app.project.add_project(project)
    app.navigation.open_manage_project_page()
    new_projects = db.get_project_list()
    if old_projects == new_projects:
        assert len(old_projects) == len(new_projects)
    else:
        assert len(old_projects) + 1 == len(new_projects)





