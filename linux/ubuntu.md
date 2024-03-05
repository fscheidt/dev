# Ubuntu initial setup

## first

check installed version:

```bash
lsb_release -drc && uname -r
```

system update:

```bash
sudo apt-get update && sudo apt-get upgrade -y
```

> basic utilities:

```bash
sudo apt install vim curl git -y
```

> zip and rar
```bash
sudo apt install rar unrar p7zip-full p7zip-rar pigz attr brotli -y
```

> build tools

[pyenv deps](/python/pyenv.md)


## python

> check python:

```bash
python --version
python3 --version
pip -V
```

```bash
sudo apt-get install python3-pip python3-venv -y
```

## [Node.js install](/javascript/nodejs.md)

## [Java](/contents/java.md)


## Utilities

> [git config](/contents/git.md) (set username and email)


## Other packages

- [ubuntu-extras](/linux/ubuntu-extras.md)

