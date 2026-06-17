import re
from pathlib import Path

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.selecionar_arquivo_button = page.get_by_role(
            "button",
            name="Selecionar arquivo",
        )

    def upload_arquivo(self, arquivo: Path) -> None:
        with self.page.expect_file_chooser() as file_chooser_info:
            self.selecionar_arquivo_button.click()

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
