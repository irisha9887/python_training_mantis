from selenium.webdriver.support.ui import Select
class ProjectHelper:

    def __init__(self, app):
        self.app = app


    def fill_project_name_field(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)

    def fill_status_field(self, project):
        wd = self.app.wd
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)

    def fill_view_status_field(self, project):
        wd = self.app.wd
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_state)

    def fill_description_field(self,project):
        wd = self.app.wd
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    def add_project(self, project):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_name_field(project)
        self.fill_status_field(project)
        if (project.inherit_global):
            wd.find_element_by_name("inherit_global").click()
        self.fill_view_status_field(project)
        self.fill_description_field(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        self.select_project_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()



