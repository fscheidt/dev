# PYENV


## Install PyEnv

```bash
curl https://pyenv.run | bash
```

close and open a new terminal


## Load PyEnv 

Append the following to `~/.bashrc`:

```bash
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Restart your shell for the changes to take effect.


### one liner

```bash
# export PYENV_ROOT="$HOME/.pyenv" && command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH" && eval "$(pyenv init -)" && eval "$(pyenv virtualenv-init -)" >> ~/.bashrc
```

## Check PyEnv

```bash
pyenv -v
```


## Update PyEnv

```bash
pyenv update
```


## List Python versions

List available python versions to install:

```bash
pyenv install -l
```


## Install Python

Install python 3.12.2

```bash
pyenv install 3.12.2
```


### Check Python

```bash
pyenv versions
```

```bash
pyenv global
```


## Change global python

```bash
pyenv global 3.12.2
```


## Optimization (optional)

### Dependencies

(optional) Install if building python:

```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

### Build

```bash
env PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto' PYTHON_CFLAGS='-march=native -mtune=native' pyenv install 3.12.2
```
