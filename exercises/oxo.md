---
slug: OXO
tags: [matrix, if]
difficulty: 4
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

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNext()) return;
    String[] b = new String[3];
    for (int i = 0; i < 3; i++) {
        b[i] = sc.next();
    }
    
    char winner = '-';
    for (int i = 0; i < 3; i++) {
        if (b[i].charAt(0) != '-' && b[i].charAt(0) == b[i].charAt(1) && b[i].charAt(1) == b[i].charAt(2)) {
            winner = b[i].charAt(0);
        }
    }
    for (int j = 0; j < 3; j++) {
        if (b[0].charAt(j) != '-' && b[0].charAt(j) == b[1].charAt(j) && b[1].charAt(j) == b[2].charAt(j)) {
            winner = b[0].charAt(j);
        }
    }
    if (b[0].charAt(0) != '-' && b[0].charAt(0) == b[1].charAt(1) && b[1].charAt(1) == b[2].charAt(2)) {
        winner = b[0].charAt(0);
    }
    if (b[0].charAt(2) != '-' && b[0].charAt(2) == b[1].charAt(1) && b[1].charAt(1) == b[2].charAt(0)) {
        winner = b[0].charAt(2);
    }
    IO.println(winner);
}
```

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
OOX
XOO
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

### Test private
```input
OXO
XOX
XOX
```
```output
-
```
