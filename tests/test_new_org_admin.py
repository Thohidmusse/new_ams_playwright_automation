import pytest
from pages.new_org_admin_page import NewOrgAdminPage
# from pages.login_page import LoginPage
# from utils.config import USERNAME, PASSWORD

@pytest.mark.regression 
def test_new_org_admin(logged_in_page): 
    newcoach_page = NewOrgAdminPage(logged_in_page) 
    newcoach_page.create_new_org_admin() 

# @pytest.mark.regression
# def test_new_org_admin(page):
#     login_page = LoginPage(page)
#     login_page.load()
    
#     login_page.login(USERNAME, PASSWORD)
    
#     # Verify login success by checking for a specific element or title 
#     assert page.title() == "Athlete Management System"  # Replace with actual title or verification
    
    
#     newcoach_page = NewOrgAdminPage(page)
#     newcoach_page.create_new_org_admin()
     