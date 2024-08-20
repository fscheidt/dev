# Visual studio code

## Download and install

- download `.deb` file from https://code.visualstudio.com/download

> Install:

```bash
sudo apt install ./code_1.88.1-1712771838_amd64.deb
```

## Configurações

### Configuração por projeto

- Na raiz do projeto criar a pasta `.vscode`
- Dentro da pasta `.vscode` criar o arquivo `settings.json`


Adicionar as configurações a seguir em `settings.json` para definir o espaçamento da [indentação](https://pt.wikipedia.org/wiki/Indenta%C3%A7%C3%A3o) (`tabSize`) de acordo com o tipo da linguagem do arquivo aberto no editor:

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

### Configurações globais

> `~/.config/Code/User/keybindings.json`

```json
[
    {
        "key": "ctrl+d",
        "command": "editor.action.deleteLines",
        "when": "textInputFocus && !editorReadonly"
    },
    {
        "key": "ctrl+shift+k",
        "command": "-editor.action.deleteLines",
        "when": "textInputFocus && !editorReadonly"
    },
    {
        "key": "ctrl+down",
        "command": "editor.action.moveLinesDownAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "alt+down",
        "command": "-editor.action.moveLinesDownAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "ctrl+up",
        "command": "editor.action.moveLinesUpAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "alt+up",
        "command": "-editor.action.moveLinesUpAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "ctrl+.",
        "command": "editor.action.copyLinesDownAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "ctrl+shift+alt+down",
        "command": "-editor.action.copyLinesDownAction",
        "when": "editorTextFocus && !editorReadonly"
    }
]
```

> `~/.config/Code/User/settings.json`

```json
{
    "files.autoSave": "afterDelay",
    "files.exclude": {
        ".git": true,
        ".idea": true,
        ".vscode": true,
        "**/__pycache__/": true,
        "**/.DS_Store": false,
        "**/.git": false,
        "**/.hg": false,
        "**/.ipynb_checkpoints/": true,
        "**/.pytest_cache/": true,
        "**/.svn": false,
        "**/CVS": false,
        "**/Thumbs.db": false
    },
    "editor.stickyScroll.enabled": false,
    "editor.lineHeight": 1.6,
    "editor.fontFamily": "'Meslo','monospace', monospace",
    "editor.minimap.enabled": false,
    "editor.renderLineHighlightOnlyWhenFocus": true,
    "explorer.confirmDelete": false,
    "explorer.confirmPasteNative": false,
    "explorer.confirmDragAndDrop": false,
    "git.openRepositoryInParentFolders": "never",
    "jupyter.askForKernelRestart": false,
    "liveServer.settings.donotShowInfoMsg": true,
    "notebook.lineNumbers": "on",
    "notebook.output.lineHeight": 1.1,
    "notebook.output.fontSize": 14,
    "notebook.output.fontFamily": "Roboto Mono, Noto Sans Mono",
    "notebook.markdown.lineHeight": 24,
    "notebook.markup.fontSize": 16,
    "notebook.output.textLineLimit": 60,
    "notebook.showFoldingControls": "always",
    "terminal.integrated.lineHeight": 1,
    "terminal.integrated.fontSize": 12,
    "window.menuBarVisibility": "compact",
    "window.zoomLevel": 1.4,
    "workbench.iconTheme": "ayu",
    "workbench.colorTheme": "Default High Contrast Light",
    "[javascript]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "[html]": {
        "editor.defaultFormatter": "vscode.html-language-features"
    }
}
```