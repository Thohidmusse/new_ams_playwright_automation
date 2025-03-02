import pytest
from pages.home_page import HomePage

@pytest.mark.sanity
def test_org_admin_login(logged_in_page):
    assert logged_in_page.title() == "Athlete Management System"

    # Create HomePage with role = Assessor
    home_page = HomePage(logged_in_page, role="Organization admin")

    # Navigate to the correct menu for Assessor
    home_page.navigate_to("Sports Talent Identification")

    print(f"Page Title: {logged_in_page.title()}")
    print("Test completed successfully")

    home_page.logout()
