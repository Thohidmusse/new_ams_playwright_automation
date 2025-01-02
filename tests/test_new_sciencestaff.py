import pytest
from pages.new_sciencestaff_page import ScienceStaffPage
# from pages.login_page import LoginPage
# from utils.config import USERNAME, PASSWORD

@pytest.mark.regression 
def test_new_sciencestaff(logged_in_page): 
    newsciencestaff_page = ScienceStaffPage(logged_in_page)
    newsciencestaff_page.create_new_sciencestaff()

# @pytest.mark.regression
# def test_new_sciencestaff(page):
#     login_page = LoginPage(page)
#     login_page.load()
    
#     # Example credentials - replace with valid ones if available
#     username = "saran@qwalton.com"
#     password = "ams@123"

#     login_page.login(USERNAME, PASSWORD)
#     # Verify login success by checking for a specific element or title 
#     assert page.title() == "Athlete Management System"  # Replace with actual title or verification
    
    
#     newsciencestaff_page = ScienceStaffPage(page)
#     newsciencestaff_page.create_new_sciencestaff()