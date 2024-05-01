# Visual studio code

## Download and install

- download `.deb` file from https://code.visualstudio.com/download

> Install:

```bash
sudo apt install ./code_1.88.1-1712771838_amd64.deb
```

## Settings

- Na raiz do projeto criar a pasta `.vscode`
- Dentro da pasta `.vscode` criar o arquivo `settings.json`


Adicionar a configuração abaixo no arquivo `settings.json` que configura o espaçamento da [indentação](https://pt.wikipedia.org/wiki/Indenta%C3%A7%C3%A3o) (`tabSize`) de acordo com a linguagem de programação:

```json
{
    "[html]": {
        "editor.tabSize": 2,
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "[javascript]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.tabSize": 2
    },
    "[python]": {
        "editor.tabSize": 4,
        "editor.wordBasedSuggestions": false
    }
}
```
