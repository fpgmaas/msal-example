# msal-example

Unit tests fail:

```sh
uv add msal-extensions
uv sync
uv run python -m pytest
```

Unit tests succeed:

```sh
uv remove msal-extensions
uv sync
uv run python -m pytest
```