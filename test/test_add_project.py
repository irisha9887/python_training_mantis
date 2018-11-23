from generator.project import *
import pytest

testdata = [Project(name=random_strings("name", 10), status=random_status(), view_state=random_view_status(),
                    inherit_global=random_boolean(), description=random_strings("description", 30))]

@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project, db):
    app.navigation.open_manage_project_page()
    old_projects = db.get_project_list()
    app.project.add_project(project)
    app.navigation.open_manage_project_page()
    new_projects = db.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)





