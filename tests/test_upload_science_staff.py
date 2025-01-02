import pytest
from pages.upload_roles.upload_new_science_staff import UploadNewScienceStaffPage

@pytest.mark.regression 
def test_new_science_staff(logged_in_page): 
    upload_science_staff = UploadNewScienceStaffPage(logged_in_page) 
    upload_science_staff.create_upload_new_science_staff()