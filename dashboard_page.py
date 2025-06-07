
class DashboardPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_admin(self):
        self.page.locator("a[href*='admin']").click()
