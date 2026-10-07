---
slug: distancia-hamming
---
# Distància Hamming

Donats dos Strings, calcula la seva distància Hamming.

La distància Hamming entre dos Strings de la mateixa longitud és la quantitat de posicions en les quals els caracters són diferents.

Exemple:

```text
Hola mon
Hala man
```

La distància Hamming entre "Hola mon" i "Hala man" és 2, ja que en les posicions 1 i 6 els caracters són diferents.

## Input

Dos Strings, cadascun en una línia.

## Output

La distància Hamming entre els dos Strings, **si són d'igual longitud**.

Si són de distinta longitud s'imprimirá -1.

## Tests

### Test 7.69
```input
Hola mon
Hala man
```
```output
2
```

### Test 7.69
```input
i hate java
i love java
```
```output
3
```

### Test private 7.69
```input
CAGGTACAGT
AAGGTACTTA
```
```output
4
```

### Test private 7.69
```input
1011010
1000010
```
```output
2
```

### Test private 7.69
```input
hola
hol
```
```output
-1
```

### Test private 7.69
```input
CGATTGACGATCAT
CGATGCTGACTAT
```
```output
-1
```

### Test private 7.69
```input
hola
hola
```
```output
0
```

### Test private 7.69
```input
h
k
```
```output
1
```

### Test private 7.69
```input
a
a
```
```output
0
```

### Test private 7.69
```input
is this a string?
is this a  string?
```
```output
-1
```

### Test private 7.69
```input
aa
aa
```
```output
0
```

### Test private 7.69
```input
aa
a
```
```output
-1
```

### Test private 7.72
```input
aa
ab
```
```output
1
```
