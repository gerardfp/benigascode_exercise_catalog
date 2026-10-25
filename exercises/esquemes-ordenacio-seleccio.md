---
slug: esquemes-ordenacio-seleccio
difficulty: 4.0
tags: [arrays, loops, nested-loops, sorting, min-max]
---
# Ordenació: selecció directa (Selection Sort)

Implementa l'algoritme d'ordenació per **selecció directa** (**Selection Sort**) per ordenar un array de $N$ nombres enters en ordre creixent. 

En cada passada $i$, cerca l'índex de l'element mínim del sub-array $[i, N-1]$ i intercanvia'l amb la posició $i$.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix els $N$ elements ordenats en ordre creixent en una única línia, separats per un espai.

## Tests

### Test
```input
5
29
10
14
37
13
```
```output
10 13 14 29 37
```

### Test
```input
4
4
3
2
1
```
```output
1 2 3 4
```

### Test
```input
3
1
2
3
```
```output
1 2 3
```

### Test
```input
2
9
2
```
```output
2 9
```
