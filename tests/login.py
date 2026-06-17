import re
from playwright.sync_api import Playwright, sync_playwright, expect

from config.settings import settings


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(settings.base_url)
    page.get_by_role("button", name="OK, entendi").click()
    page.get_by_role("textbox", name="Informe seu login").click()
    page.get_by_role("textbox", name="Informe seu login").fill(settings.username)
    page.get_by_role("textbox", name="Senha").click()
    page.get_by_role("textbox", name="Senha").fill(settings.password)
    page.get_by_role("button", name="Entrar").click()
    expect(page.get_by_text("Página Inicial")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
