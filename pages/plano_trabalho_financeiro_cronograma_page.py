from playwright.sync_api import expect

from pages.base_page import BasePage


class PlanoTrabalhoFinanceiroCronogramaPage(BasePage):
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
        self.page.get_by_role("spinbutton", name="Etapa").fill(etapa)
        self.page.get_by_role("textbox", name="Descricao").fill(descricao)
        self.page.get_by_role("spinbutton", name="Quantidade").fill(quantidade)

    def should_have_quantidade(self, quantidade: str) -> None:
        expect(self.page.get_by_role("spinbutton", name="Quantidade")).to_have_value(
            quantidade
        )
