# Node.js

Commads to verify node.js installed version:

```bash
node -v
```

We need version >= 22

## Install Node

### Option 1: [Node Version Manager](https://github.com/nvm-sh/nvm)

Commands to **run**:

**(1)** Get node installer script:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```

<u>close the terminal and open a new one.</u>

**(2)** Show available node versions:

```bash
nvm list-remote
```

**(3)** Install the **latest** node version:

> Last version

```bash
nvm install node
```

OR 

Install **specific** version:

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

- https://github.com/nodesource/distributions

> Node v20.x

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - &&\
sudo apt-get install -y nodejs
```

```bash
node -v
npm -v
```

</details>

