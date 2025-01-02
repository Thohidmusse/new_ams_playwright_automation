import time 
from playwright.sync_api import sync_playwright 
def check_links(page): # Get all links on the page 
    links = page.locator('a').all() 
    print(f"Total links found: {len(links)}") 
    for link in links: 
        href = link.get_attribute('href') 
        print(f"Checking link: {href}") # Skip empty or anchor links 
    if href and href.startswith('http'): 
        try: 
            # Click on the link and wait for the page to load 
            with page.expect_navigation(): 
                link.click() 
                print(f"Link {href} clicked successfully") 
                time.sleep(2) # Wait for 2 seconds 
        except Exception as e: 
            print(f"Failed to click link {href}: {e}") 
            # Go back to the original page 
            page.go_back() 
            time.sleep(2) # Wait for 2 seconds