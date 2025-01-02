import pytest
from pages.upload_roles.upload_new_player import UploadNewPlayerPage

@pytest.mark.regression 
def test_new_player(logged_in_page): 
    upload_player = UploadNewPlayerPage(logged_in_page) 
    upload_player.create_upload_new_player()