---
slug: esquemes-cerca-lineal-ultima-posicio
difficulty: 3.0
tags: [arrays, loops, for-loop, search]
---
# Cerca lineal: última posició d'un valor

Donada una seqüència de $N$ nombres enters i un valor objectiu $X$, troba l'índex (base 0) de l'**última** aparició de $X$ a la seqüència. Si el valor no apareix, imprimeix `-1`.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters de la seqüència.

A l'última línia hi ha el valor $X$ a cercar.

## Salida

Imprimeix l'índex de l'última aparició de $X$, o `-1` si no apareix.

## Tests

### Test
```input
5
10
20
30
20
40
20
```
```output
3
```

### Test
```input
4
1
2
3
4
5
```
```output
-1
```

### Test
```input
3
9
9
9
9
```
```output
2
```

### Test
```input
1
7
7
```
```output
0
```
