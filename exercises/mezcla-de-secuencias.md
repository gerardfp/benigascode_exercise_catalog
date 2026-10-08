---
slug: mezcla-de-secuencias
---
# Mescla de seqüències

Donades dues seqüències de nombres, s'ha d'obtenir una mescla d'elles.

Per a obtenir la mescla s'ha d'agafar un element de cada seqüència alternativament. És a dir, primer un nombre de la primera seqüència, després un altre de la segona, i així successivament. Quan en una seqüència ja no queden més nombres, s'agafaran els nombres que quedin de l'altra.

## Input

La entrada consta de des seqüències.

Per a cada seqüència, el primer nombre  indica el tamany. A continuació ve la seqüència.

## Output

La seqüència resultant.

## Tests

### Test
```input
2 1 2
2 3 4
```
```output
1 3 2 4
```

### Test
```input
3    100 200 300
3    400 500 600
```
```output
100 400 200 500 300 600
```

### Test
```input
5    10 11 12 13 14
5    20 21 22 23 24
```
```output
10 20 11 21 12 22 13 23 14 24
```

### Test
```input
1    1000
1    2000
```
```output
1000 2000
```

### Test
```input
4    1 2 3 4
3    1 2 3
```
```output
1 1 2 2 3 3 4
```

### Test
```input
6    1 2 3 4 5 6
3    1 2 3
```
```output
1 1 2 2 3 3 4 5 6
```

### Test
```input
3    10 20 30
6    10 20 30 40 50 60
```
```output
10 10 20 20 30 30 40 50 60
```

### Test
```input
6     76 65 98 45 32 21
3     99 88 77
```
```output
76 99 65 88 98 77 45 32 21
```
