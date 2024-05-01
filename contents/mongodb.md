# MongoDB

## Instalação

Obter o arquivo/pacote `.deb` na [página](https://www.mongodb.com/try/download/community) da versão community edition. Alternativamente, baixar diretamente o arquivo .deb [aqui](https://repo.mongodb.org/apt/ubuntu/dists/jammy/mongodb-org/7.0/multiverse/binary-amd64/mongodb-org-server_7.0.9_amd64.deb) (para ubuntu 22.04)


```bash
sudo apt install ./mongodb-org-server_7.0.9_amd64.deb
```

### Serviço

Iniciar serviço

```bash
sudo systemctl start mongod
```

Verificar status:

```bash
sudo systemctl status mongod
```

Habilitar o serviço `mongod` para iniciar junto com o sistema operacional

```bash
sudo systemctl enable mongod
```

Opcional: Suporte ao sistema de arquivos [XFS](/linux/utils/xfs.md)

---


## Configurações

### mongod.conf

```
# mongod.conf
# for documentation of all options, see:
#   http://docs.mongodb.org/manual/reference/configuration-options/
# Where and how to store data.
storage:
  dbPath: /var/lib/mongodb
#  engine:
#  wiredTiger:
# where to write logging data.
systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongod.log
```

### Performance

**max_map_count**

```bash
# verifica valor atual
sysctl -n vm.max_map_count
```

Editar `/etc/sysctl.conf` e definir o novo valor:

```bash
vm.max_map_count=262144
```

Definir o valor para a sessão atual:

```bash
sudo sysctl -w vm.max_map_count=262144
```


### Mongosh

Editar o arquivo `~/.mongorc.js`

**Habilitar pretty print**

```bash
echo DBQuery.prototype._prettyShell = true >> ~/.mongorc.js
```

**Mostrar** mais que 20 registros no find() do shell. Editar arquivo mongorc.js e adicionar:

```bash
DBQuery.shellBatchSize = 40
```


## Comandos 

### Importar base de dados existente

```bash
mongorestore -d dbname /path/to/dbname/
```

onde `dbname` é o nome do banco de dados, e o segundo parâmetro é a pasta onde estão os arquivos `.bson`

