import pytest
from pages.dashboard_page import DashboardPage 

@pytest.mark.regression 
def test_verify_menu_dashboard(logged_in_page):
    dashboard_page = DashboardPage(logged_in_page) 
    dashboard_page.verify_dashboard()