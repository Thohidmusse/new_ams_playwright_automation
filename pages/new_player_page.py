
import time

from pages.base_page import BasePage
from utils.config import load_config 
from utils.generate_data import random_full_name_email, randomn_mobile_number, randomn_dob, randomn_address, randomn_religion
from utils.generate_data import randomn_gender, randomn_caste,randomn_relation, randomn_weight, randomn_height, randomn_player_class
from utils.generate_data import randomn_allergies, randomn_current_medications,randomn_previous_injuries
from utils.generate_data import randomn_chronic_conditions,randomn_surgeries,randomn_family_medical_history,randomn_sleep_patterns
from utils.generate_data import randomn_diet,randomn_hydration,randomn_stress_levels,randomn_primary_sport,randomn_position_role
from utils.generate_data import randomn_secondary_sport,randomn_event,randomn_sports_category,randomn_coach
from utils.generate_data import randomn_frequency_per_week,randomn_duration_per_session,randomn_participation
from utils.generate_data import randomn_medal_won,randomn_short_term_goals,randomn_long_term_goals

class NewPlayerPage(BasePage): 
    def __init__(self, page):
        super().__init__(page)        
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        self.menu_manage = page.locator('//*[text()="Manage"]')
        self.menu_user = page.locator('//a[normalize-space()="User"]')
        self.create_new_button = page.locator('//button[@id="dropdownMenuButton1"]')
        self.new_player_role = page.locator('//a[contains(@class, "dropdown-item") and text()="Player"]') 
        self.new_player_form_head = page.locator('//h2[normalize-space()="Player Registration"]') #assert form heading

        # form-1 elements
        self.new_player_fullname = page.locator('//input[@name="usrFullName"]')
        self.new_player_dob  = page.locator('//input[@name="usrDoB"]')
        self.new_player_gender  = page.locator('//select[@name="usrGender"]')
        self.new_player_height  = page.locator('//input[@name="usrHeight"]') 
        self.new_player_weight  = page.locator('//input[@name="usrWeight"]') 
        self.new_player_religion  = page.locator('//input[@name="usrReligion"]')
        self.new_player_caste  = page.locator('//select[@name="usrCaste"]')    
        self.new_player_address  = page.locator('//input[@name="usrAddress"]')
        self.new_player_phone  = page.locator('//input[@name="usrPhoneNo"]')  
        self.new_player_email  = page.locator('//input[@name="usrEmail"]')  
        self.new_player_password  = page.locator('//input[@name="usrPassword"]')
        self.new_player_confirm_password  = page.locator('//input[@name="confirmPassword"]')
        self.new_player_ecname  = page.locator('//input[@name="usrECName"]')
        self.new_player_ecrelation  = page.locator('//input[@name="usrECRelationship"]')
        self.new_player_ecphone  = page.locator('//input[@name="usrECPhoneNo"]')
        self.new_player_organization  = page.locator('//select[@name="usrOrganization"]')
        self.new_player_class  = page.locator('//select[@name="usrClass"]') 
        self.new_player_next_button_form1 = page.locator('//button[normalize-space()="Next Step"]')
                                                         
        # form-2 elements
        self.new_player_allergies = page.get_by_placeholder('Enter Allergies')
        self.new_player_current_medications = page.get_by_placeholder('Enter Current Medications')
        self.new_player_previous_injuries = page.get_by_placeholder('Enter Previous Injuries')
        self.new_player_chronic_conditions = page.get_by_placeholder('Enter Chronic Conditions')
        self.new_player_surgeries = page.get_by_placeholder('Enter Surgeries')
        self.new_player_family_medical_history = page.get_by_placeholder('Enter Family Medical History')
        self.new_player_sleep_patterns = page.get_by_placeholder('Enter Sleep Patterns')
        self.new_player_diet = page.get_by_placeholder('Enter Diet')
        self.new_player_hydration = page.get_by_placeholder('Enter Hydration')
        self.new_player_stress_levels = page.get_by_placeholder('Enter Stress Levels')
        self.new_player_next_button_form2 = page.get_by_role('button', name='Next Step')
        
        # form-3 elements
        self.new_player_primary_sport = page.get_by_placeholder('Enter Primary Sport')
        self.new_player_position_role = page.get_by_placeholder('Enter Position/Role')
        self.new_player_secondary_sport = page.get_by_placeholder('Enter Secondary Sport')
        self.new_player_event = page.get_by_placeholder('Enter Event')
        self.new_player_sports_category = page.get_by_placeholder('Sports Category')
        self.new_player_coach = page.locator('//select[@name="asiCoach"]') 
        self.new_player_frequency_per_week = page.get_by_placeholder('Enter Frequency Per Week')
        self.new_player_duration_per_session = page.get_by_placeholder('Enter Duration Per Session')
        self.new_player_participation = page.locator('//input[@name="asiCompetitionLevel"]')
        self.new_player_medal_won = page.locator('//select[@name="asiCareerHighlights"]')
        self.new_player_short_term_goals = page.get_by_placeholder('Enter Short-term Goals')
        self.new_player_long_term_goals = page.get_by_placeholder('Enter Long-term Goals')
        #page.get_by_role('button', name='Submit')
        
        # self.new_player_ = page.getByRole('button', { name: 'Back' })
        # self.new_player_ = page.getByRole('button', { name: 'Back' })
        
    def scroll_to_element(self, locator): 
        locator.scroll_into_view_if_needed()
       
    def create_new_player(self): 
        config = load_config() # Load configuration 
        password = config['PASSWORD'] 
        full_name, email  = random_full_name_email()
        mobile_number = randomn_mobile_number()
        date_of_birth = randomn_dob()
        full_address = randomn_address()
        relation = randomn_relation()
        religion = randomn_religion()
        height = randomn_height()
        weight = randomn_weight()
        allergies = randomn_allergies()
        medications = randomn_current_medications()
        injuries = randomn_previous_injuries()
        chronic = randomn_chronic_conditions()
        surgeries = randomn_surgeries()
        medical_history = randomn_family_medical_history()
        sleep_patters = randomn_sleep_patterns()
        diet = randomn_diet()
        hydration = randomn_hydration()
        stress_levels = randomn_stress_levels()
        primary_sport = randomn_primary_sport()
        position = randomn_position_role()
        secondary_sport = randomn_secondary_sport()
        event = randomn_event()
        sports_category = randomn_sports_category()
        frequency = randomn_frequency_per_week()
        session_duration = randomn_duration_per_session()
        participation = randomn_participation()
        # medal_won = randomn_medal_won()
        short_term_goals= randomn_short_term_goals()
        long_term_goals = randomn_long_term_goals()
                      
        self.menu_dashboard.click()
        self.menu_manage.click()
        self.menu_user.click()
        self.create_new_button.click()
        self.new_player_role.click()
        assert self.new_player_form_head.text_content() == 'Player Registration'
        
        # form-1 elements actions
        self.new_player_fullname.fill(full_name)
        self.new_player_dob.fill(date_of_birth)
        self.new_player_gender.wait_for(state='visible')
        time.sleep(2)
        self.new_player_gender.click()
        randomn_gender(self.page, '//select[@name="usrGender"]')
        self.new_player_height.fill(height) 
        self.new_player_weight.fill(weight)
        self.new_player_religion.fill(religion)
        self.new_player_caste.click()
        self.new_player_caste.wait_for(state='visible')
        time.sleep(2) 
        randomn_caste(self.page, '//select[@name="usrCaste"]')
        self.new_player_address.fill(full_address)
        self.new_player_phone.fill(mobile_number)
        self.new_player_email.fill(email)
        self.new_player_password.fill(password) # Use password from config
        self.new_player_confirm_password.fill(password) # Use password from config
        self.new_player_ecname.fill(full_name)
        self.new_player_ecrelation.fill(relation)
        self.new_player_ecphone.fill(mobile_number)
        self.new_player_organization.select_option(label='DYES')
        time.sleep(1)
        self.new_player_class.click()
        self.new_player_class.wait_for(state='visible')
        self.scroll_to_element(self.new_player_class) 
        time.sleep(1)
        randomn_player_class(self.page, '//select[@name="usrClass"]')
        self.new_player_next_button_form1.click()
        
        # form-2 elements actions
        self.new_player_allergies.fill(allergies)
        self.new_player_current_medications.fill(medications)
        self.new_player_previous_injuries.fill(injuries)
        self.new_player_chronic_conditions.fill(chronic)
        self.new_player_surgeries.fill(surgeries)
        self.new_player_family_medical_history.fill(medical_history)
        self.new_player_sleep_patterns.fill(sleep_patters)
        self.new_player_diet.fill(diet)
        self.new_player_hydration.fill(hydration)
        self.new_player_stress_levels.fill(stress_levels)
        self.new_player_next_button_form2.click()
        
        # form-3 elements actions
        self.new_player_primary_sport.fill(primary_sport)
        self.new_player_position_role.fill(position)
        self.new_player_secondary_sport.fill(secondary_sport)
        self.new_player_event.fill(event)
        self.new_player_sports_category.fill(sports_category)
        self.new_player_coach.wait_for(state='visible')
        # self.scroll_to_element(self.new_player_coach) 
        # randomn_coach(self.page, '//select[@name="asiCoach"][1]')
        self.new_player_frequency_per_week.fill(frequency)
        self.new_player_duration_per_session.fill(session_duration)
        self.new_player_participation.fill(participation)
        self.new_player_medal_won.wait_for(state='visible')
        randomn_medal_won(self.page, '//select[@name="asiCareerHighlights"]')
        self.new_player_short_term_goals.fill(short_term_goals)
        self.new_player_long_term_goals.fill(long_term_goals)
        