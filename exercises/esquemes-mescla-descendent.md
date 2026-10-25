---
slug: esquemes-mescla-descendent
difficulty: 4.0
tags: [arrays, loops, while-loop, merge, two-pointers]
---
# Mescla: fusió en ordre descendent

Donats dos arrays d'enters ordenats en **ordre descendent** (de major a menor) de mides $N$ i $M$, fusiona'ls en un únic array ordenat en ordre descendent utilitzant l'esquema de mescla en temps lineal $O(N+M)$.

## Entrada

A la primera línia hi ha la mida $N$ del primer array, seguida dels seus $N$ enters en ordre descendent.

A continuació hi ha la mida $M$ del segon array, seguida dels seus $M$ enters en ordre descendent.

## Salida

Imprimeix els $N+M$ elements fusionats en ordre descendent en una sola línia, separats per espais.

## Tests

### Test
```input
3
50
30
10
3
60
40
20
```
```output
60 50 40 30 20 10
```

### Test
```input
2
20
10
3
25
15
5
```
```output
25 20 15 10 5
```

### Test
```input
1
5
1
7
```
```output
7 5
```

### Test
```input
2
8
4
2
9
3
```
```output
9 8 4 3
```
