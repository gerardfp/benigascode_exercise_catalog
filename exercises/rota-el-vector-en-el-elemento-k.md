---
slug: rota-el-vector-en-el-elemento-k
tags: [arrays]
difficulty: 3
---
# Rota el vector en el elemento k

Dado un vector de enteros y un elemento k rotar el vector para que el elemento en el la posición k sea el primer elemento del nuevo vector.

La entrada consiste en un número que indica el tamaño del vector (N), a continuación en la siguiente línea vienen todos los elementos del vector y en la última línea el elemento k.

El elemento k está comprendido entre 0 y N-1 (siendo N el tamaño del vector).

10

1 2 3 4 5 6 7 8 9 10

1

- Un vector de 10 elementos.
- Los elementos del vector son 1 2 3 4 5 6 7 8 9 10
- El elemento k es 1

Con la siguiente entrada deberíamos rotar el vector de tal manera que el elemento en la posición 1 (el número 2) esté en la primera posición.

Esta sería la salida para el caso del ejemplo:

2 3 4 5 6 7 8 9 10 1

## Input

1 2 3 4 5 6 7 8 9 10

## Output

2 3 4 5 6 7 8 9 10 1

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int n = sc.nextInt();
    int[] a = new int[n];
    for (int i = 0; i < n; i++) {
        a[i] = sc.nextInt();
    }
    int k = sc.nextInt();

    for (int i = 0; i < n; i++) {
        int idx = (k + i) % n;
        if (i > 0) {
            IO.print(" ");
        }
        IO.print(a[idx]);
    }
    IO.println();
}
```

## Tests

### Test
```input
10
1 2 3 4 5 6 7 8 9 10
1
```
```output
2 3 4 5 6 7 8 9 10 1
```
