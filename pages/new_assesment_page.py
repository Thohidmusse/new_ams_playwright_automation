
from pages.base_page import BasePage
from utils.generate_data import randomn_current_date
from utils.generate_data import randomn_assessment_name_description, randomn_organization_name

class AssessmentPage(BasePage): 
    def __init__(self, page):
        super().__init__(page)
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        self.menu_manage = page.locator('//*[text()="Manage"]')
        self.sub_menu_assessment = page.locator('//a[normalize-space()="Assessment"]')
        self.assessment_page_heading = page.locator('//h4[contains(text(), "Assessment")]')  #assert it
        self.assessment_button = page.locator('//button[normalize-space()="Add Assessment"]')
        self.assessment_heading = page.locator('//header[normalize-space()="Assessment"]')  #assert it
        self.assessment_name = page.locator('//input[@placeholder="Enter Assessment Name"]')
        self.assessment_description = page.locator('//textarea[@name="assessmentDescription"]')
        self.assessment_date = page.locator('//input[@placeholder="Enter Assessment Date"]')
        self.assessment_org = page.locator('//select[@name="usrOrganization"]')
        self.assessment_team = page.locator('//select[@name="Team"]')
        self.assessment_category = page.locator('//select[@name="Cat"]')
        self.assessment_type = page.locator('//select[@name="selectedAssessment"]')
        self.assessment_assessor = page.locator('//select[@name="selectedAssessor"]')
        self.assessment_table_checkbox = page.locator('//div[@class="ag-labeled ag-label-align-right ag-checkbox ag-input-field ag-header-select-all" and @role="presentation"]//input[@class="ag-input-field-input ag-checkbox-input"]')
        self.assessment_submit = page.locator('//button[@type="submit"]')
        self.assessment_submit_success_message = page.locator('//span[contains(@class, "msg-summary") and text()="Form submitted successfully"]')
        self.assessment_back = page.locator('//button[normalize-space()="Back"]')


    def create_assessment(self):
        assessment_name, assessment_description = randomn_assessment_name_description()
        current_date = randomn_current_date()
        self.menu_dashboard.click()
        self.menu_manage.click()
        self.sub_menu_assessment.click()
        assert self.assessment_page_heading.text_content() == "Assessment"
        self.assessment_button.click()
        self.assessment_name.fill(assessment_name)   # (f"{full_name} sports Assessment")
        self.assessment_description.fill(assessment_description)
        self.assessment_date.fill(current_date)
        self.assessment_org.select_option(label='DYES')
        #selected_organization = randomn_organization_name(self.page, '//select[@name="usrOrganization"]')
        self.assessment_team.wait_for(state='visible', timeout=10000)
        self.page.wait_for_selector('//select[@name="Team"]', state='visible', timeout=10000)
        self.assessment_team.select_option(label='Titans')
        self.assessment_category.select_option(label='Sports Talent Identification Assessment')
        self.assessment_type.select_option(label='Cognitive')
        self.assessment_assessor.select_option(label='Assessor')
        self.assessment_table_checkbox.wait_for(state='visible', timeout=60000)
        self.assessment_table_checkbox.check()
        #self.assessment_submit.click()
        #assert self.assessment_submit_success_message.text_content() == "Form submitted successfully"
        self.assessment_back.click()
        assert self.assessment_page_heading.text_content() == "Assessment"
        