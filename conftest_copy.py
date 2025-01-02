# amsui_playwright_framework/conftest.py
import time
import pytest
from playwright.sync_api import sync_playwright
from utils.config_copy import load_config 
from pages.login_page_copy import LoginPage

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
def logged1_in_page(page): 
    config = load_config() 
    username = config['USERNAME'] 
    password = config['PASSWORD'] 
    base_url = config['BASE_URL'] 
    login_page = LoginPage(page, base_url) 
    login_page.login(username, password) 
    return page


