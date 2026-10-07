---
slug: passar-llista
tags: [arrays, estructuras-de-datos]
---
# Passar llista

Tenim una llista d'alumnes.

Després preguntem els noms als alumnes que hi ha a classe, i hem de determinar si estan a la llista, o no, i en quina posició.

## Input

El primer nombre  indica la quantitat d'alumnes que hi ha a la llista.
Després venen els  noms de la llista.

A continuació ve una sèrie amb els noms dels alumnes que hi ha a la classe. La sèrie acaba amb `__FI__`

## Output

Per cada alumne de la classe, s'escriurà la seva posició a la llista, o la paraula `NO` si no hi és a la llista.

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
      
      	
    }
}
```

## Tests

### Test 33.33
```input
4
pepe juan luis jose
luis juan jose manolo vicente alfonso __FI__
```
```output
3
2
4
NO
NO
NO
```

### Test private 33.33
```input
7
juan adrian oriol ruben jose carlos pol
oriol ruben fernando vicente pedro __FI__
```
```output
3
4
NO
NO
NO
```

### Test private 33.34
```input
1
luis
__FI__
```
```output
```
