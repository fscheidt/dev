# MongoDB

## Instalação

Obter o arquivo/pacote `.deb` na [página](https://www.mongodb.com/try/download/community) da versão community edition. Alternativamente, baixar diretamente o arquivo .deb [aqui](https://repo.mongodb.org/apt/ubuntu/dists/jammy/mongodb-org/7.0/multiverse/binary-amd64/mongodb-org-server_7.0.9_amd64.deb) (para ubuntu 22.04)


```bash
sudo apt install ./mongodb-org-server_7.0.9_amd64.deb
```

### Iniciar serviço

```bash
sudo systemctl start mongod
```

```bash
sudo systemctl status mongod
```

### Habilitar serviço

Habilita o serviço `mongod` para iniciar junto com o sistema operacional

```bash
sudo systemctl enable mongod
```

---

## Comandos via terminal

### Importar uma base de dados existente

```bash
mongorestore -d dbname /path/to/dbname/
```

## Configuração mongosh

**Habilitar pretty print**

```bash
echo DBQuery.prototype._prettyShell = true >> ~/.mongorc.js
```

**Mostrar** mais que 20 registros no find() do shell. Editar arquivo mongorc.js e adicionar:

```bash
DBQuery.shellBatchSize = 40
```

## Configuração 

verificar valor atual:

```bash
sysctl -n vm.max_map_count
```

definir novo valor:

```bash
# file: /etc/sysctl.conf
vm.max_map_count=262144
```


```bash
sudo sysctl -w vm.max_map_count=262144
```

