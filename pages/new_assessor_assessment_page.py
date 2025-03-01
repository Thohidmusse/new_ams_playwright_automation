import time
import random
from datetime import datetime, timedelta
from pages.base_page import BasePage

class AssessorAssessmentPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.menu_dashboard = page.locator("((//span[normalize-space()='Dashboard'])[1]")  

        self.menu_sports_physical_fitness = page.locator('//a[normalize-space()="Sports Physical Fitness"]')
        self.google_assessment_section = page.locator("//div[normalize-space()='google assessment']")
        self.google_assessment_view_icon = self.google_assessment_section.locator("//following-sibling::div//i[@class='fa fa-eye']")
        
        

        self.player = self.page.locator("//div[normalize-space()='60']")

      
        self.edit_icon = page.locator(' //body[1]/app-root[1]/app-sidenavbar[1]/section[1]/main[1]/app-physicalfitness-assessment-list[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ag-grid-angular[1]/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/button[2]/i[1]')

        self.test_taken_date = page.locator("(//input[@name='updateDate'])[1]")      
        self.single_leg_balance_left_eye_open = page.locator("(//input[@placeholder='Enter Single Leg Balance Left Eye Open'])[1]")
        self.single_leg_balance_left_eye_close = page.locator("(//input[@placeholder='Enter Single Leg Balance Left Eye Close'])[1]")
        self.y_balance_test_1 = page.locator("(//input[@placeholder='Enter Y-Balance Test'])[1]")
        self.y_balance_test_2 = page.locator("(//input[@placeholder='Enter Y-Balance Test-2'])[1]")
        self.submit_button = page.locator('//button[@type="submit"]')

    def login_as_assessor(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def generate_random_date(self):
        today = datetime.today()
        random_days = random.randint(-30, 0)  # Random date within the last 30 days
        random_date = today + timedelta(days=random_days)
        return random_date.strftime("%Y-%m-%d")

    def random_number(self, min_value=5, max_value=30):
        return str(random.randint(min_value, max_value))

    def perform_assessment(self):
        self.menu_sports_physical_fitness.click()
        time.sleep(2)
        self.google_assessment_view_icon.click()
        time.sleep(2)
        
        self.player.click
        time.sleep(1)

        self.edit_icon.click()
        time.sleep(2)

        # Fill with random data
        self.test_taken_date.fill(self.generate_random_date())
        self.single_leg_balance_left_eye_open.fill(self.random_number())
        self.single_leg_balance_left_eye_close.fill(self.random_number())
        self.y_balance_test_1.fill(self.random_number(80, 120))
        self.y_balance_test_2.fill(self.random_number(80, 120))

        self.submit_button.click()
        time.sleep(2)

        print("Assessment filled and submitted successfully with random data!")
