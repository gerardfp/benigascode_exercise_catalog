---
slug: lineseparator
tags: [class]
difficulty: 2
---
# LineSeparator

Completa el mètode main():

- Crea un objecte de la classe LineSeparator
- Estableix el tamany de la linea a partir de la dades d'entrada.

## Input

-

## Output

-

## Solutions

```java
class LineSeparator {
    int size;

    void print() {
        for (int i = 0; i < size; i++) {
            IO.print("-");
        }
        IO.println();
    }
}

void main() {
    Scanner scanner = new Scanner(System.in);
    LineSeparator lineSeparator = new LineSeparator();

    int n;
    while (scanner.hasNextInt() && (n = scanner.nextInt()) != -1) {
        IO.println("Aqui sota hi surt una line de %d guions".formatted(n));
        lineSeparator.size = n;
        lineSeparator.print();
    }
}
```

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class LineSeparator {
    int size;

    void print(){
        for (int i = 0; i < size; i++) {
            System.out.print("-");
        }
        System.out.println();
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n;
        while((n = scanner.nextInt()) != -1){
            System.out.format("Aqui sota hi surt una line de %d guions", n);
            lineSeparator.print();
        }
    }
}
```

## Tests

### Test
```input
3 5 7   -1
```
```output
Aqui sota hi surt una line de 3 guions
---
Aqui sota hi surt una line de 5 guions
-----
Aqui sota hi surt una line de 7 guions
-------
```

### Test
```input
3 5 7   -1
```
```output
Aqui sota hi surt una line de 3 guions
---
Aqui sota hi surt una line de 5 guions
-----
Aqui sota hi surt una line de 7 guions
-------
```

### Test private
```input
10 20 30   -1
```
```output
Aqui sota hi surt una line de 10 guions
----------
Aqui sota hi surt una line de 20 guions
--------------------
Aqui sota hi surt una line de 30 guions
------------------------------
```
