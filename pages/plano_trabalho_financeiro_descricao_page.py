import re

from pages.base_page import BasePage


class PlanoTrabalhoFinanceiroDescricaoPage(BasePage):
    def abrir(self) -> None:
        self.page.locator("a").filter(has_text=re.compile(r"Descri", re.I)).click()

    def preencher(self, banco: str, valor_disponibilizado: str) -> None:
        self.abrir()
        self.page.get_by_text("expand_more").click()
        self.page.get_by_role("option", name=banco).click()
        self.page.get_by_role(
            "textbox",
            name=re.compile(r"Valor disponibilizado", re.I),
        ).fill(valor_disponibilizado, force=True)
