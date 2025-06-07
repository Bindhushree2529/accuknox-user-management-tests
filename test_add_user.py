
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

def test_add_user(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(page)
    login.login("Admin", "admin123")

    dashboard = DashboardPage(page)
    dashboard.navigate_to_admin()

    admin = AdminPage(page)
    admin.click_add_user()
    admin.fill_user_details("Paul Collings", "paul.test.user", "Test@123")
    admin.save_user()

    # Optionally add assertions here to confirm user was added
