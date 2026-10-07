---
slug: hora-dapertura-operadors-ternari
tags: [operadors, ternari]
---
# Hora d'apertura

Un local té horaris d'apertura diferents entre setmana i el cap de setmana.

Entre setmana obri a les 8:00, y els cap de setmana a les 10:00.

## Input

L'entrada és un dia de la setmana.

## Output

`8:00` | `10:00`

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

### Test
```input
Dilluns
```
```output
8:00
```

### Test
```input
Dimarts
```
```output
8:00
```

### Test
```input
Dimecres
```
```output
8:00
```

### Test
```input
Dijous
```
```output
8:00
```

### Test
```input
Divendres
```
```output
8:00
```

### Test
```input
Dissabte
```
```output
10:00
```

### Test private
```input
Diumenge
```
```output
10:00
```
