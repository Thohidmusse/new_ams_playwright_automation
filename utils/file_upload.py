from pathlib import Path
from playwright.sync_api import Page

def upload_image(page: Page, input_selector: str, image_path: str):
    """
    Uploads an image file to the specified input element on a web page.

    :param page: The Playwright Page object
    :param input_selector: The CSS selector of the input element
    :param image_path: The path to the image file to be uploaded
    """
    image_file = Path(image_path)
    if not image_file.exists():
        raise FileNotFoundError(f"Image file not found: {image_path}")
    page.set_input_files(input_selector, image_path)

def upload_file(page: Page, file_input_locator: str, file_path: str):
    """
    Uploads a file using the specified file input locator.

    :param page: The Playwright Page object
    :param file_input_locator: The CSS selector of the file input element
    :param file_path: The path to the file to be uploaded
    """
    file_input = page.locator(file_input_locator)
    file_input.set_input_files(file_path)
    print(f"Uploaded file: {file_path}")
