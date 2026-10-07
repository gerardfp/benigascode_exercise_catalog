---
slug: cuantas-veces-aparece-cada-numero
tags: [arrays]
---
# Cuantas veces aparece cada número

Dada una serie de números, cuenta cuántas veces aparece cada número.


-- TIP:

Determina cuál es el número más grande de la secuencia.
Almacena en un array cuántas veces aparece cada número.

## Entrada

* Un número `N` que indica la cantidad de números
* La secuencia de `N` números

## Salida

Se imprimirá en una línea cada `número` de la secuencia y `cuántas` veces aparece, separados por `:`

Los `números` se deben imprimir ordenados de menor a mayor.

## Plantillas

```java
public class Solution {
    public static void main(String[] args) {
        // Tu código aquí
    }
}
```

## Tests

### Test
```input
5
0 0 1 1 1
```
```output
0:2
1:3
```

### Test
```input
6
1 2 2 2 2 1
```
```output
1:2
2:4
```

### Test
```input
1
56
```
```output
56:1
```

### Test
```input
3
1000000 1000000 1000000
```
```output
1000000:3
```

### Test
```input
20
12 17 12 24 27 28 28 21 18 17 22 29 12 11 21 18 13 16 23 15 
```
```output
11:1
12:3
13:1
15:1
16:1
17:2
18:2
21:2
22:1
23:1
24:1
27:1
28:2
29:1
```

### Test
```input
20
100002 100002 100002 100003 100001 100002 100001 100003 100002 100004 100003 100000 100001 100004 100003 100004 100000 100000 100002 100004 100003 100000 100000 100000 100004 100000 100004 100002 100002 100003 100003 100001 100004 100004 100002 100002 100000 100000 100000 100002 100003 100000 100002 100002 100004 100001 100003 100004 100000 100002
```
```output
100000:3
100001:3
100002:6
100003:4
100004:4
```

### Test
```input
5
0 -1 0 -1 0
```
```output
-1:2
0:3
```

### Test private
```input
3
1 2 2
```
```output
1:1
2:2
```
