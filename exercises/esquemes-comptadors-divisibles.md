---
slug: esquemes-comptadors-divisibles
tags: [arrays, esquemes]
---
# Comptadors: divisibles

Escriu un programa que llegix una sèrie de números, i un número divisor, i compta quants són divisibles per aquest divisor.

## Entrada

A la primera línia hi ha el número `N`, que indica la quantitat de números de la sèrie.

Després ve la sèrie de números, cadascun en una línea.

A la última línia hi ha el número divisor.

## Salida

Imprimix la quantitat de números divisibles pel divisor.

## Tests

### Test
```input
4
13
27
17
29
3
```
```output
1
```
```explanation
Només el 27 es divisible per 3
```

### Test
```input
4
425
333
111
225
5
```
```output
2
```
```explanation
El 425 i el 225 son dibisibles per 5
```

### Test
```input
10
24579
3241
45693
4567
355
4567
453435
56826
86863
3228565
12
```
```output
0
```
```explanation
Cap número es divisible per 12
```
