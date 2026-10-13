---
slug: picos-maximos-y-minimos
---
# Picos máximos y mínimos

Dada una secuencia de picos máximos y mínimos, escribir la sucesión de números consecutivos que completan dichos picos. **La secuencia comienza por un pico mínimo**.

Un pico máximo es un número cuyos antorior y siguiente son menores que él, y un pico mínimo es un número cuyos anterior y siguiente son mayores que él.

Ej:

Picos: 10 14 12 15

Sucesión: 10 11 12 13 14 13 12 13 14 15

## Input

La entrada consta de una serie de casos de prueba.
El primer número T indica la cantidad de casos de prueba que vienen a continuación.
Por cada caso de prueba se indica en el primer número N la cantidad de picos que hay en la secuencia, y a continuación vienen los picos de dicha secuencia. **El primer pico de cada secuencia es un pico mínimo**.

## Output

Por cada caso de prueba se escribirá en una sola linea la sucesión de números consecutivos, separados por un espacio en blanco.

## Tests

### Test
```input
2
5 100 104 102 105 101
4 50 55 50 55
```
```output
100 101 102 103 104 103 102 103 104 105 104 103 102 101
50 51 52 53 54 55 54 53 52 51 50 51 52 53 54 55
```

### Test
```input
3
4 10 13 10 14
3 1000 1005 1004
2 20 30
```
```output
10 11 12 13 12 11 10 11 12 13 14
1000 1001 1002 1003 1004 1005 1004
20 21 22 23 24 25 26 27 28 29 30
```

### Test private
```input
1
2 1 3
```
```output
1 2 3
```
