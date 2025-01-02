import pytest
from pages.new_organization_page import NewOrganizationPage
# from pages.login_page import LoginPage
# from utils.config import USERNAME, PASSWORD

@pytest.mark.regression 
def test_new_organization(logged_in_page):
    neworganization_page = NewOrganizationPage(logged_in_page)
    org_name = neworganization_page.create_new_organization()
    
# # Find the created organization in the table 
#     found_row = NewOrganizationPage.find_organization(org_name) 
#     assert found_row is not None, f"Organization '{org_name}' not found in the table" 
#     print(f"Organization '{org_name}' found in the table")