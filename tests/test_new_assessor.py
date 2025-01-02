import pytest
from pages.new_assessor_page import NewAssessorPage
# from pages.login_page import LoginPage
# from utils.config import USERNAME, PASSWORD

@pytest.mark.regression 
def test_new_assessor(logged_in_page):
    newassessor_page = NewAssessorPage(logged_in_page) 
    newassessor_page.create_new_assessor() 

# @pytest.mark.regression
# def test_new_assessor(page):
#     login_page = LoginPage(page)
#     login_page.load()
    
#     login_page.login(USERNAME, PASSWORD)
#     # Verify login success by checking for a specific element or title 
#     assert page.title() == "Athlete Management System"  # Replace with actual title or verification
    
    
#     newassessor_page = NewAssessorPage(page)
#     newassessor_page.create_new_assessor()
    