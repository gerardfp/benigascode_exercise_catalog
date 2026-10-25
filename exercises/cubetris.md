---
slug: cubetris
difficulty: 4.0
tags: [matrices, 2d-arrays, loops, nested-loops]
---
# Cubetris

En el juego Cubetris, el jugador va colocando unas piezas sobre un tablero intentando cubrir por completo el tablero. Puede poner las piezas en la posición que quiera, y la única limitación es que estas no pueden superponerse.

Por ejemplo, el jugador podría superar el juego así:

![image](assets/cubetris-img0.png)

Si embargo, si juego de esta otra forma, no podría superar el juego, ya que las piezas verde y naranja no habría forma de colocarlas sin superponerse a otras piezas:

![image](assets/cubetris-img1.png)

Deseamos programar la parte del juego que nos dice si una pieza se puede colocar en una posición, o por el contrario no se puede debido a que se superpondría a otras piezas.

## Input

Los dos primeros números indican el tamaño del tablero: $ALTO$ y $ANCHO$
A continuación viene la definición del estado del tablero. Cada número indica el color de la pieza que esta en esa posición. Un cero significa que la posición está vacía.

Por último viene un tablero que define la pieza que se quiere colocar.

## Output

Se imprimirá el tablero resultante tras tras colocar (o no) la pieza.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int rows = sc.nextInt();
    int cols = sc.nextInt();
    int[][] board = new int[rows][cols];
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            board[i][j] = sc.nextInt();
        }
    }
    int[][] piece = new int[rows][cols];
    boolean overlap = false;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            piece[i][j] = sc.nextInt();
            if (piece[i][j] != 0 && board[i][j] != 0) {
                overlap = true;
            }
        }
    }
    if (!overlap) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (piece[i][j] != 0) {
                    board[i][j] = piece[i][j];
                }
            }
        }
    }
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (j > 0) {
                IO.print(" ");
            }
            IO.print(board[i][j]);
        }
        IO.println();
    }
}
```

## Tests

### Test
```input
4 4

1 1 2 3
1 1 2 3
0 2 2 3
0 0 0 3

0 0 0 0
0 0 0 0
4 0 0 0
4 4 4 0
```
```output
1 1 2 3
1 1 2 3
4 2 2 3
4 4 4 3
```
#### Explanation
![image](assets/cubetris-img2.png)

### Test
```input
3 3

1 1 0
1 1 0
0 0 0

0 0 2
0 0 2
0 2 2
```
```output
1 1 2
1 1 2
0 2 2
```
#### Explanation
![image](assets/cubetris-img3.png)

### Test
```input
3 3

1 1 0
1 1 0
0 0 0

0 2 0
0 2 0
2 2 0
```
```output
1 1 0
1 1 0
0 0 0
```
#### Explanation
![image](assets/cubetris-img4.png)

### Test private
```input
3 3

0 0 0
0 1 1
1 1 1

2 2 0
2 2 0
0 0 0
```
```output
0 0 0
0 1 1
1 1 1
```
