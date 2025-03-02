from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page, role=None):
        super().__init__(page)
        self.page = page
        self.role = role
        self.setup_locators()

    def setup_locators(self):
        self.menu_dashboard = self.page.locator("(//span[@class='link_name'][normalize-space()='Dashboard'])[1]")
        self.myaccount_click = self.page.locator('//img[@alt="Profile Image"]')
        self.logout_click = self.page.locator('//a[normalize-space()="Logout"]')

        if self.role == "Super Admin":
            self.menu_manage = self.page.locator('//*[text()="Manage"]')
            self.sub_menu_user = self.page.locator('//*[text()="User"]')
        elif self.role == "Assessor":
            self.menu_sports_fitness = self.page.locator("//span[normalize-space()='Sports Physical Fitness']")
        elif self.role == "Organization admin":
            self.menu_sports_identification = self.page.locator("//span[normalize-space()='Sports Talent Identification']")
        elif self.role == "Science staff":
            self.menu_sports_cognitive = self.page.locator("(//span[contains(text(),'Sports Cognitive')])[1]")

    def navigate_to(self, section):
        self.menu_dashboard.click()

        if self.role == "Super Admin":
            if section == "Manage User":
                self.menu_manage.click()
                self.sub_menu_user.click()
            else:
                raise Exception(f"Super Admin does not have '{section}' menu!")
        elif self.role == "Assessor":
            if section == "Sports Physical Fitness":
                self.menu_sports_fitness.click()
            else:
                raise Exception(f"Assessor does not have '{section}' menu!")
        elif self.role == "Organization admin":
            if section == "Sports Talent Identification":
                self.menu_sports_identification.click()
            else:
                raise Exception(f"Organization admin does not have '{section}' menu!")
        elif self.role == "Science staff":
            if section == "Sports Cognitive":
                self.menu_sports_cognitive.click()
            else:
                raise Exception(f"Science staff does not have '{section}' menu!")
        else:
            
            raise Exception(f"Unknown role '{self.role}', can't navigate to '{section}'!")
        

    def logout(self):
        self.menu_dashboard.click()
        self.myaccount_click.click()
        self.logout_click.click()
