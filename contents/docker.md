# Docker

- [ubuntu install](https://docs.docker.com/engine/install/ubuntu/)

## Instalação (Ubuntu)

### Adicionar chave GPG do docker

Adicionar certificado do docker para o ubuntu:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Adicionar repositório do docker na lista de fontes do apt:

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

### Instalar docker e plugins

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Verificar versões

```bash
docker compose version
docker --version
docker version
```

### Testar instalação

Verificar se o docker foi instalado corretamente executando o container "hello-world":

```bash

sudo docker run hello-world

```


### Inicialização do serviço

Configura a inicialização do serviço docker junto com o boot do SO:

```bash

sudo systemctl enable docker.service
sudo systemctl enable containerd.service

```

Desabilita a inicialização:

```bash

sudo systemctl disable docker.service
sudo systemctl disable containerd.service

```

## Containers 

### Flutter

Instala o container [SDK](https://hub.docker.com/r/mobiledevops/flutter-sdk-image) para desenvolvimento com Flutter.

```bash
sudo docker pull mobiledevops/flutter-sdk-image
```

## Comandos

- Exibe containers locais disponíveis?

```bash
sudo docker images
```
