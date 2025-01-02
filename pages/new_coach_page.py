
import time
from pages.base_page import BasePage
from utils.config import load_config
from utils.generate_data import random_full_name_email, randomn_mobile_number, randomn_dob, randomn_address, randomn_religion
from utils.generate_data import randomn_gender, randomn_caste, randomn_relation, randomn_organization_name, randomn_select_sports_name
from utils.generate_data import select_random_coach_sport
class NewCoachPage(BasePage): 
    def __init__(self, page):
        super().__init__(page)
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        self.menu_manage = page.locator('//*[text()="Manage"]')
        self.menu_user = page.locator('//a[normalize-space()="User"]')
        self.create_new_button = page.locator('//button[@id="dropdownMenuButton1"]')
        self.new_coach_role = page.locator('//a[contains(@class, "dropdown-item") and text()="Coach"]') 
        self.new_coach_form_head = page.locator('//h2[normalize-space()="Coach Registration"]') #assert form heading
        self.new_coach_fullname = page.locator('//input[@name="usrFullName"]')
        self.new_coach_dob  = page.locator('//input[@name="usrDoB"]')
        self.new_coach_gender  = page.locator('//select[@name="usrGender"]')
        self.new_coach_religion  = page.locator('//input[@placeholder="Enter Religion"]')
        self.new_coach_caste  = page.locator('//select[@name="usrCaste"]')    
        self.new_coach_address  = page.locator('//input[@name="usrAddress"]')
        self.new_coach_phone  = page.locator('//input[@name="usrPhoneNo"]')  
        self.new_coach_email  = page.locator('//input[@name="usrEmail"]')  
        self.new_coach_password  = page.locator('//input[@name="usrPassword"]')
        self.new_coach_confirm_password  = page.locator('//input[@name="confirmPassword"]')
        self.new_coach_ecname  = page.locator('//input[@name="usrECName"]')
        self.new_coach_ecrelation  = page.locator('//input[@name="usrECRelationship"]')
        self.new_coach_ecphone  = page.locator('//input[@name="usrECPhoneNo"]')
        self.new_coach_sport  = page.locator('//select[@name="usrSport"]')    
        self.new_coach_organization  = page.locator('//select[@name="usrOrganization"]')
        self.new_coach_submit = page.locator('//button[@class="btn-submit"]')
        self.new_coach_back = page.locator('//i[@class="fa fa-arrow-left"]')
        self.register_details_form = page.locator('//select[@id="statusFilter"]')
       
    def create_new_coach(self):
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
        self.new_coach_role.click()
        assert self.new_coach_form_head.text_content() == 'Coach Registration'
        self.new_coach_fullname.fill(full_name)
        self.new_coach_dob.fill(date_of_birth)
        randomn_gender(self.page, '//select[@name="usrGender"]')
        self.new_coach_religion.fill(religion)
        time.sleep(2)
        randomn_caste(self.page, '//select[@name="usrCaste"]')
        self.new_coach_address.fill(full_address)
        self.new_coach_phone.fill(mobile_number)
        self.new_coach_email.fill(email)
        self.new_coach_password.fill(password)
        self.new_coach_confirm_password.fill(password)
        self.new_coach_ecname.fill(full_name)
        self.new_coach_ecrelation.fill(relation)
        self.new_coach_ecphone.fill(mobile_number)
        select_random_coach_sport(self.page, 'select[name="usrSport"]')
        # self.new_coach_sport.select_option(label='Swimming')
        randomn_organization_name(self.page, '//ng-select[contains(@class, "ng-select") and @bindvalue="orgId"]')
        # self.new_coach_organization.select_option(label='DYES')
        self.new_coach_submit.click()
        self.new_coach_back.click() 
        #self.register_details_form.select_option(label='Accepted')



