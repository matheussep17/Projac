from dataclasses import dataclass
import os

from dotenv import load_dotenv


load_dotenv()

DEFAULT_BASE_URL = (
    "https://sso-homolog.cercomp.ufg.br/cas/login"
    "?service=https://gwms-sagui-dev.cercomp.ufg.br/auth-service/cas/login"
    "?back_url=https://projac-dev.cercomp.ufg.br"
)
DEFAULT_USERNAME = ""
DEFAULT_PASSWORD = ""


def _as_bool(value: str | None, default: bool = True) -> bool:
    if value is None:
        return default

    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", DEFAULT_BASE_URL)
    username: str = os.getenv("LOGIN_USERNAME", DEFAULT_USERNAME)
    password: str = os.getenv("LOGIN_PASSWORD", DEFAULT_PASSWORD)
    headless: bool = _as_bool(os.getenv("HEADLESS"), True)


settings = Settings()
