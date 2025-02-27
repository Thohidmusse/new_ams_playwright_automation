from utils.config import load_config
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_org_admin_login(page):
    config = load_config("ORG_ADMIN")
    login_page = LoginPage(page, config['BASE_URL'])
    login_page.login(config['USERNAME'], config['PASSWORD'])

    assert page.title() == "Athlete Management System"

    home_page = HomePage(page)
    home_page.menu()
    home_page.logout()

    print("ORG Admin Login Test Completed Successfully")