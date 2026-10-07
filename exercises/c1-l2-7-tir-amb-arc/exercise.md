---
slug: c1-l2-7-tir-amb-arc
---
# Tir amb arc

A l'esport de tir amb arc un arquer obté una puntuació segons l'anell on clava la fletxa.
En una diana com la aquesta, rebria 5 punts al color groc, 4 al vermell, 3 al blau, 2 al negre i 1 al blanc.

![image](1556184434-7bc003fe3f-diana2.png)

L'anell groc té un radi de 5cm, i cada anell és 5cm més gran.

Si el tir cau justament sobre el límit d'un anell, es considera que la puntuació és la que correspon a l'anell de menys puntuació.

## Input

La entrada consta de 2 nombres decimals (X, Y) que indiquen la posició on s'ha clavat la fletxa respecte al centre de la diana (0,0).

Es garanteix que la distància al centre de la diana sempre serà menor que 25.

## Output

S'imprimirà la puntuació obtinguda amb el tir.

## Tests

### Test 9.09
```input
0 0
```
```output
5
```

### Test 9.09
```input
0 0
```
```output
5
```

### Test private 9.09
```input
5 5
```
```output
4
```

### Test private 9.09
```input
10 5
```
```output
3
```

### Test private 9.09
```input
-15 -10
```
```output
2
```

### Test private 9.09
```input
20 5
```
```output
1
```

### Test private 9.09
```input
0 10
```
```output
3
```

### Test private 9.09
```input
0.1 24.9
```
```output
1
```

### Test private 9.09
```input
7.1 7.9
```
```output
3
```

### Test private 9.09
```input
20 0
```
```output
1
```

### Test private 9.1
```input
-2.67 4.89
```
```output
4
```
