# snap

## Clean unused packages 

Remove old snap packages sooner to free disk space:

```bash
sudo snap set system refresh.retain=2
```

*Retain default value is ***3***.* Value can be between **2** to **20**. 


- [Remove old packages script](/linux/scripts/clean_snap.sh)
