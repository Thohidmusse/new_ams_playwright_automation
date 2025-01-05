import pytest
from pages.new_assesment_page import AssessmentPage
from pages.login_page import LoginPage
# from utils.config import USERNAME, PASSWORD

@pytest.mark.end_to_end
@pytest.mark.regression
def test_new_assessment(logged_in_page):
    newassesment_page = AssessmentPage(logged_in_page) 
    newassesment_page.create_assessment() 

# Optimized
# @pytest.mark.end_to_end
# @pytest.mark.regression
# def test_new_assessment(page):
#     login_page = LoginPage(page)
#     login_page.load()

#     login_page.login(USERNAME, PASSWORD)
#     # Verify login success by checking for a specific element or title
#     assert page.title() == "Athlete Management System"  # Replace with actual title or verification
    
    
#     newassesment_page = AssessmentPage(page)
#     newassesment_page.create_assessment()
    