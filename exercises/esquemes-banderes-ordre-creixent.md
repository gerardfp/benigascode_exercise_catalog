---
slug: esquemes-banderes-ordre-creixent
difficulty: 3.0
tags: [arrays, loops, for-loop, operators, relational-operators, booleans, flags]
---
# Banderes: verificació d'ordre creixent

Escriu un programa que verifica si una seqüència de $N$ nombres enters està ordenada de manera **estrictament creixent** (és a dir, cada element és estrictament menor que el següent: $x_i < x_{i+1}$).

## Entrada

A la primera línia hi ha el número $N$ ($N \ge 1$).

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix `SI` si la seqüència és estrictament creixent, o `NO` en cas contrari.

## Tests

### Test
```input
4
2
5
9
14
```
```output
SI
```

### Test
```input
4
2
5
5
14
```
```output
NO
```

### Test
```input
4
10
8
6
4
```
```output
NO
```

### Test
```input
1
50
```
```output
SI
```
