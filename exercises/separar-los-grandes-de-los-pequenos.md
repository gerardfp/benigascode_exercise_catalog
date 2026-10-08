---
slug: separar-los-grandes-de-los-pequenos
tags: [condicionales, control-de-flujo]
---
# Separar los grandes de los pequeños

Dada un secuencia de números y un valor límite, separar la secuencia en dos secuencias: en la primera los valores inferiores o iguales al límite, y en la segunda los superiores al límite.

## Input

El primer número N indica el tamaño de la secuencia. A continuación viene la secuencia.

Después viene el valor límite.

1 <= N <= 100

## Output

Las dos secuencias separadas por un salto de línea.

## Tests

### Test
```input
3   1 2 3
2
```
```output
1 2
3
```

### Test
```input
5    100 300 400 200 500
300
```
```output
100 300 200
400 500
```

### Test
```input
5    34 56 78 45 12
50
```
```output
34 45 12
56 78
```

### Test
```input
3    67 78 89
10
```
```output
67 78 89
```

### Test
```input
3    67 78 89
100
```
```output
67 78 89
```

### Test
```input
5    3 1 4 2 5
1
```
```output
1
3 4 2 5
```

### Test
```input
10    12 12 13 18 19 15 16 20 17 18
17
```
```output
12 12 13 15 16 17
18 19 20 18
```
