# Git

## Instalação

```bash
sudo apt install git
```

Configurar email e nome do usuário:

```bash
git config --global user.email "email@gmail.com"
```

```bash
git config --global user.name "UserName"
```

## Comandos

Comandos frequentes:

### Cria um repositório git local

```bash
cd myproject
git init
git add -A
git commit -m "initial commit"
```

### Clonar repositório git

Faz download de um repositório git para a máquina local:

```bash
git clone https://github.com/fscheidt/dev.git
```

**Clonagem rasa:**

Obtém uma cópia do repositório com a última versão apenas (ignora histórico). Útil quando o repositório é muito grande e assim é possível reduzir bastante o tamanho ocupado.

```bash
git clone --depth 1 https://github.com/django/django.git
```

**Clonagem profunda:** ou duplicar o repositório, o que significa que todos os branchs vão ser copiados, não apenas o master/main.

```bash
git clone --bare https://github.com/github/gitignore
```

### Adicionar um novo arquivo

Adiciona o arquivo file.py
```bash
git add file.py
```

Faz commit do arquivo. Deve ser especificado uma mensagem descrevendo o conteúdo do commit.

```bash
git commit -m "arquivo file.py adicionado"
```

### push

Faz o **envio** dos arquivos modificados no repositório local para o Github (servidor remoto)

```bash
git push origin master
```

### pull

Faz uma requisição da última versão do repositório remoto e **atualiza** a versão local

```bash
git pull origin master
```

### reset
Apaga todas os arquivos do repositório local substituindo pela versão última versão do repositório remoto (github).

```bash
git fetch && git reset --hard origin/master
```

## Submodules

Adiciona um repositório como sub-módulo
```bash
git submodule add https://github.com/fscheidt/help
```

Atualiza o sub-módulo local a partir do repositório remoto
```bash
git submodule update --remote
```

Exibe log de commits incluindo modificações nos sub-módulos
```bash
git log -p --submodule
```

Clona repositório incluindo todos sub-módulos
```bash
git clone --recurse-submodules https://github.com/fscheidt/dotnext
cd help
git checkout master
```

Faz pull de um sub-módulo quando este foi adicionado posteriormente ao projeto.
```bash
git submodule update --init --recursive
```

Faz pull de modificações nos sub-módulos remotos
```bash
git submodule update --remote --merge
```

Push de modificações no submodule
```bash
# primeiro faz commit no sub-modulo
cd submod && git add -A && git commit -m "update abc" && git push
# em seguida faz commit no projeto principal
git add submod && git commit -am "update submod" && git push
```
