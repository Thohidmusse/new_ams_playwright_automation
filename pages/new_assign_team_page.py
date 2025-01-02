
import logging
import random
from pages.base_page import BasePage
from utils.generate_data import randomn_short_indian_sports_team_names, randomn_organization_name, randomn_select_sports_name

# Configure logging
logging.basicConfig(level=logging.INFO)

class AssignTeamPage(BasePage): 
    def __init__(self, page):
        super().__init__(page)
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        self.menu_manage = page.locator('//*[text()="Manage"]')
        self.menu_team = page.locator('//a[normalize-space()="Team"]')
        self.new_teams_form_head = page.locator('//h4[normalize-space()="Teams"]') #assert form heading
        self.new_add_team_button = page.locator('//button[normalize-space()="Add Team"]')
        self.new_teams_form_head2 = page.locator('//h4[normalize-space()="Create Team"]') #assert form heading/
        self.new_select_organization = page.locator('//span[normalize-space()="Select Organization"]')
        self.new_team_name = page.locator('//input[@placeholder="Enter Team Name"]')
        self.new_select_sport = page.locator('//span[normalize-space()="Select Sport"]')
        self.new_team_submit_button = page.locator('//span[normalize-space()="Submit"]')
        self.new_team_success_message = page.locator('//div[@class="toaster"]//span[@class="msg-summary"][normalize-space()="Team added successfully."]')
        self.new_team_duplicate_message = page.locator('//div[@class="toaster"]//span[@class="msg-summary"][contains(text(),"Team Name already exists for the given organizatio")]')
        self.new_team_back_button = page.locator('//span[normalize-space()="Back"]')
        
        
    def Create_Assign_New_Team(self):
        sports_team_names = randomn_short_indian_sports_team_names() 
        sport_team_name = random.choice(sports_team_names)
        
        self.menu_dashboard.click()
        self.menu_manage.click()    
        self.menu_team.click()
        assert self.new_teams_form_head.text_content() == 'Teams'
        self.new_add_team_button.click()
        assert self.new_teams_form_head2.text_content() == 'Create Team'
        selected_organization = randomn_organization_name(self.page, '//ng-select[contains(@class, "ng-select") and @bindvalue="orgId"]')
        logging.info(f"Selected organization: {selected_organization}")
        
        self.new_team_name.fill(sport_team_name)
        logging.info(f"Sport team name: {sport_team_name}")
        
        selected_sport = randomn_select_sports_name(self.page, '//ng-select[contains(@class, "ng-select") and @bindvalue="sportId"]')
        logging.info(f"Selected sport: {selected_sport}")
        
        self.new_team_submit_button.click()
        assert self.new_team_success_message.text_content() == "Team added successfully."
        self.new_team_back_button.click()
        