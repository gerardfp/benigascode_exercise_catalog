---
slug: esquemes-mescla-interseccio
difficulty: 4.0
tags: [arrays, loops, while-loop, merge, two-pointers, search]
---
# Mescla: intersecció de dos arrays ordenats

Donats dos arrays d'enters ordenats en ordre creixent de mides $N$ i $M$, troba els elements comuns que pertanyen a ambdós arrays (intersecció) aprofitant que ja estan ordenats mitjançant l'esquema de dos punters en un únic recorregut $O(N+M)$. Cada valor comú ha d'aparèixer una sola vegada.

## Entrada

A la primera línia hi ha la mida $N$ del primer array, seguida dels seus $N$ enters ordenats.

A continuació hi ha la mida $M$ del segon array, seguida dels seus $M$ enters ordenats.

## Salida

Imprimeix els elements de la intersecció separats per un espai. Si no hi ha cap element comú, imprimeix una línia buida.

## Tests

### Test
```input
4
1
2
4
5
3
2
3
5
```
```output
2 5
```

### Test
```input
3
1
2
3
3
4
5
6
```
```output

```

### Test
```input
3
10
20
30
3
10
20
30
```
```output
10 20 30
```

### Test
```input
4
1
1
2
2
3
1
2
3
```
```output
1 2
```
