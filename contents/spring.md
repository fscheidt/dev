# Spring framework

## Configurações

### `application.properties`

H2 database config:

```properties
server.port=8080
spring.h2.console.enabled=true
spring.h2.console.path=/h2admin
spring.jpa.show-sql=true
spring.thymeleaf.cache=false
spring.datasource.url=jdbc:h2:file:~/h2files/namedb;DB_CLOSE_ON_EXIT=FALSE;AUTO_RECONNECT=TRUE
spring.datasource.username=admin
spring.datasource.password=1234
spring.datasource.driver-class-name=org.h2.Driver

#spring.jpa.hibernate.ddl-auto=update
spring.jpa.hibernate.ddl-auto=create-drop
#spring.jpa.hibernate.ddl-auto=create
```
