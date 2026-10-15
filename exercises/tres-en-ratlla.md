---
slug: tres-en-ratlla
tags: [if]
difficulty: 5
---
# Tres en ratlla

Donat un tauler de tres en ratlla, determina el guanyador, o si hi ha empat.

## Input

El tauler consta de nou nombres corresponents a les nou caselles.

Les caselles buides es marquen amb un 0.

Les caselles amb una fitxa es marquen amb un 1 o un 2.

## Output

Jugador1 | Jugador2 | Empat

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int[] b = new int[9];
    for (int i = 0; i < 9; i++) {
        b[i] = sc.nextInt();
    }

    int[][] lines = {
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
        {0, 4, 8}, {2, 4, 6}
    };

    boolean p1Wins = false;
    boolean p2Wins = false;

    for (int i = 0; i < lines.length; i++) {
        int x = lines[i][0];
        int y = lines[i][1];
        int z = lines[i][2];
        if (b[x] != 0 && b[x] == b[y] && b[y] == b[z]) {
            if (b[x] == 1) p1Wins = true;
            if (b[x] == 2) p2Wins = true;
        }
    }

    if (p1Wins) {
        IO.println("Jugador1");
    } else if (p2Wins) {
        IO.println("Jugador2");
    } else {
        IO.println("Empat");
    }
}
```

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

### Test private
```input
0 0 0
0 0 0
0 0 0
```
```output
Empat
```
