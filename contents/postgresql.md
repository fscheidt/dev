
# Postgresql

## ubuntu

## instalação padrão

```bash
sudo apt -y install postgresql
```

## instalação manual
```bash
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql
```

### acesso pelo terminal

alterar senha

```bash
# define senha usuario postgres
sudo -u postgres psql
# prompt
\password postgres
\q
```

## Python lib - psycopg

- https://www.psycopg.org/install/

```bash
sudo apt install python3-dev libpq-dev
sudo pip install psycopg2
```
