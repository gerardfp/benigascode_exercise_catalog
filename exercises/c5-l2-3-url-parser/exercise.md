---
slug: c5-l2-3-url-parser
tags: [condicionales, control-de-flujo]
---
# URL parser

Una URL consisteix en 8 components:

- scheme

- user

- password

- host

- port

- path

- query

- fragment

Excepte scheme i path, la resta són opcionals.

Un exemple d'una URL completa amb els 8 components, podria ser aquest:

![image](1556921749-f057ec7687-url1.png)

Es desitja crear una macro que prengui una URL i la descomposi en els seus components, generant codi Java amb les variables i els seus valors corresponents.

## Input

La entrada consta d'una URL amb els 8 components.

El format de la URL és vàlid.

## Output

S'imprimirà el codi Java generat, que contingui una variable per a cada component de la URL, amb el seu valor assignat.

Les variables , , ,  i  són de tipus String.

La variable  es de tipus int.

Les variables  i  són de tipus String[], inicialitzats amb els seus segments.

## Tests

### Test 20
```input
http://user:pass@example.com:3000/docs/api/index.php?version=7&lang=java#strings
```
```output
String scheme = "http";
String user = "user";
String password = "pass";
String host = "example.com";
int port = 3000;
String[] path = {"docs", "api", "index.php"};
String[] query = {"version=7", "lang=java"};
String fragment = "strings";
```

### Test 20
```input
http://user:pass@example.com:3000/docs/api/index.php?version=7&lang=java#strings
```
```output
String scheme = "http";
String user = "user";
String password = "pass";
String host = "example.com";
int port = 3000;
String[] path = {"docs", "api", "index.php"};
String[] query = {"version=7", "lang=java"};
String fragment = "strings";
```

### Test private 20
```input
http://richard:stallman@www.gnu.org:80/philosophy/free-sw.html?r=1.663#history
```
```output
String scheme = "http";
String user = "richard";
String password = "stallman";
String host = "www.gnu.org";
int port = 80;
String[] path = {"philosophy", "free-sw.html"};
String[] query = {"r=1.663"};
String fragment = "history";
```

### Test private 20
```input
https://linus:torvalds@git-scm.com:8080/downloads/linux?v=2.21&dev=true#arch
```
```output
String scheme = "https";
String user = "linus";
String password = "torvalds";
String host = "git-scm.com";
int port = 8080;
String[] path = {"downloads", "linux"};
String[] query = {"v=2.21", "dev=true"};
String fragment = "arch";
```

### Test private 20
```input
https://linus:torvalds@git-scm.com:8080/downloads/gnu/linux?v=2.21&dev=true#arch
```
```output
String scheme = "https";
String user = "linus";
String password = "torvalds";
String host = "git-scm.com";
int port = 8080;
String[] path = {"downloads", "gnu", "linux"};
String[] query = {"v=2.21", "dev=true"};
String fragment = "arch";
```
