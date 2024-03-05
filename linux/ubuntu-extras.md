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

- [bat](https://github.com/sharkdp/bat/releases/latest)
  - `sudo apt install ./bat_0.xx.amd64.deb`
- [fd](https://github.com/sharkdp/fd/releases/latest)
- [btop](https://github.com/aristocratos/btop)

> fzf

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
sudo apt install httpie
```

## Snap

```bash
sudo snap install drawing
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

```bash
sudo apt install ./tilix_1.9.4-2build1_amd64.deb --fix-broken
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
sudo apt install ./virtualbox-6.1_6.1.38-153438_Ubuntu_jammy_amd64.deb --fix-broken
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


## Timeshift

version: 24.01

- https://github.com/linuxmint/timeshift
- [build howto](https://github.com/linuxmint/timeshift/blob/master/docs/development.md)

### Btrfs

```bash
sudo apt install btrfs-progs
```

### Build

```bash
sudo apt install meson \
help2man \
gettext \
valac \
libvte-2.91-dev \
libgee-0.8-dev \
libjson-glib-dev \
libxapp-dev
```

```bash
git clone https://github.com/linuxmint/timeshift.git
```

```bash
cd timeshift
```

```bash
meson setup build
```

```bash
meson compile -C build 
```

```bash
sudo meson install -C build
```

```bash
sudo timeshift-gtk
```

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
