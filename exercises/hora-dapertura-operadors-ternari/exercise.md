---
slug: hora-dapertura-operadors-ternari
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

### Test 14.29
```input
Dilluns
```
```output
8:00
```

### Test 14.29
```input
Dimarts
```
```output
8:00
```

### Test private 14.29
```input
Dimecres
```
```output
8:00
```

### Test private 14.29
```input
Dijous
```
```output
8:00
```

### Test private 14.29
```input
Divendres
```
```output
8:00
```

### Test private 14.29
```input
Dissabte
```
```output
10:00
```

### Test private 14.26
```input
Diumenge
```
```output
10:00
```
