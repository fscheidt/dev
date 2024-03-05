# Instalação Flask

## Pré-requisitos

Verificar se estão instalados:

- python3
- pip
- Visual studio

### Python 3

abrir terminal e digitar:

```bash
python3
```

Deve apresentar o prompt do interpretador python (CTRL+D para sair):

```console
user@vm:~$ python3
Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

caso o python não esteja instalado fazer baixar o instalador para o seu sistema operacional:

- https://www.python.org/downloads/

### Pip

No terminal digitar:

```bash
pip -V
```

Saída:

```console
user@vm:~$ pip -V
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

### Visual studio

No terminal:

```bash
code .
```

Caso não tenha instalado, baixar o instalador do site:

- https://code.visualstudio.com/

## Projeto flask

Agora podemos criar um projeto web python usando o framework Flask.

### Criar o Workspace

Criar uma pasta `pyweb` para armazenar os arquivos do projeto, que em desenvolvimento de software é chamado de *workspace*:

```bash
mkdir pyweb
cd pyweb
```

### Criar o ambiente virtual

Para instalar outras bibliotecas do python é preciso **criar** um *virtual environment* e **ativá-lo**.

A seguir é criado o ambiente **env**

```bash
python3 -m venv env --without-pip --system-site-packages
```

para usar esse ambiente, é preciso ativá-lo:

```bash
source env/bin/activate
```

### Instalação do Flask

Logo após criar e ativar o ambiente virtual instalamos o framework Flask usando o pip:

```bash
pip install Flask
```

Saída

```console

(env) scheidt@vm:~/pyweb$ pip install Flask
Collecting Flask
  Downloading Flask-2.2.2-py3-none-any.whl (101 kB)
     |████████████████████████████████| 101 kB 2.3 MB/s 
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting importlib-metadata>=3.6.0; python_version < "3.10"
  Downloading importlib_metadata-4.13.0-py3-none-any.whl (23 kB)
Collecting Jinja2>=3.0
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 4.0 MB/s 
Collecting click>=8.0
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     |████████████████████████████████| 96 kB 2.1 MB/s 
Collecting Werkzeug>=2.2.2
  Downloading Werkzeug-2.2.2-py3-none-any.whl (232 kB)
     |████████████████████████████████| 232 kB 2.8 MB/s 
Collecting zipp>=0.5
  Downloading zipp-3.8.1-py3-none-any.whl (5.6 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Installing collected packages: itsdangerous, zipp, importlib-metadata, MarkupSafe, Jinja2, click, Werkzeug
Successfully installed Flask-2.2.2 Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.2.2 click-8.1.3 importlib-metadata-4.13.0 itsdangerous-2.1.2 zipp-3.8.1

```

### `app.py`

Agora podemos abrir o visual studio e criar o arquivo `app.py`. Colar o código abaixo dentro do arquivo:

```python
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    agora = datetime.now()
    return f"Seja bem vindo - {agora}"

if __name__ == "__main__":
    app.run(debug=True)

```

Executar `app.py` pelo visual studio

Abrir o navegador no endereço: http://localhost:5000/


**END**

<br>
<br>

--- 

## Comandos alternativos

### Instalação flask com python

```bash
python -m pip install flask
```

### Instalações adicionais

Na instalação padrão do ubuntu é necessário instalar também os pacotes `python3-pip` e `python3-venv` para criar o ambiente virtual e conseguir instalar outras bibliotecas do python como o Flask. Porém o usuário necessita de permissão para rodar o comando `sudo` (senha admin):

```bash
sudo apt-get install python3-pip
sudo apt-get install python3-venv
```

O python3-venv facilita para criar novos ambientes:
```bash
python3 -m venv env
source env/bin/activate
```




## Referências

Para mais detalhes de configuração do ambiente python e flask no vscode, assim como os passos para configuração no windows, vejam o tutorial da microsoft:

- [Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask)
