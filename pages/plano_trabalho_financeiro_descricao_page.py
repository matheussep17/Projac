import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class PlanoTrabalhoFinanceiroDescricaoPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.descricao_tab = page.locator("a").filter(
            has_text=re.compile(r"Descri", re.I)
        )
        self.banco_select = page.get_by_text("expand_more")
        self.valor_disponibilizado_input = page.get_by_role(
            "textbox",
            name=re.compile(r"Valor disponibilizado", re.I),
        )

    def abrir(self) -> None:
        self.descricao_tab.click()

    def preencher(self, banco: str, valor_disponibilizado: str) -> None:
        self.abrir()
        self.banco_select.click()
        self.page.get_by_role("option", name=banco).click()
        self.valor_disponibilizado_input.fill(valor_disponibilizado, force=True)
