import time

import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.sanity
def test_login(page):
    login_page = LoginPage(page)
    login_page.load()
    
    # Example credentials - replace with valid ones if available
    username = "saran@qwalton.com"
    password = "ams@123"

    login_page.login(username, password)

    # time.sleep(5)
    # Verify login success by checking for a specific element or title 
    assert page.title() == "Athlete Management System"  # Replace with actual title or verification
    
    home_page = HomePage(page)
    home_page.menu()

    #time.sleep(5)
    print(f"Page Title: {page.title()}") 
    print("Hi") 
    print("Test completed successfully")

