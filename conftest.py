# amsui_playwright_framework/conftest.py
import time
import pytest
# import os
# import webbrowser
from playwright.sync_api import sync_playwright
from utils.config import load_config #newly added
from pages.login_page import LoginPage #newly added

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture 
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({'width': 1536, 'height': 730})
    #time.sleep(20)
    yield page
    time.sleep(2)
    context.close()

@pytest.fixture 
def logged_in_page(page): 
    # Replace with actual login steps 
    # page.goto("https://amsui-qa.qwalton.com") 
    # page.fill("#username", "your_username") 
    # page.fill("#password", "your_password") 
    # page.click("button[type='submit']") 
    # assert page.title() == "Dashboard" 
    # return page
    config = load_config() 
    username = config['USERNAME'] 
    password = config['PASSWORD'] 
    base_url = config['BASE_URL'] 
    login_page = LoginPage(page, base_url) 
    login_page.login(username, password) 
    return page

# def pytest_configure(config): 
#     config.option.htmlpath = 'report.html' 
    
# def pytest_sessionfinish(session, exitstatus): 
#     report_path = os.path.abspath('report.html') 
#     webbrowser.open_new_tab(f'file://{report_path}')