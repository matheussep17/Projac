import re
from pathlib import Path

from pages.base_page import BasePage


class PlanoTrabalhoFinanceiroProjetoPage(BasePage):
    def preencher_dados_basicos(
        self,
        tipo_projeto: str,
        nome_projeto: str,
        opcao_projeto: re.Pattern[str],
        subtitulo: str,
        arquivo: Path,
    ) -> None:
        self.page.locator(".mat-mdc-select-placeholder").click()
        self.page.get_by_role("option", name=tipo_projeto).click()

        self.page.get_by_role("combobox", name="Nome do projeto").click()
        self.page.get_by_role("combobox", name="Nome do projeto").fill(nome_projeto)
        self.page.get_by_text(opcao_projeto).click()

        subtitulo_field = self.page.get_by_role(
            "textbox",
            name=re.compile(r"Subt.*projeto", re.I),
        )
        subtitulo_field.click()
        subtitulo_field.fill(subtitulo)
        subtitulo_field.press("Enter")

        self.upload_arquivo(arquivo)

    def abrir_aba_coordenador(self) -> None:
        self.page.get_by_role(
            "tab",
            name=re.compile(r"Dados do.*Coordenador", re.I),
        ).click()
