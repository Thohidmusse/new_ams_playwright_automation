import pytest
from pages.new_team_page import NewTeamPage
# from pages.login_page import LoginPage
# from utils.config import USERNAME, PASSWORD

@pytest.mark.regression 
def test_new_team(logged_in_page): 
    newteam_page = NewTeamPage(logged_in_page) 
    newteam_page.Create_New_Team() 