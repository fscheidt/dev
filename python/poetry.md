# Poetry

Gerenciamento de dependências para projetos em Python.

- https://python-poetry.org/

## Install

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

> verificar a versão instalada

```bash
poetry --version
```

*Se o comando acima falhar, adicionar na variável PATH o caminho de instalação do poetry:*

```bash
echo 'export PATH="${HOME}/.local/bin:${PATH}"' >> ~/.bashrc
```

## Criar *novo* projeto

O comando `poetry new` cria um novo projeto chamado "poetry-demo"

```bash
poetry new poetry-demo
```

## Adicionar o poetry a um projeto *existente*

O comando `poetry init` cria os arquivos `pyproject.toml` que contém as dependências do projeto.

```bash
poetry init
```

## Adiciona a biblioteca `requests`

O comando `poetry add` adiciona uma biblioteca python como dependência ao projeto, atualizando o arquivo pyproject.toml.

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


