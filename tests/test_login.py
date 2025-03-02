import pytest
from pages.home_page import HomePage

@pytest.mark.sanity
def test_login(logged_in_page):
    assert logged_in_page.title() == "Athlete Management System"

    # This assumes you are testing Super Admin login here. Change if needed.
    home_page = HomePage(logged_in_page, role="Super Admin")

    # Super Admin should go to Manage > User
    home_page.navigate_to("Manage User")

    print(f"Page Title: {logged_in_page.title()}")
    print("Admin login test completed successfully")

    home_page.logout()
