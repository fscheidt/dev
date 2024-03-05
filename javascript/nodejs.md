# Node.js

Commads to verify node.js installed version:

```bash
node -v
```

We need version >= 18

## Install Node

### Option 1: [Node Version Manager](https://github.com/nvm-sh/nvm)

Commands to **run**:

**(1)** Get node installer script:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
```

<u>close the terminal and open a new one.</u>

**(2)** Show available node versions:

```bash
nvm list-remote
```

**(3)** Install the latest node version:

> Last version

```bash
nvm install node
```

OR 

Install specific version:

> Gallium LTS

```bash
nvm install v16.19.0
```

> Hydrogen LTS

```bash
nvm install v18.13.0
```

**(4)** Verify which node version is installed:

```bash
node -v
```


### Option 2: Install from source

<details>
<summary>...</summary>
```bash
curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh
```

```bash
sudo bash nodesource_setup.sh
```

```bash
sudo apt install nodejs
```

```bash
node -v
npm -v
```
</details>

