---
slug: contando-minas
difficulty: 4.0
tags: [matrices, 2d-arrays, loops, nested-loops, counters]
---
# Comptant mines

![image](assets/contando-minas-img0.jpg)

Donat un tauler de buscamines, dir per a cada casella sense mina, quantes caselles amb mina té al seu voltant.

<details>
<summary>Suggerència per a la solució</summary>
Crea dues matrius: una per al tauler inicial, i una altra per al tauler de la solució.

Ves llegint el tauler inicial, i quan trobes un 1, incrementa les cel·les corresonents en el tauler solució.
</details>

## Input

L'entrada consta en primer lloc de dos números $M$ i $N$ que indiquen el tamany (files i columnes) del tauler.

A continuación venen les caselles del tauler. (`0`=no hi ha mina, `1`=hi ha mina)

## Output

S'imprimirá el tauler amb les casellas separades amb un espai i les files separades per un salt de línia. 

En cada casella sense mina s'escriurà el número de mines que té al seu voltant.

Les caselles amb mina es deixaran igual, és a dir, amb un `1`.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int rows = sc.nextInt();
    int cols = sc.nextInt();
    int[][] grid = new int[rows][cols];
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            grid[r][c] = sc.nextInt();
        }
    }

    int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1};
    int[] dc = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            int val;
            if (grid[r][c] == 1) {
                val = 1;
            } else {
                int count = 0;
                for (int d = 0; d < 8; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                        if (grid[nr][nc] == 1) {
                            count++;
                        }
                    }
                }
                val = count;
            }
            IO.print(val);
            if (c < cols - 1) {
                IO.print(" ");
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
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
```
```output
0 0 0 0 0
0 1 1 1 0
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0
```
#### Explanation
![image](assets/contando-minas-img1.png)

### Test
```input
5 5
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 0 0 0
```
```output
1 1 1 0 0
1 1 1 0 0
1 1 2 1 1
0 0 1 1 1
0 0 1 1 1
```
#### Explanation
![image](assets/contando-minas-img2.png)

### Test
```input
3 3

1 0 0
0 0 0
0 0 0
```
```output
1 1 0
1 1 0
0 0 0
```
#### Explanation
![image](assets/contando-minas-img3.png)

### Test
```input
3 3

1 1 1
1 0 1
1 1 1
```
```output
1 1 1
1 8 1
1 1 1
```
#### Explanation
![image](assets/contando-minas-img4.png)

### Test
```input
4 4

0 0 0 0
1 1 0 0
1 1 0 0
0 0 0 0
```
```output
2 2 1 0
1 1 2 0
1 1 2 0
2 2 1 0
```
#### Explanation
![image](assets/contando-minas-img5.png)

### Test
```input
1 4

1 0 1 0
```
```output
1 2 1 1
```
#### Explanation
![image](assets/contando-minas-img6.png)

### Test
```input
5 5

0 0 0 0 0
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
0 0 0 0 0
```
```output
1 1 2 1 1
2 1 3 1 2
1 4 1 4 1
2 1 3 1 2
1 1 2 1 1
```
#### Explanation
![image](assets/contando-minas-img7.png)

### Test
```input
4 1

0
1
0
0
```
```output
1
1
1
0
```
#### Explanation
![image](assets/contando-minas-img8.png)

### Test
```input
8 8

0 0 0 0 0 0 0 1
0 1 0 0 0 0 1 0
1 0 1 0 0 0 0 1
1 1 1 0 0 0 0 0
0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0
1 0 0 1 0 0 0 1
```
```output
1 1 1 0 0 1 2 1 
2 1 2 1 0 1 1 3 
1 6 1 2 0 1 2 1 
1 1 1 3 2 2 2 1 
2 3 2 2 1 1 1 0 
0 0 0 1 2 2 1 0 
1 1 1 1 1 0 1 1 
1 1 1 1 1 0 1 1 
```

### Test private
```input
2 2
1 0
0 0
```
```output
1 1
1 1
```
