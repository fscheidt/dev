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
