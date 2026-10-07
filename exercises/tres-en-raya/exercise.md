---
slug: tres-en-raya
---
# OXO

Donat un tauler de tres en ratlla, determina el guanyador, o si hi ha empat.

## Input

El tauler consisteix en 3 línies amb 3 caracters cada línia.
Les caselles del tauler buides es marquen amb un '-'
Les caselles ocupades per fitxes es marquen amb 'O' i 'X'.

## Output

El guanyador es mostrarà amb la seva marca, i s'usa '-' per a l'empat.

{ X | O | - }

## Tests

### Test
```input
O--
-O-
XXX
```
```output
X
```

### Test
```input
--X
OOO
-X-
```
```output
O
```

### Test
```input
XXX
00X
X00
```
```output
X
```

### Test
```input
O-X
-XO
XO-
```
```output
X
```

### Test
```input
OXX
XOX
XOO
```
```output
O
```

### Test
```input
XO-
XO-
X--
```
```output
X
```

### Test
```input
XO-
XO-
-O-
```
```output
O
```

### Test
```input
XXO
XXO
O-O
```
```output
O
```

### Test
```input
OXO
OXO
XOX
```
```output
-
```

### Test
```input
XXO
OXX
XOO
```
```output
-
```

### Test
```input
OXO
XOX
XOX
```
```output
-
```

### Test private
```input
XXX
O--
-O-
```
```output
X
```
