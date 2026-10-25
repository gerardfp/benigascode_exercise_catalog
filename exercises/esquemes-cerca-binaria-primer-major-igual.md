---
slug: esquemes-cerca-binaria-primer-major-igual
difficulty: 4.0
tags: [arrays, loops, while-loop, search]
---
# Cerca binària: primer element major o igual (lower bound)

Donat un array de $N$ nombres enters ordenats en ordre creixent i un valor llindar $X$, utilitza cerca binària per trobar el valor del primer element de l'array que sigui major o igual a $X$ ($element \ge X$). Si tots els elements de l'array són estrictament menors que $X$, imprimeix `CAP`.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters ordenats.

A l'última línia hi ha el valor llindar $X$.

## Salida

Imprimeix el valor del primer element $\ge X$ o la paraula `CAP`.

## Tests

### Test
```input
5
10
20
30
40
50
25
```
```output
30
```

### Test
```input
5
10
20
30
40
50
30
```
```output
30
```

### Test
```input
4
2
4
6
8
10
```
```output
CAP
```

### Test
```input
3
5
10
15
1
```
```output
5
```
