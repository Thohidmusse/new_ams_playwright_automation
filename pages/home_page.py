import time
from pages.base_page import BasePage

class HomePage(BasePage): 
    def __init__(self, page):
        super().__init__(page)
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        #self.menu_manage = page.locator('//*[text()="Manage"]')
        #self.sub_menu_user = page.locator('//*[text()="User"]') 
        self.myaccount_click = page.locator('//img[@alt="Profile Image"]')
        self.logout_click = page.locator('//a[normalize-space()="Logout"]')


       

    def menu(self):
        self.menu_dashboard.click()
        self.menu_manage.click()
        self.sub_menu_user.click()

    def logout(self):
        self.menu_dashboard.click()
        self.myaccount_click.click()
        #time.sleep(5)
        self.logout_click.click()