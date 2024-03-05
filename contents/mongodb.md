# MongoDB


### Habilitar serviço

```bash
# check if service is running
sudo systemctl start mongod
sudo systemctl status mongod

# set mongod service to start with the system boot
sudo systemctl enable mongod
```

## Import dataset

```bash
mongorestore -d dbname dir/dbname/
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
