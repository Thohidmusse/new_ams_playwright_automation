from pages.base_page import BasePage

class DashboardPage(BasePage):
    def init(self, page):
        super().init(page)
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        self.logo_name = page.locator('//span[@class="logo-name"]')
        self.role_name = page.locator('//span[@class="role-description"]')
        