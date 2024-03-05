# DD

## Dump partition to image file

Command:

```bash
dd if=/dev/hda1 of=./part1.image
```

Example:

```bash
# raw
dd if=/dev/nvme0n1p5 of=./ubuntu2204.image

# compressed
sudo dd if=/dev/nvme0n1p5 bs=32M conv=sparse | gzip -c > ./ubuntu2204.image.gz
```

## Restore partition from image file

```bash
gzip -cd < ./ubuntu2204.image.gz | dd of=/dev/nvme0n1p5 bs=32M
```

# Partclone

- https://github.com/Thomas-Tsai/partclone

Partition to image:
```bash
partclone.ext4 -d -c -s /dev/nvme0n1p5 -o nvme0n1p5.img
```


Restore partition:
```bash
partclone.ext4 -d -r -s nvme0n1p5.img -o /dev/nvme0n1p5
```
