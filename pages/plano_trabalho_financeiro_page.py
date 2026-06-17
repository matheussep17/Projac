from playwright.sync_api import Page

from pages.plano_trabalho_financeiro_aprovacao_page import (
    PlanoTrabalhoFinanceiroAprovacaoPage,
)
from pages.plano_trabalho_financeiro_cronograma_page import (
    PlanoTrabalhoFinanceiroCronogramaPage,
)
from pages.plano_trabalho_financeiro_descricao_page import (
    PlanoTrabalhoFinanceiroDescricaoPage,
)
from pages.plano_trabalho_financeiro_projeto_page import (
    PlanoTrabalhoFinanceiroProjetoPage,
)


class PlanoTrabalhoFinanceiroPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.menu_plano_trabalho = page.locator("span").filter(
            has_text="Plano de Trabalho Financeiro"
        )
        self.cadastrar_plano_card = page.locator("span.card-nome").filter(
            has_text="Cadastrar Plano de Trabalho Financeiro"
        )
        self.projeto = PlanoTrabalhoFinanceiroProjetoPage(page)
        self.aprovacao = PlanoTrabalhoFinanceiroAprovacaoPage(page)
        self.descricao = PlanoTrabalhoFinanceiroDescricaoPage(page)
        self.cronograma = PlanoTrabalhoFinanceiroCronogramaPage(page)

    def abrir_cadastro(self) -> None:
        self.menu_plano_trabalho.click()
        self.cadastrar_plano_card.click()
