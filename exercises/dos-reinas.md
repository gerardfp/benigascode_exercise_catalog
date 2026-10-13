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

## Output

SI | NO

## Tests

### Test
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

### Test
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

### Test
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

### Test
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

### Test
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

### Test
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

### Test
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

### Test
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

### Test
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

### Test
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

### Test
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

### Test
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

### Test private
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
