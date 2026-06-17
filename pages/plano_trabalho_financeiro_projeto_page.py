import re
from pathlib import Path

from playwright.sync_api import Page

from pages.base_page import BasePage


class PlanoTrabalhoFinanceiroProjetoPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.tipo_projeto_select = page.locator(".mat-mdc-select-placeholder")
        self.nome_projeto_input = page.get_by_role("combobox", name="Nome do projeto")
        self.subtitulo_input = page.get_by_role(
            "textbox",
            name=re.compile(r"Subt.*projeto", re.I),
        )
        self.dados_coordenador_tab = page.get_by_role(
            "tab",
            name=re.compile(r"Dados do.*Coordenador", re.I),
        )

    def preencher_dados_basicos(
        self,
        tipo_projeto: str,
        nome_projeto: str,
        opcao_projeto: re.Pattern[str],
        subtitulo: str,
        arquivo: Path,
    ) -> None:
        self.tipo_projeto_select.click()
        self.page.get_by_role("option", name=tipo_projeto).click()

        self.nome_projeto_input.click()
        self.nome_projeto_input.fill(nome_projeto)
        self.page.get_by_text(opcao_projeto).click()

        self.subtitulo_input.click()
        self.subtitulo_input.fill(subtitulo)
        self.subtitulo_input.press("Enter")

        self.upload_arquivo(arquivo)

    def abrir_aba_coordenador(self) -> None:
        self.dados_coordenador_tab.click()
