---
slug: suma-de-dos-secuencias
difficulty: 4.0
tags: [arrays, loops, for-loop, operators, arithmetic]
---
# Suma de dos secuencias

Dadas dos secuencias de números, sumar cada número de la primera con su correspondiente de la segunda.

## Input

La entrada consta de dos secuencias de números.
Para cada secuencia primero se indica la cantidad N de números que hay en la secuencia. A continuación viene la secuencia.

## Output

La secuencia de números resultante, separados por espacios en blanco

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int n1 = sc.nextInt();
    int[] a = new int[n1];
    for (int i = 0; i < n1; i++) {
        a[i] = sc.nextInt();
    }

    if (!sc.hasNextInt()) return;
    int n2 = sc.nextInt();
    int[] b = new int[n2];
    for (int i = 0; i < n2; i++) {
        b[i] = sc.nextInt();
    }

    int n = Math.min(n1, n2);
    for (int i = 0; i < n; i++) {
        if (i > 0) IO.print(" ");
        IO.print(a[i] + b[i]);
    }
    IO.println();
}
```

## Tests

### Test
```input
3    1 2 3
3    1 2 3
```
```output
2 4 6
```

### Test
```input
3    1 2 3
3    4 5 6
```
```output
5 7 9
```

### Test
```input
4    100 200 300 400
4    10 20 30 40
```
```output
110 220 330 440
```

### Test
```input
5    2 1 4 3 2
5    3 4 2 3 4
```
```output
5 5 6 6 6
```

### Test private
```input
1    10
1    10
```
```output
20
```
