from playwright.sync_api import Page

class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_tab = page.locator("a:has-text('Admin')")
        self.add_button = page.locator("button:has-text('Add')")
        self.search_input = page.locator("input[placeholder='Username']")
        self.search_button = page.locator("button:has-text('Search')")
        self.user_checkbox = lambda username: page.locator(f"//div[text()='{username}']/ancestor::div[contains(@class, 'oxd-table-row')]//input")
        self.delete_button = page.locator("button:has-text('Delete')")
        self.confirm_delete_button = page.locator("button:has-text('Yes, Delete')")

    def navigate_to_admin(self):
        self.admin_tab.click()

    def click_add_user(self):
        self.add_button.click()

    def fill_user_details(self, employee_name, username, password, status="Enabled", user_role="ESS"):
        # Select user role
        self.page.locator("label:has-text('User Role')").locator("..").locator("div").nth(1).click()
        self.page.locator(f"div[role='option']:has-text('{user_role}')").click()

        # Enter employee name
        self.page.locator("input[placeholder='Type for hints...']").fill(employee_name)
        self.page.locator("div[role='listbox'] >> text=" + employee_name).click()

        # Enter username
        self.page.locator("label:has-text('Username')").locator("..").locator("input").fill(username)

        # Select status
        self.page.locator("label:has-text('Status')").locator("..").locator("div").nth(1).click()
        self.page.locator(f"div[role='option']:has-text('{status}')").click()

        # Enter password and confirm
        self.page.locator("label:has-text('Password')").locator("..").locator("input").fill(password)
        self.page.locator("label:has-text('Confirm Password')").locator("..").locator("input").fill(password)

    def save_user(self):
        self.page.locator("button:has-text('Save')").click()

    def search_user(self, username):
        self.search_input.fill(username)
        self.search_button.click()

    def delete_user(self, username):
        self.user_checkbox(username).check()
        self.delete_button.click()
        self.confirm_delete_button.click()
