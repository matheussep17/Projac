import re
from pathlib import Path

from playwright.sync_api import Page, expect

from config.settings import settings
from pages.login_page import LoginPage


TEST_FILE = Path("fixtures/TesteArquivoPDF.pdf").resolve()


def upload_test_file(page: Page) -> None:
    with page.expect_file_chooser() as file_chooser_info:
        page.get_by_role("button", name="Selecionar arquivo").click()

    file_chooser_info.value.set_files(str(TEST_FILE))


def fill_autocomplete(page: Page, field_name: re.Pattern[str], value: str, option: str | re.Pattern[str]) -> None:
    field = page.get_by_role("combobox", name=field_name)

    expect(field).to_be_visible()
    field.fill(value, force=True)
    page.get_by_text(option).click()


def test_plano_de_trabalho_financeiro(page: Page) -> None:
    login_page = LoginPage(page)

    login_page.open(settings.base_url)
    login_page.should_be_loaded()
    login_page.login(settings.username, settings.password)
    login_page.should_be_logged_in()

    page.locator("span").filter(has_text="Plano de Trabalho Financeiro").click()
    page.locator("span.card-nome").filter(
        has_text="Cadastrar Plano de Trabalho Financeiro"
    ).click()

    page.locator(".mat-mdc-select-placeholder").click()
    page.get_by_role("option", name="Pesquisa").click()

    page.get_by_role("combobox", name="Nome do projeto").click()
    page.get_by_role("combobox", name="Nome do projeto").fill("teste")
    page.get_by_text(re.compile(r"PI09224-2026 - Avalia")).click()

    page.get_by_role("textbox", name=re.compile(r"Subt.*projeto", re.I)).click()
    page.get_by_role("textbox", name=re.compile(r"Subt.*projeto", re.I)).fill("teste")
    page.get_by_role("textbox", name=re.compile(r"Subt.*projeto", re.I)).press("Enter")

    upload_test_file(page)

    page.get_by_role("tab", name=re.compile(r"Dados do.*Coordenador", re.I)).click()
    page.get_by_role("tab", name=re.compile(r"Dados da Aprova", re.I)).click()

    fill_autocomplete(
        page,
        re.compile(r"Unidade de aprova", re.I),
        "cercomp",
        "CERCOMP - CENTRO DE RECURSOS",
    )
    fill_autocomplete(
        page,
        re.compile(r"Respons.*vel pela aprova", re.I),
        "lauro",
        re.compile(r"LAURO RAMON GOMIDES"),
    )

    upload_test_file(page)

    page.locator("a").filter(has_text=re.compile(r"Descri", re.I)).click()
    page.get_by_text("expand_more").click()
    page.get_by_role("option", name="Banco do Brasil").click()
    page.get_by_role("textbox", name=re.compile(r"Valor disponibilizado", re.I)).click()

    page.goto("https://projac-dev.cercomp.ufg.br/projac/projetos-academicos/plano-trabalho-financeiro/new#Cronograma")
    page.get_by_role("spinbutton", name="Etapa").fill("2")
    page.get_by_role("textbox", name="Descricao").fill("etapa 2")
    page.get_by_role("spinbutton", name="Quantidade").fill("1")

    expect(page.get_by_role("spinbutton", name="Quantidade")).to_have_value("1")
