from utils.config import load_config
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_science_staff_login(page):
    config = load_config("SCIENCE_STAFF")
    login_page = LoginPage(page, config['BASE_URL'])
    login_page.login(config['USERNAME'], config['PASSWORD'])

    assert page.title() == "Athlete Management System"

    home_page = HomePage(page)
    home_page.menu()
    home_page.logout()

    print("ORG Admin Login Test Completed Successfully")