---
slug: scrabble
tags: [loops]
difficulty: 5
---
# Scrabble

Donada una paraula, obté la seva puntuació d'Scrabble.

```
Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
```

## Input

Una paraula

## Output

La puntuació obtinguda

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNext()) return;
    String word = sc.next().toUpperCase();
    int score = 0;
    for (int i = 0; i < word.length(); i++) {
        char c = word.charAt(i);
        score += switch (c) {
            case 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T' -> 1;
            case 'D', 'G' -> 2;
            case 'B', 'C', 'M', 'P' -> 3;
            case 'F', 'H', 'V', 'W', 'Y' -> 4;
            case 'K' -> 5;
            case 'J', 'X' -> 8;
            case 'Q', 'Z' -> 10;
            default -> 0;
        };
    }
    IO.println(score);
}
```

## Tests

### Test
```input
hola
```
```output
7
```
#### Explanation
`
h=4
o=1
l=1
a=1
`

### Test
```input
mundo
```
```output
8
```
#### Explanation
`
m=3
u=1
n=1
d=2
o=1
`

### Test
```input
java
```
```output
14
```
#### Explanation
`
j=8
a=1
v=4
a=1
`

### Test
```input
a
```
```output
1
```

### Test private
```input
HACKERRANK
```
```output
23
```
