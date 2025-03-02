import pytest
from pages.home_page import HomePage

@pytest.mark.sanity
def test_science_staff_login(logged_in_page):
    assert logged_in_page.title() == "Athlete Management System"

    # This assumes you are testing Super Admin login here. Change if needed.
    home_page = HomePage(logged_in_page, role="Science staff")

    # Super Admin should go to Manage > User
    home_page.navigate_to("Sports Cognitive")

    print(f"Page Title: {logged_in_page.title()}")
    print("Admin login test completed successfully")

    home_page.logout()
