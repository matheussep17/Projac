import re
from pathlib import Path

from playwright.sync_api import Page, expect


class PlanoTrabalhoFinanceiroPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def abrir_cadastro(self) -> None:
        self.page.locator("span").filter(has_text="Plano de Trabalho Financeiro").click()
        self.page.locator("span.card-nome").filter(
            has_text="Cadastrar Plano de Trabalho Financeiro"
        ).click()

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

    def preencher_aba_aprovacao(
        self,
        unidade: str,
        opcao_unidade: str,
        responsavel: str,
        opcao_responsavel: re.Pattern[str],
        arquivo: Path,
    ) -> None:
        self.page.get_by_role(
            "tab",
            name=re.compile(r"Dados da Aprova", re.I),
        ).click()

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

    def preencher_aba_descricao(self, banco: str, valor_disponibilizado: str) -> None:
        self.page.locator("a").filter(has_text=re.compile(r"Descri", re.I)).click()
        self.page.get_by_text("expand_more").click()
        self.page.get_by_role("option", name=banco).click()
        self.page.get_by_role(
            "textbox",
            name=re.compile(r"Valor disponibilizado", re.I),
        ).fill(valor_disponibilizado, force=True)

    def preencher_aba_cronograma(
        self,
        etapa: str,
        descricao: str,
        quantidade: str,
    ) -> None:
        self.page.goto(
            "https://projac-dev.cercomp.ufg.br/projac/projetos-academicos/"
            "plano-trabalho-financeiro/new#Cronograma"
        )
        self.page.get_by_role("spinbutton", name="Etapa").fill(etapa)
        self.page.get_by_role("textbox", name="Descricao").fill(descricao)
        self.page.get_by_role("spinbutton", name="Quantidade").fill(quantidade)

    def should_have_quantidade(self, quantidade: str) -> None:
        expect(self.page.get_by_role("spinbutton", name="Quantidade")).to_have_value(
            quantidade
        )

    def upload_arquivo(self, arquivo: Path) -> None:
        with self.page.expect_file_chooser() as file_chooser_info:
            self.page.get_by_role("button", name="Selecionar arquivo").click()

        file_chooser_info.value.set_files(str(arquivo.resolve()))

    def fill_autocomplete(
        self,
        field_name: re.Pattern[str],
        value: str,
        option: str | re.Pattern[str],
    ) -> None:
        field = self.page.get_by_role("combobox", name=field_name)

        expect(field).to_be_visible()
        field.fill(value, force=True)
        self.page.get_by_text(option).click()
