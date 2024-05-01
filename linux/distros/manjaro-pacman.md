# Manjaro

Principais comandos:

- **sudo**: executa outros comandos do linux com permissão elevada
- **pacman**: package manager ou gerenciador de pacotes equivalente ao apt do debian.
- **makepkg**: script que automatiza o build de pacotes
- **yay**: Yet Another Yogurt - utilitário que facilita a instalação de pacotes

## update

Update mirrors

```bash
sudo pacman-mirrors --fasttrack && sudo pacman -Syu
```

update do sistema:

```bash
sudo pacman -Syu
```

**install git**

```bash
sudo pacman -S --needed --noconfirm base-devel git
```

**[-S]** this options allow packages be installed directly from the remote repositories, including all dependencies required to run the packages. For example, `pacman -S qt` will download and install `qt` and all the packages it depends on. 

- If a package name exists in more than one repository, the repository can be explicitly specified to clarify the package to install: `pacman -S testing/qt`
- You can also specify version requirements: `pacman -S "bash>=3.2"`. Quotes are needed, otherwise the shell interprets ">" as redirection to a file.


## mirrors

CHECK

```bash
pacman-mirrors --status
```

update mirrors

GET fast

```bash
sudo pacman-mirrors --fasttrack && sudo pacman -Syu
```

GET by country
```bash
sudo pacman-mirrors --geoip && sudo pacman -Syu
```

RESET to default

```bash
sudo pacman-mirrors --country all --api --protocols all --set-branch stable && sudo pacman -Syu
```

## yay

INSTALL [yay](https://github.com/Jguer/yay) AUR helper

```bash
git clone https://aur.archlinux.org/yay-git.git
```

```bash
sudo mv yay-git /opt/ && cd /opt/yay-git
```

```bash
makepkg -si
```

## nerd-fonts

INSTALL

```bash
yay -S nerd-fonts-complete --noconfirm
```

UPDATE

```bash
yay -Syu --devel --timeupdate
```

REMOVE

```bash
yay -Rns nerd-fonts-complete --noconfirm
```

CLEAN UP

```bash
yay -Yc
```

## VScode

INSTALL

```bash
yay -S visual-studio-code-bin
```

```bash
visual-studio-code --version
```

## Utils

ZIP

```bash
yay -S 7-zip --noconfirm
```

GH CLI

```bash
sudo pacman -S github-cli
```

```bash
gh auth login
```

## Snap support

Habilitar suporte ao snap:

```bash
sudo pacman -S snapd
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap

# test:
sudo snap install btop
```

## Virtualbox

Install guest additions:

```bash
pacman -Q | grep headers
```


```bash
sudo pacman -S linux-headers
```


```bash
sudo ./VBoxLinuxAdditions.run
```
