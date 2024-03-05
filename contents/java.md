# Java (jdk) install

Install with sdkman

- [sdkman](https://sdkman.io/)

```bash
curl -s "https://get.sdkman.io" | bash
```

Install java 11:

```bash
sdk i java 11.0.9-zulu
```

Java 17:

```bash
sdk i java 17.0.5-zulu
```

## Maven

- Download maven binaries: https://maven.apache.org/download.cgi
- unzip and move to /opt/maven

add to `.profile`

```bash
M2_HOME='/opt/maven'
PATH="$M2_HOME/bin:$PATH"
export PATH
```