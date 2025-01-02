import pytest
from pages.upload_roles.upload_new_org_admin import UploadNewOrgAdminPage

@pytest.mark.regression 
def test_new_org_admin(logged_in_page): 
    upload_org = UploadNewOrgAdminPage(logged_in_page) 
    upload_org.create_upload_new_org_admin()