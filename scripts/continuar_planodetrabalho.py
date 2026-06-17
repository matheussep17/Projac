import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from config.settings import settings
from pages.login_page import LoginPage
from pages.plano_trabalho_financeiro_page import PlanoTrabalhoFinanceiroPage


TEST_FILE = Path("fixtures/TesteArquivoPDF.pdf").resolve()


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=250)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

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

        page.pause()
        input("Pressione Enter aqui no terminal para fechar o navegador...")

        context.close()
        browser.close()


if __name__ == "__main__":
    main()
