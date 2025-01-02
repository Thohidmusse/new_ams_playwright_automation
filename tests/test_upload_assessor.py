import pytest
from pages.upload_roles.upload_new_accessor import UploadNewAssessorPage

@pytest.mark.regression 
def test_upload_new_assessor(logged_in_page): 
    upload_assessor = UploadNewAssessorPage(logged_in_page) 
    upload_assessor.create_upload_new_Assessor()