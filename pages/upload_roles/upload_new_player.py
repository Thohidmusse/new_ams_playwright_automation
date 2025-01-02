import time
from pages.base_page import BasePage
from utils.file_upload import upload_file

class UploadNewPlayerPage(BasePage): 
    def __init__(self, page):
        super().__init__(page)
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        self.menu_manage = page.locator('//*[text()="Manage"]')
        self.menu_user = page.locator('//a[normalize-space()="User"]') 
        self.upload_button = page.locator('//button[contains(text(),"Upload")]')
        self.popup_upload_label = page.locator('//h5[@id="fileUploadModalLabel"]')  #assert popup heading
        self.role_dropdwon = page.locator('//ng-select[@placeholder="Select Role"]//div[@role="combobox"]')
        self.file_input_locator = 'input[type="file"]'
        self.file_upload_button = page.locator('//span[@class="btnText"]')
                    
    def create_upload_new_player(self):
        self.menu_dashboard.click()
        self.menu_manage.click()
        self.menu_user.click()
        self.upload_button.click()
        assert self.popup_upload_label.text_content() == 'Upload File'
        self.role_dropdwon.click()
        # Select the "Org Admin" role 
        org_admin_option = self.page.locator('.ng-option', has_text='Player') 
        org_admin_option.click() 
        print("Selected Player role")
        # Path to the Excel file in the data folder 
        excel_filename = 'data/PlayerRegister_Template.xlsx'
        # Upload the Excel file 
        # file_input = self.page.locator(self.file_input_locator)
        # file_input.set_input_files(excel_filename)
        upload_file(self.page, self.file_input_locator, excel_filename) 
        print(f"Uploaded file: {excel_filename}")
        self.file_upload_button.click()   