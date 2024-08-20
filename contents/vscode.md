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
    "workbench.colorTheme": "Default High Contrast Light",
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
    "files.autoSave": "afterDelay",
    "explorer.confirmDelete": false,
    "editor.stickyScroll.enabled": false,
    "[html]": {
        "editor.defaultFormatter": "vscode.html-language-features"
    },
    "explorer.confirmPasteNative": false,
    "liveServer.settings.donotShowInfoMsg": true,
    "explorer.confirmDragAndDrop": false,
    "editor.lineHeight": 1.6,
    "git.openRepositoryInParentFolders": "never",
    "editor.minimap.enabled": false,
    "[javascript]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "window.zoomLevel": 1.4,
    "editor.fontFamily": "'Meslo','monospace', monospace",
    "notebook.output.lineHeight": 1.1,
    "notebook.output.fontSize": 14,
    "notebook.output.fontFamily": "Roboto Mono, Noto Sans Mono, Inconsolata",
    "notebook.markdown.lineHeight": 24,
    "notebook.markup.fontSize": 16,
    "notebook.output.textLineLimit": 60,
    "notebook.showFoldingControls": "always",
    "window.menuBarVisibility": "compact",
    "terminal.integrated.lineHeight": 1,
    "terminal.integrated.fontSize": 12,
    "workbench.iconTheme": "ayu",
    "jupyter.askForKernelRestart": false,
    "editor.renderLineHighlightOnlyWhenFocus": true,
    "notebook.lineNumbers": "on"
}
```