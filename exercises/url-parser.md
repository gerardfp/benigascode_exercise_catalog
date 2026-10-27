---
slug: url-parser
difficulty: 10.0
tags: [strings, scanner, parsing]
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

![image](assets/url-parser-img0.png)

Es desitja crear una macro que prengui una URL i la descomposi en els seus components, generant codi Java amb les variables i els seus valors corresponents.

## Input

La entrada consta d'una URL amb els 8 components.

## Output

S'imprimirà el codi Java generat, que contingui una variable per a cada component de la URL, amb el seu valor assignat.

Les variables `scheme`, `user`, `password`, `host` i `fragment` son de tipus `String`

La variable `port` es de tipus `int`.

Les variables `path` i `query` son de tipus `String[]`, inicialitzats amb els seus segments.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNext()) return;
    String url = sc.next();

    // Find scheme: up to "://"
    int schemeEnd = 0;
    for (int i = 0; i <= url.length() - 3; i++) {
        if (url.charAt(i) == ':' && url.charAt(i + 1) == '/' && url.charAt(i + 2) == '/') {
            schemeEnd = i;
            break;
        }
    }
    String scheme = url.substring(0, schemeEnd);
    String afterScheme = url.substring(schemeEnd + 3);

    // Find user and password: up to '@'
    int atPos = 0;
    for (int i = 0; i < afterScheme.length(); i++) {
        if (afterScheme.charAt(i) == '@') {
            atPos = i;
            break;
        }
    }
    String userInfo = afterScheme.substring(0, atPos);
    String afterAt = afterScheme.substring(atPos + 1);

    int colonPos = 0;
    for (int i = 0; i < userInfo.length(); i++) {
        if (userInfo.charAt(i) == ':') {
            colonPos = i;
            break;
        }
    }
    String user = userInfo.substring(0, colonPos);
    String password = userInfo.substring(colonPos + 1);

    // Find fragment: after '#'
    int hashPos = afterAt.length();
    for (int i = 0; i < afterAt.length(); i++) {
        if (afterAt.charAt(i) == '#') {
            hashPos = i;
            break;
        }
    }
    String fragment = afterAt.substring(hashPos + 1);
    String beforeHash = afterAt.substring(0, hashPos);

    // Find query: after '?'
    int qPos = beforeHash.length();
    for (int i = 0; i < beforeHash.length(); i++) {
        if (beforeHash.charAt(i) == '?') {
            qPos = i;
            break;
        }
    }
    String queryString = beforeHash.substring(qPos + 1);
    String beforeQuery = beforeHash.substring(0, qPos);

    // In beforeQuery, find first '/' to separate host:port from path
    int slashPos = 0;
    for (int i = 0; i < beforeQuery.length(); i++) {
        if (beforeQuery.charAt(i) == '/') {
            slashPos = i;
            break;
        }
    }
    String hostPort = beforeQuery.substring(0, slashPos);
    String pathString = beforeQuery.substring(slashPos + 1);

    int hpColonPos = 0;
    for (int i = 0; i < hostPort.length(); i++) {
        if (hostPort.charAt(i) == ':') {
            hpColonPos = i;
            break;
        }
    }
    String host = hostPort.substring(0, hpColonPos);
    int port = Integer.parseInt(hostPort.substring(hpColonPos + 1));

    String[] pathSegments = pathString.split("/");
    String[] querySegments = queryString.split("&");

    String pathResult = "String[] path = {";
    for (int i = 0; i < pathSegments.length; i++) {
        pathResult += "\"" + pathSegments[i] + "\"";
        if (i < pathSegments.length - 1) {
            pathResult += ", ";
        }
    }
    pathResult += "};";

    String queryResult = "String[] query = {";
    for (int i = 0; i < querySegments.length; i++) {
        queryResult += "\"" + querySegments[i] + "\"";
        if (i < querySegments.length - 1) {
            queryResult += ", ";
        }
    }
    queryResult += "};";

    IO.println("String scheme = \"" + scheme + "\";");
    IO.println("String user = \"" + user + "\";");
    IO.println("String password = \"" + password + "\";");
    IO.println("String host = \"" + host + "\";");
    IO.println("int port = " + port + ";");
    IO.println(pathResult);
    IO.println(queryResult);
    IO.println("String fragment = \"" + fragment + "\";");
}
```

## Tests

### Test
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

### Test
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

### Test
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

### Test
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

### Test private
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
