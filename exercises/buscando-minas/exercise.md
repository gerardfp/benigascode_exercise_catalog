---
slug: buscando-minas
tags: [matrix]
---
# Cercant mines

Donat un tauler de buscamines i unes posicions, dir si en aquestes posicions hi ha o no una mina.

![image](buscando-minas-img0.jpg)

## Input

L'entrada consta en primer lloc de dos números `F` i `C` que indiquen el número de files i columnes del tauler.

A continuació venen les `FxC` caselles del tauler (`0`, `1`).

Després venen les posicions en les que s'ha de comprovar si hi ha mina.
Cada posició consta de dos números que indiquen la fila i la columna  que s'ha de comprovar. 
**Les posicions comencen per 1** (ja que és la forma en què es jugaria el joc).

Les posicions a comprovar acaben amb `0 0`.

## Output

Per cada posició a comprovar s'escriurà `SI` si en la casella hi ha una mina, o `NO` si no hi ha.

## Tests

### Test
```input
3 3
1 0 0
0 0 0
0 0 0
1 1
2 2
0 0
```
```output
SI
NO
```

### Test
```input
3 3

1 0 0
0 0 0
0 0 1

1 1
2 2
3 3
0 0
```
```output
SI
NO
SI
```

### Test
```input
5 5

0 1 0 0 0
0 0 0 0 1
0 1 0 0 1
0 0 1 1 0
0 0 1 1 0

1 1
1 2
3 4
3 5
5 3
0 0
```
```output
NO
SI
NO
SI
SI
```

### Test
```input
1 1

1

1 1
0 0
```
```output
SI
```

### Test
```input
1 4

0 0 0 0

1 1
1 2
1 3
1 4
0 0
```
```output
NO
NO
NO
NO
```

### Test
```input
3 4

0 1 0 0
0 0 0 1
0 1 1 0

1 3
3 4
3 2
0 0
```
```output
NO
NO
SI
```
