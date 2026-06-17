import re
from pathlib import Path

from pages.base_page import BasePage


class PlanoTrabalhoFinanceiroAprovacaoPage(BasePage):
    def abrir(self) -> None:
        self.page.get_by_role(
            "tab",
            name=re.compile(r"Dados da Aprova", re.I),
        ).click()

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
            re.compile(r"Unidade de aprova", re.I),
            unidade,
            opcao_unidade,
        )
        self.fill_autocomplete(
            re.compile(r"Respons.*vel pela aprova", re.I),
            responsavel,
            opcao_responsavel,
        )
        self.upload_arquivo(arquivo)
