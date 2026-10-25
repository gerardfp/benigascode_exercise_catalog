---
slug: esquemes-cerca-binaria-punt-insercio
difficulty: 4.0
tags: [arrays, loops, while-loop, search]
---
# Cerca binària: posició d'inserció ordenada

Donat un array de $N$ enters diferents ordenats en ordre creixent i un valor $X$, determina l'índex on es troba $X$. Si no és a l'array, determina l'índex on s'hauria d'inserir per tal que l'array continuï ordenat.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters ordenats.

A l'última línia hi ha el valor $X$.

## Salida

Imprimeix l'índex on es troba o on s'hauria d'inserir $X$.

## Tests

### Test
```input
4
1
3
5
6
5
```
```output
2
```

### Test
```input
4
1
3
5
6
2
```
```output
1
```

### Test
```input
4
1
3
5
6
7
```
```output
4
```

### Test
```input
4
1
3
5
6
0
```
```output
0
```
