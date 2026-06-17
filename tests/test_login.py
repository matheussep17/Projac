from config.settings import settings
from pages.login_page import LoginPage


def test_login_success(page):
    login_page = LoginPage(page)

    login_page.open(settings.base_url)
    login_page.should_be_loaded()
    login_page.login(settings.username, settings.password)
    login_page.should_be_logged_in()
