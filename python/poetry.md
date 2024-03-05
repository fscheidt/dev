# Poetry
Gerenciamento de dependências para Python.

- https://python-poetry.org/

## Install

```bash
curl -sSL https://install.python-poetry.org | python3 -
```


```bash
poetry --version
```
Se o comando acima falhar, rodar o comando abaixo para adicionar o caminho para o poetry:

```bash
echo 'export PATH="${HOME}/.local/bin:${PATH}"' >> ~/.bashrc
```

## Criar novo projeto

```bash
poetry new poetry-demo
```

## Adicionar o poetry a um projeto

```bash
poetry init
```

## Adiciona a biblioteca `requests`

```bash
poetry add requests
```

## Ativar o ambiente
```bash
poetry shell
```

## Instalar dependências
Instala todas a dependências definidas no arquivo `pyproject.toml`

```bash
poetry install
```

---

## Exemplo projeto pycine

```
git clone https://github.com/fscheidt/pycine
cd pycine
poetry install
poetry add requests fastapi uvicorn
poetry shell
uvicorn pycine:app --reload
```



## poetry config

```bash
vi ~/.config/pypoetry/config.toml
```

> add to config.toml

```bash
# use current active env as default
virtualenvs.prefer-active-python = true
```


