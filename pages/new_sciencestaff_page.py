
import random
import time
from pages.base_page import BasePage
from utils.config import load_config
from utils.generate_data import random_full_name_email, randomn_mobile_number, randomn_dob, randomn_address, randomn_religion
from utils.generate_data import randomn_gender, randomn_caste, randomn_sciencestaff_supportstaff,randomn_relation

class ScienceStaffPage(BasePage): 
    def __init__(self, page):
        super().__init__(page)
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        self.menu_manage = page.locator('//*[text()="Manage"]')
        self.menu_user = page.locator('//a[normalize-space()="User"]')
        self.create_new_button = page.locator('//button[@id="dropdownMenuButton1"]')
        self.new_sciencestaff_role = page.locator('//a[contains(@class, "dropdown-item") and text()="Science Staff"]') 
        self.new_sciencestaff_form_head = page.locator('//h2[normalize-space()="Science Staff Registration"]') #assert form heading
        self.new_sciencestaff_fullname = page.locator('//input[@name="usrFullName"]')
        self.new_sciencestaff_dob  = page.locator('//input[@name="usrDoB"]')
        self.new_sciencestaff_gender  = page.locator('//select[@name="usrGender"]')  
        self.new_sciencestaff_religion  = page.locator('//input[@placeholder="Enter Religion"]')
        self.new_sciencestaff_caste  = page.locator('//select[@name="usrCaste"]')   
        self.new_sciencestaff_address  = page.locator('//input[@name="usrAddress"]')
        self.new_sciencestaff_phone  = page.locator('//input[@name="usrPhoneNo"]') 
        self.new_sciencestaff_email  = page.locator('//input[@name="usrEmail"]')   
        self.new_sciencestaff_password  = page.locator('//input[@name="usrPassword"]')
        self.new_sciencestaff_confirm_password  = page.locator('//input[@name="confirmPassword"]')
        self.new_sciencestaff_ecname  = page.locator('//input[@name="usrECName"]')
        self.new_sciencestaff_ecrelation  = page.locator('//input[@name="usrECRelationship"]')
        self.new_sciencestaff_ecphone  = page.locator('//input[@name="usrECPhoneNo"]')
        self.new_sciencestaff_supportstaff = page.locator('//select[@name="usrSupport"]')
        self.new_sciencestaff_submit = page.locator('//button[@class="btn-submit"]')
        self.new_sciencestaff_back = page.locator('//i[@class="fa fa-arrow-left"]')
        self.register_details_form = page.locator('//select[@id="statusFilter"]')
            
    def create_new_sciencestaff(self):
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
        self.new_sciencestaff_role.click()
        assert self.new_sciencestaff_form_head.text_content() == 'Science Staff Registration'
        self.new_sciencestaff_fullname.fill(full_name)
        self.new_sciencestaff_dob.fill(date_of_birth)
        randomn_gender(self.page, '//select[@name="usrGender"]')
        # self.new_sciencestaff_gender.select_option(label='Female')
        self.new_sciencestaff_religion.fill(religion)
        time.sleep(2)
        randomn_caste(self.page, '//select[@name="usrCaste"]')
        # self.new_sciencestaff_caste.select_option(label='ST')
        self.new_sciencestaff_address.fill(full_address) 
        self.new_sciencestaff_phone.fill(mobile_number)
        self.new_sciencestaff_email.fill(email)
        self.new_sciencestaff_password.fill(password)
        self.new_sciencestaff_confirm_password.fill(password)
        self.new_sciencestaff_ecname.fill(full_name)
        self.new_sciencestaff_ecrelation.fill(relation)
        self.new_sciencestaff_ecphone.fill(mobile_number)
        time.sleep(2)
        randomn_sciencestaff_supportstaff(self.page, '//select[@name="usrSupport"]')
        # self.new_sciencestaff_supportstaff.select_option(label='Cognitive')
        self.new_sciencestaff_submit.click()
        self.new_sciencestaff_back.click()
        #self.register_details_form.select_option(label='Accepted')




