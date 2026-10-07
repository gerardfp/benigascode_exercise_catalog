---
slug: notacio-vectorial
tags: [arrays, estructuras-de-datos]
---
# Notació arrays

En Java els arrays es poden inicialitzar amb la següent notació:

```text
tipus[] identificador = { valor0, valor1, valor2, ..., valorN };
```

Escriu un programa que generi el codi d'inicialització d'un array a partir de les dades d'entrada.

El tipus de dades de l'entrada sempre és `int`, i l'identificador de l'array ha de ser `myArray`.

## Input

El primer número  indica la quantitat de nombres que venen a continuació.

Després venen els  nombres separats per espais en blanc.

> 0

## Output

S'imprimirà la declaració de l'array en el format indicat i en una sola línia.

## Tests

### Test 20
```input
5
11 13 17 19 23
```
```output
int[] myArray = { 11, 13, 17, 19, 23 };
```

### Test 20
```input
3
100 200 300
```
```output
int[] myArray = { 100, 200, 300 };
```

### Test private 20
```input
10
23 76 12 54 98 65 67 39 91 83
```
```output
int[] myArray = { 23, 76, 12, 54, 98, 65, 67, 39, 91, 83 };
```

### Test private 20
```input
1
67
```
```output
int[] myArray = { 67 };
```

### Test private 20
```input
9
11 22 33 44 55 66 77 88 99
```
```output
int[] myArray = { 11, 22, 33, 44, 55, 66, 77, 88, 99 };
```
