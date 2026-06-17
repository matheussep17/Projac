from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class PlanoTrabalhoFinanceiroCronogramaPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.etapa_input = page.get_by_role("spinbutton", name="Etapa")
        self.descricao_input = page.get_by_role("textbox", name="Descricao")
        self.quantidade_input = page.get_by_role("spinbutton", name="Quantidade")

    def abrir(self) -> None:
        self.page.goto(
            "https://projac-dev.cercomp.ufg.br/projac/projetos-academicos/"
            "plano-trabalho-financeiro/new#Cronograma"
        )

    def preencher(
        self,
        etapa: str,
        descricao: str,
        quantidade: str,
    ) -> None:
        self.abrir()
        self.etapa_input.fill(etapa)
        self.descricao_input.fill(descricao)
        self.quantidade_input.fill(quantidade)

    def should_have_quantidade(self, quantidade: str) -> None:
        expect(self.quantidade_input).to_have_value(quantidade)
