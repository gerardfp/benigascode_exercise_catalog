---
slug: sumas-encadenadas
tags: [strings]
---
# Sumas encadenadas

Dada una secuencia de números, cuenta la cantidad de sumas encadenadas que hay.

Una suma encadenada cuando hay tres números consecutivos, de forma que la suma de los dos primeros es igual al tercero.

## Input

Una secuencia de N números terminados en un 0.

3 <= N <= 1000

## Output

Un número indicando la cantidad de sumas encadenadas.

## Tests

### Test
```input
1 2 3 10 11 21 22 0
```
```output
2
```

### Test
```input
10 10 20 30    0
```
```output
2
```

### Test
```input
4 0 4 4 2 6 8    0
```
```output
4
```

### Test
```input
3 6 9 1 1 2 3 5 8 4    0
```
```output
5
```

### Test
```input
1 1 1   0
```
```output
0
```

### Test
```input
8 8 2 0 0 9 0 1 5 7    0
```
```output
0
```

### Test
```input
1 1 2   0
```
```output
1
```

### Test
```input
5 6 1 7 2 0 7 2 4 1 9 8 4 5 9 9 0 2 1 3 4 7 9 8 1 3 4 7 2 4 6 2 2 4 4 8 9 9 0 6 1 6 1 6 6 3 8 5 9 7 2 4 4 0 0 3 0 9 9 5 1 7 1 1 6 8 4 6 0 8 4 8 6 3 2 7 3 9 4 7 0 1 1 5 4 2 0 2 5 7 3 3 0 5 5 7 7 0 3    0
```
```output
15
```
