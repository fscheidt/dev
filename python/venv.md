# venv

## Criar ambiente virtual python

Seja o nome do projeto `pyweb`, executar a seguinte sequência de comandos no terminal para criar um ambiente virtual python para o projeto:

**(1) abrir o terminal na pasta pyweb:**

```bash
cd pyweb
```

confirir se o terminal esta na pasta correta:
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

testar se o ambiente foi corretamente instalado e se esta ativado:
```bash
which python
```

saída no terminal:
<pre>
(env)  ~/pyweb$ which python
/home/ifpr/projetos/pyweb/env/bin/python
</pre>

**(4) Instalar biblioteca**

Dentro do projeto **pyweb**, deverá aparecer uma nova pasta com nome `env`. Esta pasta contém a instalação do python e outras bibliotecas (dependências) usadas no projeto.

Para instalar uma nova biblioteca no projeto, verificar se o ambiente esta ativado e na sequencia executar o comando `pip install`. 

Exemplo de instalação da biblioteca `requests`:

```bash
pip install requests
```

