---
slug: tres-en-raya
difficulty: 5
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

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    char[][] b = new char[3][3];
    for (int i = 0; i < 3; i++) {
        String line = sc.next();
        for (int j = 0; j < 3; j++) {
            char c = line.charAt(j);
            if (c == '0') {
                c = 'O';
            }
            b[i][j] = c;
        }
    }

    char winner = '-';
    for (int i = 0; i < 3; i++) {
        if (b[i][0] != '-' && b[i][0] == b[i][1] && b[i][1] == b[i][2]) {
            winner = b[i][0];
        }
    }
    for (int j = 0; j < 3; j++) {
        if (b[0][j] != '-' && b[0][j] == b[1][j] && b[1][j] == b[2][j]) {
            winner = b[0][j];
        }
    }
    if (b[0][0] != '-' && b[0][0] == b[1][1] && b[1][1] == b[2][2]) {
        winner = b[0][0];
    }
    if (b[0][2] != '-' && b[0][2] == b[1][1] && b[1][1] == b[2][0]) {
        winner = b[0][2];
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
