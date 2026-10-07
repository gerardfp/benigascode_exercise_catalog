---
slug: graficos-de-calificaciones
tags: [scanner, i/o]
---
# Gràfics de qualificacions

Donades les notes que han tret els alumnes en una matèria, genera un gràfic que resumeixi les qualificacions obtingudes.

- Excel·lent: entre 9 i 10

- Notable: entre 7 i 9

- Bé: entre 6 i 7

- Suficient: entre 5 i 6

- Insuficient: menys de 5

La gràfica mostrarà un caracter coixinet '#' per cada estudiant que ha tret cada qualificació.

Exemple:

```text
E: #######
N: #########
B: #####
S: ###
I: #
```

## Input

Una seqüència de  nombres enters.

Cada nombre és la Nota obtinguda per un alumne en la matèria.

La seqüència acaba amb un -1.

## Output

La gràfica amb el resum de les notes, amb el format indicat.

## Tests

### Test 16.67
```input
4 5 6 7 8 9 10    -1
```
```output
E:##
N:##
B:#
S:#
I:#
```

### Test 16.67
```input
4 4 4 4 5 6 6 7 7 7 9   -1
```
```output
E:#
N:###
B:##
S:#
I:####
```

### Test private 16.67
```input
4 5 3 6 7 5 6 8 5 6  9 8 5 8 7 9 5 8 4 3 7 8 6   -1
```
```output
E:##
N:########
B:####
S:#####
I:####
```

### Test private 16.67
```input
5 6 7 3 5 8 9 5 6 7 6 5 8 7 9 2 9 3 7 9 9 5 4 6 9 3 8 9 10 10 8 10 6    -1
```
```output
E:##########
N:########
B:#####
S:#####
I:#####
```

### Test private 16.67
```input
5  -1
```
```output
E:
N:
B:
S:#
I:
```

### Test private 16.65
```input
10 10 10 10 10 10 10 10 10 10    -1
```
```output
E:##########
N:
B:
S:
I:
```
