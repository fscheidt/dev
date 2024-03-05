# Visual studio code

## Download and install

- https://code.visualstudio.com/download

## Settings

No raiz do projeto criar o arquivo `settings.json` na pasta `.vscode`


Configura diferentes níveis de indentação (`tabSize`) de acordo com a linguagem de programação:

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
