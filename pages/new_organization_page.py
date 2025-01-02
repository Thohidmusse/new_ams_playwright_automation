import time
import random
from pages.base_page import BasePage
from utils.file_upload import upload_image
from utils.generate_data import randomn_sports_organization_names

class NewOrganizationPage(BasePage): 
    def __init__(self, page):
        super().__init__(page)
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        self.menu_manage = page.locator('//*[text()="Manage"]')
        self.menu_organization = page.locator('//a[normalize-space()="Organization"]')
        self.new_organization_form_head = page.locator('//h4[normalize-space()="Organization Management"]') #assert form heading
        self.new_organization_create_button = page.locator('//button[normalize-space()="Create Organization"]')
        self.new_organization_form_head2 = page.locator('//h4[normalize-space()="Create Organization"]') #assert form heading
        self.new_organization_Name = page.locator('//input[@name="orgName"]')   
        self.new_organization_logo = page.locator('//input[type="file"]')
        self.new_organiation_submit = page.locator('//span[normalize-space()="Submit"]')
        self.new_organization_table = page.locator('//div[@class="ag-root-wrapper ag-layout-normal ag-ltr"]')
        
    def create_new_organization(self):
        organization_names = randomn_sports_organization_names() 
        organization_name = random.choice(organization_names)
        
        self.menu_dashboard.click()
        self.menu_manage.click()    
        self.menu_organization.click()
        assert self.new_organization_form_head.text_content() == 'Organization Management'
        self.new_organization_create_button.click()
        assert self.new_organization_form_head2.text_content() == ' Create Organization '
        self.new_organization_Name.fill(organization_name)
        
        # Upload the image 
        image_path = 'data/org_logo.png' 
        upload_image(self.page,'input[type="file"]', image_path) 
        
        self.new_organiation_submit.click()  
        assert self.new_organization_form_head.text_content() == 'Organization Management' 
        
        return organization_name # Return the organization name for validation
    
    def find_organization(self, organization_name): 
        rows = self.new_organization_table 
        row_count = rows.count() 
        for i in range(row_count): 
            row = rows.nth(i) 
            name_cell = row.locator('td').nth(1) # Assuming the second column is the Org Name 
            if name_cell.text_content() == organization_name: 
                return row 
            return None # Return None if the organization is not found
        
        