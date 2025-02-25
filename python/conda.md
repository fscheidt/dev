# Conda

Environment management

## Install

install:

```bash
sh ./Anaconda3-2023.03-Linux-x86_64.sh
```

> update:

```bash
conda update -n base conda -c anaconda 
```

## Create new Environment

```bash
conda create -n dataview python=3.10
conda activate dataview
```

> instalar dependências:

```bash
conda install -c anaconda mysql-connector-python -y
conda install -c conda-forge notebook -y
conda install -c anaconda pymongo -y
conda install pandas scikit-learn matplotlib -y
pip install wget
```
