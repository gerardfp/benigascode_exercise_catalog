---
slug: c5-l1-6-tres-en-ratlla
---
# OXO

Donat un tauler de tres en ratlla, determina el guanyador, o si hi ha empat.

## Input

El tauler consisteix en 3 línies amb 3 caracters cada línia.

Les caselles del tauler buides es marquen amb un '-'

Les caselles ocupades per fitxes es marquen amb 'O' i 'X'.

## Output

El guanyador es mostrarà amb la seva marca, i s'usarà '-' per a l'empat.

{ X | O | - }

## Tests

### Test 8.33
```input
O--
-O-
XXX
```
```output
X
```

### Test 8.33
```input
O--
-O-
XXX
```
```output
X
```

### Test private 8.33
```input
--X
OOO
-X-
```
```output
O
```

### Test private 8.33
```input
XXX
OOX
XOO
```
```output
X
```

### Test private 8.33
```input
O-X
-XO
XO-
```
```output
X
```

### Test private 8.33
```input
OXX
XOX
XOO
```
```output
O
```

### Test private 8.33
```input
XO-
XO-
X--
```
```output
X
```

### Test private 8.33
```input
XO-
XO-
-O-
```
```output
O
```

### Test private 8.33
```input
XXO
XXO
O-O
```
```output
O
```

### Test private 8.33
```input
OXO
OXO
XOX
```
```output
-
```

### Test private 8.33
```input
XXO
OXX
XOO
```
```output
-
```

### Test private 8.37
```input
OXO
XOX
XOX
```
```output
-
```
