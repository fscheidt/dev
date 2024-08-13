# Ubuntu Extra tools


## nvidia drivers

this is optional, run only if ubuntu doesn't recognize our gpu card:

```bash
# check drivers and gpu model
ubuntu-drivers devices

# install (option 1):
sudo ubuntu-drivers autoinstall

# install (option 2):
# sudo apt install nvidia-driver-515

sudo reboot

# test if nvidia-settings is installed:
nvidia-settings
```


## Utilities

```bash
sudo apt install htop
```

```bash
sudo apt install silversearcher-ag jq sqlite3
```

```bash
sudo apt install neofetch
```

```bash
sudo apt install xsel xclip -y;
```

```bash
sudo apt install dconf-editor -y;
```

```bash
sudo apt install gnome-tweaks -y;
```

```bash
sudo apt-get install ripgrep pdfgrep -y
```

> [fuse](https://docs.appimage.org/user-guide/troubleshooting/fuse.html) (to run appimage files)

```bash
sudo apt install libfuse2
```


## Essential

### [bat](https://github.com/sharkdp/bat)

```bash
cargo install --locked bat
```


### [fd](https://github.com/sharkdp/fd)

```bash
cargo install fd-find
```

### [btop](https://github.com/aristocratos/btop)

```bash
sudo snap install btop --edge
or
sudo snap install btop-desktop --edge
```

### fzf

```bash
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

> network

```bash
sudo apt-get install net-tools -y
```

```bash
sudo apt-get install openssh-server -y
```

```bash
sudo systemctl enable ssh; sudo systemctl start ssh
```

> api tools

```bash
sudo apt install httpie -y
```

## Snap

```bash
sudo snap install drawing
```

```bash
sudo snap install okular
```


## Other tools

### Markdown

> glow

```bash
go install github.com/charmbracelet/glow@latest
```

> docs helper

```bash
npm install -g tldr
```

### GH 

- github cli [➥](https://cli.github.com/)


### Tilix

Ubuntu versions install file:
- 20.04 - https://packages.ubuntu.com/focal/tilix
- 22.04 - https://packages.ubuntu.com/jammy/tilix 
    - v1.9.4-2 [deb file](http://ubuntu.c3sl.ufpr.br/ubuntu/pool/universe/t/tilix/tilix_1.9.4-2build1_amd64.deb)
- 24.04 - https://packages.ubuntu.com/noble/amd64/tilix/download
    - [v1.9.6-2build1_amd64.deb](http://mirrors.kernel.org/ubuntu/pool/universe/t/tilix/tilix_1.9.6-2build1_amd64.deb)

```bash
sudo apt install ./tilix_1.9.4-2build1_amd64.deb
```

```bash
# sudo apt install ./tilix_1.9.4-2build1_amd64.deb --fix-broken
```

## Databases

- [mongodb](/contents/mongodb.md)
- [mysql](/contents/mysql.md)


## Hardware info

> [cpu-x](https://github.com/TheTumultuousUnicornOfDarkness/CPU-X)

```bash
sudo apt install lm-sensors cpu-x
```

## Flatpack

```bash
sudo apt install flatpak
```

## Virtualbox

- [download linux distros](https://www.virtualbox.org/wiki/Linux_Downloads)

```bash
sudo apt install ./virtualbox-7.0_7.0.16-162802~Ubuntu~jammy_amd64.deb --fix-broken
```

## Dotfiles

- [homeshick](https://github.com/andsens/homeshick)


## Dropbox

> Fix for: "dropbox can't sync"

```bash
sudo gedit /etc/sysctl.conf
fs.inotify.max_user_watches=500000
```

reboot..., or skip with:

```bash
sudo sysctl fs.inotify.max_user_watches=500000  
sudo sysctl -p
```

## [Timeshift](/linux/utils/timeshift.md)

### Apt

```bash
sudo apt-get update
sudo apt-get install timeshift
```

## Grub customizer

```bash
sudo add-apt-repository ppa:danielrichter2007/grub-customizer
sudo apt-get update
sudo apt-get install grub-customizer
```


## Boot-repair

```bash
sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt update
sudo apt install -y boot-repair && boot-repair
```
