---
slug: lletres-scrabble
tags: [if, switch]
difficulty: 5
---
# Lletres de l'Scrabble

![image](assets/c2-l1-2-lletres-scrabble-img0.jpg)

Donada una lletra, obté la seva puntuació d'Scrabble.

```
Letter                             Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
```

## Input

Un caracter

## Output

La puntuació de la lletra

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    String s = sc.next().toUpperCase();
    char c = s.charAt(0);
    int score = switch (c) {
        case 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T' -> 1;
        case 'D', 'G' -> 2;
        case 'B', 'C', 'M', 'P' -> 3;
        case 'F', 'H', 'V', 'W', 'Y' -> 4;
        case 'K' -> 5;
        case 'J', 'X' -> 8;
        case 'Q', 'Z' -> 10;
        default -> 0;
    };
    IO.println(score);
}
```

## Tests

### Test
```input
E
```
```output
1
```

### Test
```input
A
```
```output
1
```

### Test
```input
E
```
```output
1
```

### Test
```input
I
```
```output
1
```

### Test
```input
O
```
```output
1
```

### Test
```input
U
```
```output
1
```

### Test
```input
L
```
```output
1
```

### Test
```input
N
```
```output
1
```

### Test
```input
R
```
```output
1
```

### Test
```input
S
```
```output
1
```

### Test
```input
T
```
```output
1
```

### Test
```input
D
```
```output
2
```

### Test
```input
G
```
```output
2
```

### Test
```input
B
```
```output
3
```

### Test
```input
C
```
```output
3
```

### Test
```input
M
```
```output
3
```

### Test
```input
P
```
```output
3
```

### Test
```input
F
```
```output
4
```

### Test
```input
H
```
```output
4
```

### Test
```input
V
```
```output
4
```

### Test
```input
W
```
```output
4
```

### Test
```input
Y
```
```output
4
```

### Test
```input
K
```
```output
5
```

### Test
```input
J
```
```output
8
```

### Test
```input
X
```
```output
8
```

### Test
```input
Q
```
```output
10
```

### Test private
```input
Z
```
```output
10
```
