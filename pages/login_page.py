from pages.base_page import BasePage
# from utils.config import BASE_URL

class LoginPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url
        self.username_field = page.locator('//*[@id="email"]')
        self.password_field = page.locator('//*[@id="password"]')
        self.login_button = page.locator('//*[@type="submit"]')

    def login(self, username, password):
        self.page.goto(self.base_url, wait_until="load")
        self.username_field.wait_for(state="visible", timeout=30000)
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

# class LoginPage(BasePage):
#     def __init__(self, page):
#         super().__init__(page)
#         self.username_field = page.locator('//*[@id="email"]')
#         self.password_field = page.locator('//*[@id="password"]')
#         self.login_button = page.locator('//*[@type="submit"]')

#     def load(self):
#         self.visit(BASE_URL)

#     def login(self, username, password):
#         self.username_field.fill(username)
#         self.password_field.fill(password)
#         self.login_button.click()
