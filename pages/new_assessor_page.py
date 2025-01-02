
import time
from pages.base_page import BasePage
from utils.config import load_config 
from utils.generate_data import random_full_name_email, randomn_mobile_number, randomn_dob, randomn_address, randomn_religion
from utils.generate_data import randomn_gender, randomn_caste, randomn_relation

class NewAssessorPage(BasePage): 
    def __init__(self, page):
        super().__init__(page)
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        self.menu_manage = page.locator('//*[text()="Manage"]')
        self.menu_user = page.locator('//a[normalize-space()="User"]')
        self.create_new_button = page.locator('//button[@id="dropdownMenuButton1"]')
        self.new_assessor_role = page.locator('//a[contains(@class, "dropdown-item") and text()="Assessor"]') 
        self.new_assessor_form_head = page.locator('//h2[normalize-space()="Assessor Registration"]') #assert form heading
        self.new_assessor_fullname = page.locator('//input[@name="usrFullName"]')
        self.new_assessor_dob  = page.locator('//input[@name="usrDoB"]')
        self.new_assessor_gender  = page.locator('//select[@name="usrGender"]')
        self.new_assessor_religion  = page.locator('//input[@placeholder="Enter Religion"]')
        self.new_assessor_caste  = page.locator('//select[@name="usrCaste"]')    
        self.new_assessor_address  = page.locator('//input[@name="usrAddress"]')
        self.new_assessor_phone  = page.locator('//input[@name="usrPhoneNo"]')  
        self.new_assessor_email  = page.locator('//input[@name="usrEmail"]')  
        self.new_assessor_password  = page.locator('//input[@name="usrPassword"]')
        self.new_assessor_confirm_password  = page.locator('//input[@name="confirmPassword"]')
        self.new_assessor_ecname  = page.locator('//input[@name="usrECName"]')
        self.new_assessor_ecrelation  = page.locator('//input[@name="usrECRelationship"]')
        self.new_assessor_ecphone  = page.locator('//input[@name="usrECPhoneNo"]')
        self.new_assessor_organization  = page.locator('//select[@name="usrOrganization"]') 
        self.new_assessor_submit = page.locator('//button[@class="btn-submit"]')
        self.new_assessor_back = page.locator('//i[@class="fa fa-arrow-left"]')
        self.register_details_form = page.locator('//select[@id="statusFilter"]')
       
    def create_new_assessor(self):
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
        self.new_assessor_role.click()
        assert self.new_assessor_form_head.text_content() == 'Assessor Registration'
        self.new_assessor_fullname.fill(full_name)
        self.new_assessor_dob.fill(date_of_birth)
        randomn_gender(self.page, '//select[@name="usrGender"]')
        # self.new_assessor_gender.select_option(label='Female')
        self.new_assessor_religion.fill(religion)
        randomn_caste(self.page, '//select[@name="usrCaste"]')
        # self.new_assessor_caste.select_option(label='ST')
        self.new_assessor_address.fill(full_address)
        self.new_assessor_phone.fill(mobile_number)
        self.new_assessor_email.fill(email)
        self.new_assessor_password.fill(password)
        self.new_assessor_confirm_password.fill(password)
        self.new_assessor_ecname.fill(full_name)
        self.new_assessor_ecrelation.fill(relation)
        self.new_assessor_ecphone.fill(mobile_number)
        self.new_assessor_organization.select_option(label='DYES')
        time.sleep(2)
        self.new_assessor_submit.click()
        time.sleep(2)
        self.new_assessor_back.click()
        #self.register_details_form.select_option(label='Accepted')



