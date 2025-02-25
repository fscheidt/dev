# gitignore

O arquivo `.gitignore` deve ser criado na pasta raiz do projeto. Nele são especificados os padrões de arquivos e diretórios que devem ser ignorados no controle de versionamento. A seguir alguns templates para o gitignore de acordo com a linguagem de desenvolvimento:

### Projetos python

Todos os arquivo abaixo são *ignorados* pelo git:

```
*.zip
*.7z
.idea/

# Jupyter Notebook
.ipynb_checkpoints

__pycache__/  
*.py[cod]  
*$py.class

# Distribution / packaging
build/
develop-eggs/
dist/
downloads/
lib/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Cython debug symbols
cython_debug/
```


## Projetos java

```git
HELP.md
target/
!.mvn/wrapper/maven-wrapper.jar
!**/src/main/**/target/
!**/src/test/**/target/

### STS ###
.apt_generated
.classpath
.factorypath
.project
.settings
.springBeans
.sts4-cache

### IntelliJ IDEA ###
.idea
*.iws
*.iml
*.ipr

### NetBeans ###
/nbproject/private/
/nbbuild/
/dist/
/nbdist/
/.nb-gradle/
build/
!**/src/main/**/build/
!**/src/test/**/build/

# Compiled class file
*.class

# Log file
*.log

# Package Files
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs
hs_err_pid*

```
