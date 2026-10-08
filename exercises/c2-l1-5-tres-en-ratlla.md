---
slug: c2-l1-5-tres-en-ratlla
---
# Tres en ratlla

Donat un tauler de tres en ratlla, determina el guanyador, o si hi ha empat.

## Input

El tauler consta de nou nombres corresponents a les nou caselles.

Les caselles buides es marquen amb un 0.

Les caselles amb una fitxa es marquen amb un 1 o un 2.

El tauler és vàlid.

## Output

Jugador1 | Jugador2 | Empat

## Tests

### Test
```input
1 1 1
2 2 0
2 2 0
```
```output
Jugador1
```

### Test
```input
1 2 2
1 2 2
1 0 0
```
```output
Jugador1
```

### Test
```input
1 2 2
2 1 0
2 0 1
```
```output
Jugador1
```

### Test
```input
0 0 0
1 1 1
2 2 0
```
```output
Jugador1
```

### Test
```input
0 0 0
1 1 2
2 1 1
```
```output
Empat
```

### Test
```input
0 1 0
2 1 2
0 1 2
```
```output
Jugador1
```

### Test
```input
1 0 2
1 2 0
2 1 0
```
```output
Jugador2
```

### Test
```input
1 1 0
1 1 0
2 2 2
```
```output
Jugador2
```

### Test
```input
0 2 1
2 1 1
2 2 1
```
```output
Jugador1
```

### Test
```input
0 0 0
0 0 0
0 0 0
```
```output
Empat
```
