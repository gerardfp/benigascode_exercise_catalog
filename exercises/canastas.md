---
slug: canastas
---
# Encistellaments

Al basquetbol es poden anotar cistelles d'1, 2 i 3 punts.

Donada l'evolució de la puntuació d'un equip en un partit, determina el nombre de cistelles anotades d'1, 2 i 3 punts.

Exemple:

Evolució de la puntuació:

```text
2 4 7 8 11 13 14
```

- La primera cistella va estar de 2 punts

- La segona cistella va estar de 2 punts

- La tercera cistella va estar de 3 punts

- La quarta cistella va estar d'1 punt

- La cinquena cistella va estar de 3 punts

- La sisena cistella va estar de 2 punts

- L'última cistella va estar de 1 punt

En total:

- Cistelles d' 1 punt -> 2

- Cistelles de 2 punts -> 3

- Cistelles de 3 punts -> 2

## Input

L'entrada consta d'una seqüència d'  nombres que indiquen l'evolució de la puntuació.

L'entrada acaba amb un -1.

## Output

El nombre de cistelles d'1, 2 i 3 punts, en diferents línies.

## Tests

### Test
```input
1 4 6 7 9   -1
```
```output
2
2
1
```

### Test
```input
3 5 6 9   -1
```
```output
1
1
2
```

### Test
```input
3    -1
```
```output
0
0
1
```

### Test
```input
1 3 6   -1
```
```output
1
1
1
```

### Test
```input
3 4 7 9 12 15 16 17 20 21 23 25 28    -1
```
```output
4
3
6
```

### Test
```input
2 3 6 7 8 11 14 16 19 20 21 22 25 28 29 31 32 33 34 36 39 41 43 45 48 51 52 55 56 57 58 60 62 63 66 68 70 71 73 75 76 77 78      -1
```
```output
19
13
11
```

### Test
```input
1 4 5 8 10 11 13 14 17 18 20 23 25 27 28 29 31 34 36 38 40 42 44 45 48 49 50 53 54 55 57 60 62 63 65 67 69 70 73 74 75 78 79 81    -1
```
```output
17
17
10
```

### Test
```input
1  -1
```
```output
1
0
0
```

### Test
```input
1  -1
```
```output
1
0
0
```

### Test
```input
-1
```
```output
0
0
0
```

### Test
```input
2   -1
```
```output
0
1
0
```
