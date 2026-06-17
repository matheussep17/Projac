import re
from pathlib import Path

from playwright.sync_api import Page

from config.settings import settings
from pages.login_page import LoginPage
from pages.plano_trabalho_financeiro_page import PlanoTrabalhoFinanceiroPage


TEST_FILE = Path("fixtures/TesteArquivoPDF.pdf").resolve()


def test_plano_de_trabalho_financeiro(page: Page) -> None:
    login_page = LoginPage(page)
    plano_page = PlanoTrabalhoFinanceiroPage(page)

    login_page.open(settings.base_url)
    login_page.should_be_loaded()
    login_page.login(settings.username, settings.password)
    login_page.should_be_logged_in()

    plano_page.abrir_cadastro()
    plano_page.projeto.preencher_dados_basicos(
        tipo_projeto="Pesquisa",
        nome_projeto="teste",
        opcao_projeto=re.compile(r"PI09224-2026 - Avalia"),
        subtitulo="teste",
        arquivo=TEST_FILE,
    )
    plano_page.projeto.abrir_aba_coordenador()
    plano_page.aprovacao.preencher(
        unidade="cercomp",
        opcao_unidade="CERCOMP - CENTRO DE RECURSOS",
        responsavel="lauro",
        opcao_responsavel=re.compile(r"LAURO RAMON GOMIDES"),
        arquivo=TEST_FILE,
    )
    plano_page.descricao.preencher(
        banco="Banco do Brasil",
        valor_disponibilizado="100,00",
    )
    plano_page.cronograma.preencher(
        etapa="2",
        descricao="etapa 2",
        quantidade="1",
    )

    plano_page.cronograma.should_have_quantidade("1")
