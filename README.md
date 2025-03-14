# msal-example

This repo serves as a reproducible example for [this issue](https://github.com/AzureAD/microsoft-authentication-extensions-for-python/issues/140#issuecomment-2725509472) in `msal-extensions`.

To reproduce, clone the repository and install the environment with

```sh
uv sync
```

By default `msal-extensions` is added to the project, and the unit tests fail;

```sh
uv run python -m pytest
```

Removing `msal-extensions` will make the unit tests succeed:

```sh
uv remove msal-extensions
uv sync
uv run python -m pytest
```