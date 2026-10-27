---
slug: outline
difficulty: 8.0
tags: [arrays, matrices, 2d-arrays, loops, nested-loops]
---
# Outline

Dadas unas figuras, dibuja su contorno.

Los ángulos se marcarán con un `+`

Las líneas verticales con un `|`

Las líneas horizontales con un `-`

## Input

Los números $M$ y $N$ indican el ancho y alto del lienzo.

A continuación vienen los $MxN$ píxeles:

Un símbolo `#` representa el relleno de la figura

Un símbolo `.` representa el fondo del lienzo.

## Output

Se imprimirá el lienzo resultante conforme los casos de prueba.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int W = sc.nextInt();
    int H = sc.nextInt();

    char[][] grid = new char[H][W];
    for (int r = 0; r < H; r++) {
        for (int c = 0; c < W; c++) {
            grid[r][c] = sc.next().charAt(0);
        }
    }

    for (int r = 0; r < H; r++) {
        for (int c = 0; c < W; c++) {
            if (c > 0) IO.print(" ");
            if (grid[r][c] == '.') {
                IO.print('.');
            } else {
                int u = (r > 0 && grid[r - 1][c] == '#') ? 1 : 0;
                int d = (r < H - 1 && grid[r + 1][c] == '#') ? 1 : 0;
                int l = (c > 0 && grid[r][c - 1] == '#') ? 1 : 0;
                int ri = (c < W - 1 && grid[r][c + 1] == '#') ? 1 : 0;

                int ul = (r > 0 && c > 0 && grid[r - 1][c - 1] == '#') ? 1 : 0;
                int ur = (r > 0 && c < W - 1 && grid[r - 1][c + 1] == '#') ? 1 : 0;
                int dl = (r < H - 1 && c > 0 && grid[r + 1][c - 1] == '#') ? 1 : 0;
                int dr = (r < H - 1 && c < W - 1 && grid[r + 1][c + 1] == '#') ? 1 : 0;

                if ((u == 0 || d == 0) && (l == 0 || ri == 0)) {
                    IO.print('+');
                } else if ((u == 0 || d == 0) && (l == 1 && ri == 1)) {
                    IO.print('-');
                } else if ((l == 0 || ri == 0) && (u == 1 && d == 1)) {
                    IO.print('|');
                } else if (u == 1 && d == 1 && l == 1 && ri == 1) {
                    if (ul == 0 || ur == 0 || dl == 0 || dr == 0) {
                        IO.print('+');
                    } else {
                        IO.print(' ');
                    }
                }
            }
        }
        IO.println();
    }
}
```

## Tests

### Test
```input
5 5
. . . . . 
. # # # .
. # # # .
. # # # .
. . . . . 
```
```output
. . . . .
. + - + .
. |   | .
. + - + .
. . . . .
```

### Test
```input
8 7
. . . . . . . .
. # # # # . . .
. # # # # . . .
. # # # # # # .
. # # # # # # .
. # # # # # # .
. . . . . . . . 
```
```output
. . . . . . . .
. + - - + . . .
. |     | . . .
. |     + - + .
. |         | .
. + - - - - + .
. . . . . . . . 
```

### Test
```input
6 7
. . . . . .
# # # # # .
# # # # # .
# # # # # .
. . # # # .
. . # # # .
. . . . . .
```
```output
. . . . . .
+ - - - + .
|       | .
+ - +   | .
. . |   | .
. . + - + .
. . . . . .
```

### Test
```input
7 5
# # # # # . .
# # # # # . .
# # # # # # #
. . # # # # #
. . # # # # #
```
```output
+ - - - + . .
|       | . .
+ - +   + - +
. . |       |
. . + - - - +
```

### Test
```input
13 15
. . . . . . . . . . . . .
. . . # # # . # # # . . .
. . . # # # . # # # . . . 
. # # # # # # # # # # # .
. # # # # # # # # # # # .
. # # # # # # # # # # # .
. . . # # # . # # # . . .
. . . # # # . # # # . . .
. . . # # # . # # # . . .
. # # # # # # # # # # # .
. # # # # # # # # # # # .
. # # # # # # # # # # # .
. . . # # # . # # # . . .
. . . # # # . # # # . . .
. . . . . . . . . . . . .
```
```output
. . . . . . . . . . . . .
. . . + - + . + - + . . .
. . . |   | . |   | . . . 
. + - +   + - +   + - + .
. |                   | .
. + - +   + - +   + - + .
. . . |   | . |   | . . .
. . . |   | . |   | . . .
. . . |   | . |   | . . .
. + - +   + - +   + - + .
. |                   | .
. + - +   + - +   + - + .
. . . |   | . |   | . . .
. . . + - + . + - + . . .
. . . . . . . . . . . . .
```

### Test private
```input
11 13
. . # # # . # # # . .
. . # # # . # # # . . 
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
. . # # # . # # # . .
. . # # # . # # # . .
. . # # # . # # # . .
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
. . # # # . # # # . .
. . # # # . # # # . .
```
```output
. . + - + . + - + . .
. . |   | . |   | . . 
+ - +   + - +   + - +
|                   |
+ - +   + - +   + - +
. . |   | . |   | . .
. . |   | . |   | . .
. . |   | . |   | . .
+ - +   + - +   + - +
|                   |
+ - +   + - +   + - +
. . |   | . |   | . .
. . + - + . + - + . .
```
