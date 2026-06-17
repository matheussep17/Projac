# Projac

Projeto inicial de automacao com Playwright em Python.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
Copy-Item .env.example .env
```

Edite o arquivo `.env` com a URL e as credenciais do ambiente.

## Rodar os testes

```powershell
pytest
```

Para ver o navegador abrindo:

```powershell
pytest --headed
```

## Usar o codegen

```powershell
playwright codegen https://example.com
```
