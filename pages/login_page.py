import re

from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Informe seu login")
        self.password_input = page.get_by_role("textbox", name="Senha")
        self.submit_button = page.get_by_role("button", name="Entrar")
        self.cookie_button = page.get_by_role("button", name="OK, entendi")
        self.home_text = page.get_by_text(re.compile(r"P.*gina Inicial"))

    def open(self, url: str) -> None:
        self.page.goto(url)
        self.accept_cookies()

    def login(self, username: str, password: str) -> None:
        self.username_input.click()
        self.username_input.fill(username)
        self.password_input.click()
        self.password_input.fill(password)
        self.submit_button.click()

    def should_be_loaded(self) -> None:
        expect(self.submit_button).to_be_visible()

    def should_be_logged_in(self) -> None:
        expect(self.home_text).to_be_visible()

    def accept_cookies(self) -> None:
        if self.cookie_button.is_visible():
            self.cookie_button.click()
