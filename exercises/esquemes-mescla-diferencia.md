---
slug: esquemes-mescla-diferencia
difficulty: 4.0
tags: [arrays, loops, while-loop, merge, two-pointers, filtering]
---
# Mescla: diferència d'arrays ordenats (A - B)

Donats dos arrays d'enters ordenats $A$ (de mida $N$) i $B$ (de mida $M$), calcula la diferència $A \setminus B$ (els elements que estan a $A$ però no a $B$) aprofitant que ambdós arrays estan ordenats mitjançant la tècnica de mescla en $O(N+M)$.

## Entrada

A la primera línia hi ha la mida $N$ del primer array $A$, seguida dels seus $N$ enters ordenats.

A continuació hi ha la mida $M$ del segon array $B$, seguida dels seus $M$ enters ordenats.

## Salida

Imprimeix els elements de $A \setminus B$ en ordre creixent separats per un espai. Si la diferència és buida, imprimeix una línia buida.

## Tests

### Test
```input
5
1
2
3
4
5
2
2
4
```
```output
1 3 5
```

### Test
```input
3
1
2
3
3
1
2
3
```
```output

```

### Test
```input
3
5
10
15
2
1
2
```
```output
5 10 15
```

### Test
```input
4
1
3
5
7
3
3
5
9
```
```output
1 7
```
