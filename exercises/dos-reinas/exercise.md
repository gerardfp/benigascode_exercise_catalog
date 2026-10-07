---
slug: dos-reinas
---
# Dos Reinas

Dadas las posiciones de las reinas blanca y negra en un tablero de ajedrez, el programa debe decir si se atacan mútuamente.

## Input

El tablero de ajedrez consiste en 8 lineas de ocho caracteres cada una.
Cada caracter representa una casilla del tablero.
El caracter '-' indica una casilla vacía.
La casilla en la que está la reina BLANCA se indica con una 'B'.
La casilla en la que está la reina NEGRA se indica con una 'N'.

C = 64

## Output

SI | NO

## Tests

### Test 7.69
```input
B----N--
--------
--------
--------
--------
--------
--------
--------
```
```output
SI
```

### Test 7.69
```input
--------
B-------
--------
--------
--------
--------
-----N--
--------
```
```output
SI
```

### Test private 7.69
```input
--------
--------
B-------
--------
--------
--------
--------
N-------
```
```output
SI
```

### Test private 7.69
```input
--------
------B-
--------
--------
--------
--N-----
--------
--------
```
```output
SI
```

### Test private 7.69
```input
--------
-------N
--------
--------
--------
--------
--------
-B------
```
```output
SI
```

### Test private 7.69
```input
--------
--------
--------
--------
--------
-------N
--------
-------B
```
```output
SI
```

### Test private 7.69
```input
--------
--------
-N------
--------
--------
--------
--------
------B-
```
```output
SI
```

### Test private 7.69
```input
--------
--------
--------
--------
--------
--------
--------
--N--B--
```
```output
SI
```

### Test private 7.69
```input
-B------
------N-
--------
--------
--------
--------
--------
--------
```
```output
NO
```

### Test private 7.69
```input
-----B--
--------
--------
--------
--------
--------
--------
---N----
```
```output
NO
```

### Test private 7.69
```input
--------
--------
--------
--------
N-------
--------
--------
------B-
```
```output
NO
```

### Test private 7.69
```input
--------
--------
--------
--------
-------N
--------
--------
B-------
```
```output
NO
```

### Test private 7.72
```input
BN------
--------
--------
--------
--------
--------
--------
--------
```
```output
SI
```
