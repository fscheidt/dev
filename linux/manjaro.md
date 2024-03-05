# Manjaro

Comandos usados:

- **sudo**: executa comandos do linux com permissão elevada.
- **pacman**: package manager ou gerenciador de pacotes equivalente ao apt do debian.
- **makepkg**: script que automatiza o build de pacotes.
- **yay**: Yet Another Yogurt - utilitário que facilita a instalação de pacotes.

## Update

Check manjaro version:

```bash
lsb_release -drc
mhwd-kernel -li
```

Update mirrors: obtem lista de servidores mais rápidos de acordo com a localização do usuário.

```bash
sudo pacman-mirrors --fasttrack && sudo pacman -Syu
```

Atualiza o sistema:

```bash
sudo pacman -Syu
```

## Git

```bash
sudo pacman -S --needed --noconfirm base-devel git
```

## yay

Install [yay](https://github.com/Jguer/yay): aur package helper

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
Typefaces amigáveis para uso no terminal e escrever código:

```bash
yay -S nerd-fonts-complete --noconfirm
```

## vscode editor

```bash
yay -S visual-studio-code-bin
```

```bash
visual-studio-code --version
```

## zip

```bash
yay -S 7-zip --noconfirm
```

## utils

[fd](https://github.com/sharkdp/fd)

```bash
sudo pacman -S fd
```

[bat](https://github.com/sharkdp/bat)

```bash
sudo pacman -S bat 
```

[httpie](https://httpie.io)

```bash
sudo pacman -Syu httpie
```

httpie (snap):
```bash
sudo snap install httpie
```

## ghcli

```bash
sudo pacman -S github-cli
```

```bash
gh auth login
```

## snap

Habilitar suporte pacotes snap:

```bash
sudo pacman -S snapd
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
```

test:

```bash
sudo snap install btop
```

## Virtualbox

[+info](https://wiki.manjaro.org/index.php/VirtualBox)

Check kernel version:
```bash
mhwd-kernel -li
```

Install virtualbox package (according with kernel version)
```bash
sudo pacman -Syu virtualbox linux515-virtualbox-host-modules
```

Add virtualbox to the kernel, or reboot.
```bash
sudo vboxreload
```

check vb version:
```bash
vboxmanage --version
```

## Dropbox

> install via software > dropbox (flatpack)

```bash
flatpak install flathub com.dropbox.Client
```

## Apps

```bash
flatpak install flathub org.kde.okular
flatpak run org.kde.okular
```

## Mysql

```bash
pamac install mariadb
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
systemctl start mariadb
sudo mariadb-secure-installation
mysql -u root -p
```

```bash
sudo mysql_secure_installation
```

```bash
sudo mysql
```


## Mongodb

```bash

```

## Homeshick

[repo project](https://github.com/andsens/homeshick)

```bash

git clone https://github.com/andsens/homeshick.git $HOME/.homesick/repos/homeshick

# from sh (bash, dash, ksh, zsh)
printf '\nsource "$HOME/.homesick/repos/homeshick/homeshick.sh"' >> $HOME/.bashrc

```

## Docker

```bash
sudo pacman -S docker
sudo systemctl start docker.service
sudo systemctl enable docker.service
sudo docker version
# view docker container:
sudo docker info
```
