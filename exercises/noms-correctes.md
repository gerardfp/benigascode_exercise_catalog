---
slug: noms-correctes
difficulty: 1.0
tags: [variables, types]
---
# Noms correctes

Dona el nom que li pertoca a cada variable.

## Input

-

## Output

-

## Solutions

```java
void main() {
    String feature = "Text Blocks";
    String language = "Java";
    char quote = '"';
    int version = 15;

    IO.println(language + " " + version + " incorpora " + feature + ", que es delimiten amb " + quote + quote + quote);
}
```

## Plantillas

```java
public class Main {

    public static void main(String[] args) {
      String  = "Text Blocks";
      String  = "Java";
      char    = '"';
      int     = 15;
      
      System.out.println(language + " " + version + " incorpora " + feature + ", que es delimiten amb " + quote + quote + quote);
    }
}
```

## Tests

### Test
```input
```
```output
Java 15 incorpora Text Blocks, que es delimiten amb """
```
