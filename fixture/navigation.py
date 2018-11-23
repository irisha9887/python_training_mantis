class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/login_page.php")

    def open_manage_overview_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/manage_overview_page.php")

    def open_manage_project_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")



