# Go lang

## Install

Download binary `go1.20.2.linux-amd64.tar.gz` from [go.dev](https://go.dev/doc/install)

```bash
sudo tar -C /usr/local -xzf go1.20.2.linux-amd64.tar.gz
```

## Adicionar path

```bash
sudo vi /etc/profile
```

`export PATH=$PATH:/usr/local/go/bin`

## Utilities

### Markdown viewer

```bash
go install github.com/charmbracelet/glow@latest
```
