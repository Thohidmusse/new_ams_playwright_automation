import pytest
from pages.new_org_player_page import NewPlayerPage
# from pages.login_page import LoginPage
# from utils.config import USERNAME, PASSWORD
 
@pytest.mark.regression 
def test_new_player(logged_in_page):
    newplayer_page = NewPlayerPage(logged_in_page) 
    newplayer_page.create_new_player() 
 

# @pytest.mark.regression 
# def test_new_player(page):
#     login_page = LoginPage(page)
#     login_page.load()
    
#     login_page.login(USERNAME, PASSWORD)
#     # Verify login success by checking for a specific element or title 
#     assert page.title() == "Athlete Management System"  # Replace with actual title or verification
    
    
#     newplayer_page = NewPlayerPage(page)
#     newplayer_page.create_new_player()
    