import pytest
from pages.upload_roles.upload_new_coach import UploadNewCoachPage

@pytest.mark.regression 
def test_new_org_admin(logged_in_page): 
    upload_coach = UploadNewCoachPage(logged_in_page) 
    upload_coach.create_upload_new_coach()