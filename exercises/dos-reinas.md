---
slug: dos-reinas
difficulty: 3.0
tags: [conditionals, if-else, math]
---
# Dos Reinas

Dadas las posiciones de las reinas blanca y negra en un tablero de ajedrez, el programa debe decir si se atacan mútuamente.

## Input

El tablero de ajedrez consiste en 8 lineas de ocho caracteres cada una.
Cada caracter representa una casilla del tablero:
- Las casillas vaciás se indican con un caracter `-`
- La casilla en la que está la reina BLANCA se indica con una `B`
- La casilla en la que está la reina NEGRA se indica con una `N`

## Output

`SI` | `NO`

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int rB = -1, cB = -1, rN = -1, cN = -1;
    for (int r = 0; r < 8; r++) {
        String row = sc.next();
        for (int c = 0; c < 8; c++) {
            char ch = row.charAt(c);
            if (ch == 'B') {
                rB = r;
                cB = c;
            } else if (ch == 'N') {
                rN = r;
                cN = c;
            }
        }
    }
    if (rB == rN || cB == cN || Math.abs(rB - rN) == Math.abs(cB - cN)) {
        IO.println("SI");
    } else {
        IO.println("NO");
    }
}
```

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
