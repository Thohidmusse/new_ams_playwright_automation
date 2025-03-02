import pytest
from pages.new_org_coach_page import NewCoachPage
# from pages.login_page import LoginPage
# from utils.config import USERNAME, PASSWORD

@pytest.mark.regression 
def test_org_new_coach(logged_in_page):
    newcoach_page = NewCoachPage(logged_in_page) 
    newcoach_page.create_new_coach() 

# @pytest.mark.regression
# def test_new_coach(page):
#     login_page = LoginPage(page)
#     login_page.load()

#     login_page.login(USERNAME, PASSWORD)
#     # Verify login success by checking for a specific element or title 
#     assert page.title() == "Athlete Management System"  # Replace with actual title or verification
    
    
#     newcoach_page = NewCoachPage(page)
#     newcoach_page.create_new_coach()
    