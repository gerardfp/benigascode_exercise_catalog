---
slug: dintre-de-termini
---
# Dintre de termini

Donades tres dates, digues si la segona és posterior a la primera i anterior a la tercera.

## Input

L'entrada consisteix en tres dates en format `dd / mm / yyyy`.

Les tres dates són distintes.

## Output

S'imprimirà `true` si la segona data és posterior a la primera i anterior a la tercera, i `false` en cas contrari.

**Suggerència per a la solució**

Cal llegir el dia, mes i any de cada data amb `nextInt()`. S'hauràn de descartar les barres `/` amb `next()`.

Una possible idea per a la solució és presuposar que la segona data està enmig, i després veure si es compleix alguna condició que impliqui que realment no està enmig.

```text
// suposem que està enmig
boolean enmig = true;

// mirem si hi ha alguna condició
// que contradigui la presuposició incial
if (any1 > any2) {
    enmig = false;
} else if (any2 > any3) {
    enmig = false;
}
// resta de condicions

// imprimim el resultat
System.out.println(enmig);
```

## Plantillas

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
      	Scanner scanner = new Scanner(System.in);
      
      
    }
}
```

## Tests

### Test
```input
7 / 1 / 1999      17 / 10 / 2050      7 / 1 / 2020
```
```output
false
```

### Test
```input
7 / 1 / 1999      7 / 1 / 2020      7 / 1 / 2050
```
```output
true
```

### Test
```input
7 / 1 / 1999      7 / 10 / 2020      17 / 1 / 2020
```
```output
false
```

### Test
```input
7 / 1 / 1999      7 / 12 / 1999      7 / 1 / 2020
```
```output
true
```

### Test
```input
7 / 1 / 1999      17 / 1 / 2050      27 / 1 / 2020
```
```output
false
```

### Test
```input
7 / 1 / 1999      17 / 12 / 2020      17 / 1 / 1999
```
```output
false
```

### Test
```input
7 / 1 / 1999      27 / 10 / 1999      17 / 10 / 2020
```
```output
true
```

### Test
```input
7 / 1 / 2020      7 / 1 / 1999      17 / 1 / 2020
```
```output
false
```

### Test
```input
7 / 1 / 2020      17 / 1 / 2020      7 / 1 / 2050
```
```output
true
```

### Test
```input
7 / 1 / 2020      27 / 1 / 2050      17 / 10 / 1999
```
```output
false
```

### Test
```input
7 / 1 / 2050      7 / 12 / 2050      27 / 12 / 2050
```
```output
true
```

### Test
```input
7 / 1 / 2050      27 / 10 / 2050      17 / 10 / 2020
```
```output
false
```

### Test
```input
7 / 10 / 2020      7 / 12 / 2020      7 / 1 / 2050 
```
```output
true
```

### Test
```input
7 / 10 / 2050      17 / 10 / 2020      7 / 1 / 2050 
```
```output
false
```

### Test
```input
7 / 12 / 2020      17 / 10 / 2050      7 / 12 / 2050 
```
```output
true
```

### Test
```input
17 / 1 / 1999      27 / 10 / 2050      7 / 1 / 1999 
```
```output
false
```

### Test
```input
17 / 10 / 1999      7 / 1 / 2020      7 / 1 / 2050 
```
```output
true
```

### Test
```input
17 / 10 / 2020      27 / 1 / 1999      17 / 10 / 1999 
```
```output
false
```

### Test
```input
17 / 10 / 2050      27 / 10 / 2050      17 / 12 / 2050 
```
```output
true
```

### Test
```input
17 / 12 / 2020      7 / 12 / 2020      27 / 10 / 1999 
```
```output
false
```

### Test
```input
27 / 1 / 1999      7 / 1 / 2020      7 / 1 / 2050 
```
```output
true
```

### Test
```input
27 / 1 / 2020      7 / 12 / 2050      7 / 1 / 1999 
```
```output
false
```

### Test
```input
27 / 10 / 1999      7 / 1 / 2020      7 / 1 / 2050 
```
```output
true
```

### Test
```input
27 / 10 / 1999      27 / 10 / 2020      17 / 12 / 1999 
```
```output
false
```

### Test
```input
27 / 12 / 1999      7 / 1 / 2020      7 / 1 / 2050 
```
```output
true
```

### Test
```input
27 / 12 / 1999      27 / 10 / 2020      7 / 1 / 2020 
```
```output
false
```

### Test
```input
27 / 12 / 2020      7 / 1 / 2050      7 / 10 / 2050 
```
```output
true
```

### Test
```input
27 / 12 / 2020      27 / 10 / 2050      7 / 12 / 2020 
```
```output
false
```
