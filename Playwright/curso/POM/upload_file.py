from playwright.sync_api import Playwright
from Pages.upload_file_page import upload_file

file_path = 'Playwright/POM/images/selector.png'

def test_upload_file(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=2000, args=["--start-maximized"])
    page = browser.new_page()
    page.set_default_timeout(5000)

    upfile = upload_file(page)
    upfile.navigate('https://qa-practice.netlify.app/file-upload')
    upfile.upload_file(file_path)
    upfile.submit_file()
    upfile.read_confirmation_message('You have successfully uploaded "selector.png"')

    page.close()
    browser.close()

def test_remove_uploaded_file(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=2000, args=["--start-maximized"])
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)

    upfile = upload_file(page)
    upfile.navigate('https://qa-practice.netlify.app/file-upload')
    upfile.upload_file(file_path)
    upfile.upload_file([])
    upfile.submit_file()
    upfile.read_confirmation_message('You have successfully uploaded ""')

    # ---------------------
    context.close()
    browser.close()