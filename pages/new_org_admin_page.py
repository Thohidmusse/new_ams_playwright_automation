
import time
from pages.base_page import BasePage
from utils.config import load_config
from utils.generate_data import random_full_name_email, randomn_mobile_number, randomn_dob, randomn_address, randomn_religion
from utils.generate_data import randomn_gender, randomn_caste, randomn_relation

class NewOrgAdminPage(BasePage): 
    def __init__(self, page):
        super().__init__(page)
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        self.menu_manage = page.locator('//*[text()="Manage"]')
        self.menu_user = page.locator('//a[normalize-space()="User"]')
        self.create_new_button = page.locator('//button[@id="dropdownMenuButton1"]')
        self.new_org_admin_role = page.locator('//a[contains(@class, "dropdown-item") and text()="Org Admin"]') 
        self.new_org_admin_form_head = page.locator('//h2[normalize-space()="OrgAdmin Registration"]') #assert form heading
        self.new_org_admin_fullname = page.locator('//input[@name="usrFullName"]')
        self.new_org_admin_dob  = page.locator('//input[@name="usrDoB"]')
        self.new_org_admin_gender  = page.locator('//select[@name="usrGender"]')
        self.new_org_admin_religion  = page.locator('//input[@placeholder="Enter Religion"]')
        self.new_org_admin_caste  = page.locator('//select[@name="usrCaste"]')    
        self.new_org_admin_address  = page.locator('//input[@name="usrAddress"]')
        self.new_org_admin_phone  = page.locator('//input[@name="usrPhoneNo"]')  
        self.new_org_admin_email  = page.locator('//input[@name="usrEmail"]')  
        self.new_org_admin_password  = page.locator('//input[@name="usrPassword"]')
        self.new_org_admin_confirm_password  = page.locator('//input[@name="confirmPassword"]')
        self.new_org_admin_ecname  = page.locator('//input[@name="usrECName"]')
        self.new_org_admin_ecrelation  = page.locator('//input[@name="usrECRelationship"]')
        self.new_org_admin_ecphone  = page.locator('//input[@name="usrECPhoneNo"]')   
        self.new_org_admin_organization  = page.locator('//select[@name="usrOrganization"]')
        self.new_org_admin_submit = page.locator('//button[@class="btn-submit"]')
        self.new_org_admin_back = page.locator('//i[@class="fa fa-arrow-left"]')
        self.register_details_form = page.locator('//select[@id="statusFilter"]')
       
    def create_new_org_admin(self):
        config = load_config() # Load configuration 
        password = config['PASSWORD']
        full_name, email  = random_full_name_email()
        mobile_number = randomn_mobile_number()
        date_of_birth = randomn_dob()
        full_address = randomn_address()
        religion = randomn_religion()
        relation = randomn_relation()
        
        self.menu_dashboard.click()
        self.menu_manage.click()
        self.menu_user.click()
        self.create_new_button.click()
        self.new_org_admin_role.click()
        assert self.new_org_admin_form_head.text_content() == 'OrgAdmin Registration'
        self.new_org_admin_fullname.fill(full_name)
        self.new_org_admin_dob.fill(date_of_birth)
        randomn_gender(self.page, '//select[@name="usrGender"]')
        # self.new_org_admin_gender.select_option(label='Female')
        self.new_org_admin_religion.fill(religion)
        time.sleep(2)
        randomn_caste(self.page, '//select[@name="usrCaste"]')
        # self.new_org_admin_caste.select_option(label='ST')
        self.new_org_admin_address.fill(full_address)
        self.new_org_admin_phone.fill(mobile_number)
        self.new_org_admin_email.fill(email)
        self.new_org_admin_password.fill(password)
        self.new_org_admin_confirm_password.fill(password)
        self.new_org_admin_ecname.fill(full_name)
        self.new_org_admin_ecrelation.fill(relation)
        self.new_org_admin_ecphone.fill(mobile_number) #fill('9876543210')
        self.new_org_admin_organization.select_option(label='DYES')
        self.new_org_admin_submit.click()
        self.new_org_admin_back.click()
        self.register_details_form.select_option(label='Accepted')



