---
slug: media-truncada
tags: [matemáticas, algorithms]
---
# Media truncada

![image](1613471174-9deed84a32-judges-300x200.jpg)

El método de puntuación utilizado en muchos deportes que son evaluados por un panel de jueces es una media truncada: descartar la puntuación más baja y más alta, y calcular el valor medio de las puntuaciones restantes.

## Input

El primer numero  indica la cantidad de puntuaciones.

A continuación vienen las  puntuaciones (float)

## Output

Se imprimirà la puntuación truncada media

## Plantillas

```java
import java.util.Locale;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.ENGLISH);
    	
      	
    }
}
```

## Tests

### Test
```input
5
10 9 8 7 5
```
```output
8.0
```

### Test
```input
3
9 8 6
```
```output
8.0
```

### Test
```input
4
10 10 0 5 
```
```output
7.5
```

### Test
```input
5
10 10 5 0 0
```
```output
5.0
```

### Test
```input
7
4.7 5.3 7.2 3.1 8.2 7.9 5.6
```
```output
6.14
```
