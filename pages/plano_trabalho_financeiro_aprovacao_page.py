import re
from pathlib import Path

from playwright.sync_api import Page

from pages.base_page import BasePage


class PlanoTrabalhoFinanceiroAprovacaoPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.aprovacao_tab = page.get_by_role(
            "tab",
            name=re.compile(r"Dados da Aprova", re.I),
        )
        self.unidade_field_name = re.compile(r"Unidade de aprova", re.I)
        self.responsavel_field_name = re.compile(r"Respons.*vel pela aprova", re.I)

    def abrir(self) -> None:
        self.aprovacao_tab.click()

    def preencher(
        self,
        unidade: str,
        opcao_unidade: str,
        responsavel: str,
        opcao_responsavel: re.Pattern[str],
        arquivo: Path,
    ) -> None:
        self.abrir()
        self.fill_autocomplete(
            self.unidade_field_name,
            unidade,
            opcao_unidade,
        )
        self.fill_autocomplete(
            self.responsavel_field_name,
            responsavel,
            opcao_responsavel,
        )
        self.upload_arquivo(arquivo)
