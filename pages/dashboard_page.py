from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.menu_dashboard = page.locator('//*[text()="Dashboard"]')
        self.menu_sports_talent = page.locator('//span[normalize-space()="Sports Talent Identification"]')
        self.menu_school_health = page.locator('//span[normalize-space()="School Health & Fitness"]')
        self.menu_sports_physical = page.locator('//span[normalize-space()="Sports Physical Fitness"]')
        self.menu_sports_nutritional = page.locator('//span[normalize-space()="Sports Nutritional"]')
        self.menu_sports_nutritional_sleeprest = page.locator('//a[normalize-space()="Sleep and Rest"]')
        self.menu_sports_nutritional_Hydration = page.locator('//a[normalize-space()="Hydration and Nutrition"]')
        self.menu_sports_nutritional_bodycomposition = page.locator('//a[normalize-space()="Body Composition"]')
        self.menu_sports_nutritional_24hour = page.locator('//a[normalize-space()="24 Hour Recall Assessment"]')
        self.menu_sports_cognitive = page.locator('//span[normalize-space()="Sports Cognitive"]')
        self.menu_sports_cardio = page.locator('//span[normalize-space()="Sports Cardio"]')
        self.menu_sports_injury = page.locator('//span[normalize-space()="Injury Prevention Analysis"]')
        self.menu_sports_performance_analysis = page.locator('//span[normalize-space()="Sports Performance Analysis"]')
        self.menu_manage = page.locator('//span[normalize-space()="Manage"]')
        self.menu_manage_user = page.locator('//a[normalize-space()="User"]')
        self.menu_manage_organization = page.locator('//a[normalize-space()="Organization"]')
        self.menu_manage_team= page.locator('//a[normalize-space()="Team"]')
        self.menu_manage_assessment = page.locator('//a[normalize-space()="Assessment"]')
        self.dashboard_logout = page.locator('//span[normalize-space()="Log Out"]')
        self.title_user = page.locator('//div[@class="Title"]')
        self.dashboard_name = page.locator('//p[@class="description"]')
        self.dashboard_orgnaization_label = page.locator('//h4[normalize-space()="Organization"]')
        self.dashboard_team_label = page.locator('//h4[normalize-space()="Team"]')
        self.dashboard_team_dropdown = page.locator('//ng-select[@class="ng-select-custom disabled-dropdown ng-select ng-select-single ng-untouched ng-pristine ng-select-disabled"]')
        self.dashboard_test_label = page.locator('//h4[normalize-space()="Test Type"]')
        self.dashboard_category_label = page.locator('//h4[normalize-space()="Category"]')
        self.dashboard_download_id_button = page.locator('//button[normalize-space()="Download Players Ids"]')
        self.dashboard_overall_performers = page.locator('//h4[contains(text(),"Overall")]')
        self.dashboard_players_count = page.locator('//p[normalize-space()="Players Count"]')
        self.dashboard_add_player = page.locator('//button[normalize-space()="Add New Player"]')
        self.dashboard_overall_score = page.locator('//p[normalize-space()="Overall Score"]')
        self.dashboard_overall_score_percentage = page.locator('//h2[contains(text(),"%")]')
        self.dashboard_all_performers = page.locator('//h4[normalize-space()="All Performers"]')
        self.dashboard_all_performers_category = page.locator("(//div[@class='ng-value-container']/div/span[contains(text(),'All')])[3]")
        self.dashboard_top_performer_label = page.locator('//h4[normalize-space()="Top Performer"]')
        self.dashboard_top_performer_name = page.locator('//h4[contains(text(),"Name : ")]')
        self.dashboard_top_performer_id = page.locator('//h4[contains(text(),"ID : ")]')
        self.dashboard_top_performer_test = page.locator('//th[normalize-space()="Test"]')
        self.dashboard_top_performer_score = page.locator('//th[normalize-space()="Score"]')
        
        
    def verify_dashboard(self):
        assert self.menu_dashboard.text_content() == 'Dashboard'
        assert self.menu_sports_talent.text_content() == 'Sports Talent Identification'
        assert self.menu_school_health.text_content() == 'School Health & Fitness'
        assert self.menu_sports_physical.text_content() == 'Sports Physical Fitness'
        assert self.menu_sports_nutritional.text_content() == 'Sports Nutritional'
        self.menu_sports_nutritional.click()
        assert self.menu_sports_nutritional_sleeprest.text_content() == 'Sleep and Rest'
        assert self.menu_sports_nutritional_Hydration.text_content() == 'Hydration and Nutrition'
        assert self.menu_sports_nutritional_bodycomposition.text_content() == 'Body Composition'
        assert self.menu_sports_nutritional_24hour.text_content() == '24 Hour Recall Assessment'
        self.menu_sports_nutritional.click()
        assert self.menu_sports_cognitive.text_content() == 'Sports Cognitive'
        assert self.menu_sports_cardio.text_content() == 'Sports Cardio'
        assert self.menu_sports_injury.text_content() == 'Injury Prevention Analysis'
        assert self.menu_sports_performance_analysis.text_content() == 'Sports Performance Analysis'
        assert self.menu_manage.text_content() == 'Manage'
        self.menu_manage.click()
        assert self.menu_manage_user.text_content() == 'User'
        assert self.menu_manage_organization.text_content() == 'Organization'
        assert self.menu_manage_team.text_content() == 'Team'
        assert self.menu_manage_assessment.text_content() == 'Assessment'
        self.menu_manage.click()
        assert self.dashboard_logout.text_content() == 'Log Out'
        "Hello, " in self.title_user.text_content()
        "Welcome" in self.dashboard_name.text_content()
        print(self.dashboard_name.text_content())
        assert self.dashboard_orgnaization_label.text_content() == 'Organization'
        assert self.dashboard_team_label.text_content() == 'Team'
        self.dashboard_team_dropdown.is_disabled()
        assert self.dashboard_test_label.text_content() == ' Test Type'
        assert self.dashboard_category_label.text_content() == 'Category'
        assert self.dashboard_download_id_button.text_content() == 'Download Players Ids'
        assert self.dashboard_overall_performers.text_content() == 'Overall  Performers'
        assert self.dashboard_players_count.text_content() == 'Players Count'
        assert self.dashboard_add_player.text_content() == 'Add New Player'
        assert self.dashboard_overall_score.text_content() == 'Overall Score'
        assert '%' in self.dashboard_overall_score_percentage.text_content()
        assert self.dashboard_all_performers.text_content() == 'All Performers'
        assert self.dashboard_all_performers_category.text_content() == 'All'
        assert self.dashboard_top_performer_label.text_content() == 'Top Performer'
        assert 'Name :' in self.dashboard_top_performer_name.text_content()
        assert 'ID :' in self.dashboard_top_performer_id.text_content()
        assert self.dashboard_top_performer_test.text_content() == 'Test'
        assert self.dashboard_top_performer_score.text_content() == 'Score'