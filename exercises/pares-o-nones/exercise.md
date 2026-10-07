---
slug: pares-o-nones
tags: [ternari]
---
# Pares o nones

Dos amics juguen al pares o nones. Ú diu *pares*, i l'altre *nones*, i després trauen els dits. Digues qui guanya!

## Input

l'entrada consta de 4 dades:
- una paraula amb que diu el primer jugador
- un número amb els dits que trau el primer jugador
- una paraula amb el que diu el segon jugador
- un número amb els dits que trau el segon jugador

## Output

S'imprimirà el jugador que guanya: `primer jugador` | `segon jugador`

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Main {
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    }
}
```

## Tests

### Test
```input
pares 4
nones 1
```
```output
segon jugador
```

### Test
```input
nones 4
pares 1
```
```output
primer jugador
```

### Test
```input
pares 3
nones 3
```
```output
primer jugador
```

### Test
```input
nones 3
pares 3
```
```output
segon jugador
```

### Test private
```input
pares 3
nones 2
```
```output
segon jugador
```
