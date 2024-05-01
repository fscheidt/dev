# Setup ubuntu virtual machine

Check SO and kernel version:

```bash
lsb_release -drc && uname -r
```

## Update the system

```bash
sudo apt-get update && sudo apt-get upgrade -y
```

```bash
sudo apt install build-essential dkms linux-headers-$(uname -r)
```

**reboot**

## Install guess additions (optional)

- Guess Additons (GA) provide extra functionalities, but is optional.

`Devices -> Insert guess addition CD`

```bash
cd /media/user/VBox_GAs_7.x/
sudo ./VBoxLinuxAdditions.run
```

**reboot**

### Checks additions was installed:

```bash
lsmod | grep vboxguest
```

## Ubuntu packages

Recommended packages to install

```bash
sudo apt install vim curl git rar unrar p7zip-full p7zip-rar attr -y
```

Install python utilities
```bash
sudo apt-get install python3-pip python3-venv python3-gpg -y
```
