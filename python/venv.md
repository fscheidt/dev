# venv

## Criar o ambiente virtual

Seja o nome do projeto `pyweb`, executar a seguinte sequência de comandos no terminal para criar um ambiente virtual python para o projeto:

**(1) acessar a pasta pyweb:**

```bash
cd pyweb
```

confira se o terminal está dentro da pasta:
```bash
pwd
```

exemplo de resposta exibida pelo comando `pwd`:

```
/home/ifpr/projetos/pyweb
```

**(2) Criar o ambiente virtual**

```bash
python3 -m venv env
```

**(3) Ativar o ambiente**

```bash
source env/bin/activate
```

O ambiente deverá estar configurado. Dentro do projeto **pyweb**, deverá aparecer uma nova pasta com nome `env`. Esta pasta contém a instalação do python e outras bibliotecas (dependências) usadas no projeto.

Para instalar uma nova biblioteca no projeto, devemos primeiro **ativar** o ambiente e depois executar o comando pip install. Abaixo temos um exemplo onde a biblioteca `requests` é instalada no ambiente virtual:

```bash
pip install requests
```
