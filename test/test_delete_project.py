from model.project import Project
import random


def test_delete_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.add_project(Project(name="Google", status="development", view_state="public", description="Project for Google issues" ))
    app.navigation.open_manage_project_page()
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = db.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)


