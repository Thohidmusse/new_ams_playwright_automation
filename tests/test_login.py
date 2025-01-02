import time

import pytest
# from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config_copy import load_config 

@pytest.mark.sanity 
def test_login(logged_in_page): 
    # config = load_config() 
    # username = config['USERNAME'] 
    # password = config['PASSWORD'] 
    # login_page = LoginPage(logged_in_page, config['BASE_URL']) 
    # login_page.login(username, password) 
    assert logged_in_page.title() == "Athlete Management System" 
    # Replace with actual title or verification 
    home_page = HomePage(logged_in_page) 
    home_page.menu() 
    print(f"Page Title: {logged_in_page.title()}") 
    print("Test completed successfully")
    home_page.logout()





# from utils.config import USERNAME, PASSWORD

# @pytest.mark.sanity
# def test_login(page):
#     login_page = LoginPage(page)
#     login_page.load()
    
#     login_page.login(USERNAME, PASSWORD)

#     # Verify login success by checking for a specific element or title 
#     assert page.title() == "Athlete Management System"  # Replace with actual title or verification
    
#     home_page = HomePage(page)
#     home_page.menu()

#     #time.sleep(5)
#     print(f"Page Title: {page.title()}") 
#     print("Hi") 
#     print("Test completed successfully")
 
