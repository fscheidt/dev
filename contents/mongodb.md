# MongoDB


## Mongo 6.0 (ubuntu 22.04)

```bash
sudo apt update
```

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
```

```bash
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```

```bash
sudo apt-get update
```

```bash
sudo apt-get install -y mongodb-org
```

```bash
sudo systemctl start mongod
```

```bash
sudo systemctl enable mongod
```

```bash
mongod --version
```

```bash
mongosh
```
[source](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

### Compass - GUI desktop

- [Download .deb](https://www.mongodb.com/products/compass)

```bash
sudo apt install ./mongodb-compass_1.36.2_amd64.deb --fix-broken
```

## Mongo 6.0 (ubuntu 20.04)

```bash
sudo apt update

# install if necessary dependencies:
sudo apt install wget curl gnupg2 software-properties-common apt-transport-https ca-certificates lsb-release

# begin install:
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org

# check if service is running
sudo systemctl start mongod
sudo systemctl status mongod

# set mongod service to start with the system boot
sudo systemctl enable mongod
```

open mongo terminal:

```
mongosh
```

## Mongo 4.4

### Install

[Instalação ubuntu 20.04](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#import-the-public-key-used-by-the-package-management-system)

> Add repository (ubuntu 20.04):

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
```

> update and install:

```bash
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl enable mongod
```

## Import dataset

```bash
mongorestore -d dbname dir/dbname/
```

## Configuração

**Habilitar pretty print**

```bash
echo DBQuery.prototype._prettyShell = true >> ~/.mongorc.js
```

**Mostrar** mais que 20 registros no find() do shell. Editar arquivo mongorc.js e adicionar:

```bash
DBQuery.shellBatchSize = 40
```

## mongo-hacker

Melhora da interface cli: https://github.com/TylerBrock/mongo-hacker

Install:

```
git clone https://github.com/TylerBrock/mongo-hacker
cd mongo-hacker
make install
cd ..
rm -rf mongo-hacker/
```
