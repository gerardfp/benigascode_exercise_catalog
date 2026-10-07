---
slug: rota-el-vector-en-el-elemento-k
tags: [arrays, estructuras-de-datos]
---
# Rota el vector en el elemento k

Dado un vector de enteros y un elemento k rotar el vector para que el elemento en el la posición k sea el primer elemento del nuevo vector.

La entrada consiste en un número que indica el tamaño del vector (N), a continuación en la siguiente línea vienen todos los elementos del vector y en la última línea el elemento k.

El elemento k está comprendido entre 0 y N-1 (siendo N el tamaño del vector).

10

1 2 3 4 5 6 7 8 9 10

1

- Un vector de 10 elementos.
- Los elementos del vector son 1 2 3 4 5 6 7 8 9 10
- El elemento k es 1

Con la siguiente entrada deberíamos rotar el vector de tal manera que el elemento en la posición 1 (el número 2) esté en la primera posición.

Esta sería la salida para el caso del ejemplo:

2 3 4 5 6 7 8 9 10 1

## Input

1 2 3 4 5 6 7 8 9 10

El formato de entrada SIEMPRE será correcto.

El elemento k está comprendido entre 0 y N-1 (siendo N el tamaño del vector).

## Output

2 3 4 5 6 7 8 9 10 1

## Tests

### Test
```input
10
1 2 3 4 5 6 7 8 9 10
1
```
```output
2 3 4 5 6 7 8 9 10 1
```

### Test
```input
5
10 20 30 40 50
3
```
```output
40 50 10 20 30
```

### Test
```input
4
1 2 3 4
0
```
```output
1 2 3 4
```

### Test
```input
3
5 6 7
2
```
```output
7 5 6
```
