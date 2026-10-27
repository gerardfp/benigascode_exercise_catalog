---
slug: separar-los-grandes-de-los-pequenos
difficulty: 4.0
tags: [arrays, loops, for-loop, filtering, partitioning]
---
# Separar los grandes de los pequeños

Dada un secuencia de números y un valor límite, separar la secuencia en dos secuencias: en la primera los valores inferiores o iguales al límite, y en la segunda los superiores al límite.

## Input

El primer número N indica el tamaño de la secuencia. A continuación viene la secuencia.

Después viene el valor límite.

## Output

Las dos secuencias separadas por un salto de línea.

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
    int limit = sc.nextInt();

    String small = "";
    String big = "";
    for (int i = 0; i < n; i++) {
        if (a[i] <= limit) {
            small += (small.length() == 0 ? "" : " ") + a[i];
        } else {
            big += (big.length() == 0 ? "" : " ") + a[i];
        }
    }

    if (small.length() > 0) {
        IO.println(small);
    }
    if (big.length() > 0) {
        IO.println(big);
    }
}
```

## Tests

### Test
```input
3   1 2 3
2
```
```output
1 2
3
```

### Test
```input
5    100 300 400 200 500
300
```
```output
100 300 200
400 500
```

### Test
```input
5    34 56 78 45 12
50
```
```output
34 45 12
56 78
```

### Test
```input
3    67 78 89
10
```
```output
67 78 89
```

### Test
```input
3    67 78 89
100
```
```output
67 78 89
```

### Test
```input
5    3 1 4 2 5
1
```
```output
1
3 4 2 5
```

### Test private
```input
10    12 12 13 18 19 15 16 20 17 18
17
```
```output
12 12 13 15 16 17
18 19 20 18
```
