---
slug: uri-scheme
difficulty: 3.0
tags: [strings, class, parsing]
---
# URI Scheme

Completa la classe `URL`, i el mètode `main()`

## Input

La entrada consta de 5 línies:

- protocol
- domain
- path
- query
- fragment

## Output

S'imprimirà la URL ben formada.

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class URL {
    String protocol;
    String domain;
    String path;
    String query;
    String fragment;

	// escriu codi aqui
}

public class E11 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
	    URL url = new URL();

	    // escriu codi aqui

        System.out.println(url);
    }
}
```

## Solutions

```java
class URL {
    String protocol;
    String domain;
    String path;
    String query;
    String fragment;

    @Override
    public String toString() {
        return protocol + "://" + domain + path + "?" + query + "#" + fragment;
    }
}

void main() {
    Scanner scanner = new Scanner(System.in);
    URL url = new URL();
    url.protocol = scanner.nextLine();
    url.domain = scanner.nextLine();
    url.path = scanner.nextLine();
    url.query = scanner.nextLine();
    url.fragment = scanner.nextLine();
    IO.println(url);
}
```

## Tests

### Test
```input
http
www.mydomain.com
/path/to
query=true
fragment1
```
```output
http://www.mydomain.com/path/to?query=true#fragment1
```

### Test
```input
http
www.mydomain.com
/path/to
query=true
fragment1
```
```output
http://www.mydomain.com/path/to?query=true#fragment1
```

### Test
```input
https
anotherdomain.cat
/path/to/page
q=1&s=1
frag
```
```output
https://anotherdomain.cat/path/to/page?q=1&s=1#frag
```

### Test private
```input
https
domainname.org
/document
t=www&s=1
new
```
```output
https://domainname.org/document?t=www&s=1#new
```
