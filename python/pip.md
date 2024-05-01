# pip - *package installer for python*

O comando `pip` permite instalar pacotes da linguagem python.

## versão

Para verificar se o pip está corretamente instalado na máquina, execute no terminal:

```bash
pip -V
```

## instalar pacote

```bash
pip install requests
```

Opções:

```bash
--user
instala dependências na pasta $HOME/.local
```

por padrão pip instala pacotes python na pasta (requer permissão root)
> /usr/local/lib/python3.x 

--user permite usuários a instalação de pacotes sem permissão de super usuário

## local de instalação

Verifica o local onde as dependências estão instaladas:

```bash
python3 -m site --user-base
```

Por padrão no linux estão nas pastas:

Libs:
> /home/user/.local/lib/python3.x/site-packages

binaries:
> /home/user/.local/bin

