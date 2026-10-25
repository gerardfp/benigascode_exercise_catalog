---
slug: numero-de-divisores
difficulty: 2.0
tags: [loops, for-loop, operators, modulo, math, counters]
---
# Número de divisores

Dado un número, calcula la cantidad de divisores que tiene.

## Input

Un número entero N

## Output

Un número indicando la cantidad de divisores

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    if (n <= 0) {
        IO.println(0);
        return;
    }
    int count = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            count++;
        }
    }
    IO.println(count);
}
```

## Tests

### Test
```input
6
```
```output
4
```
#### Explanation
El 6 es divisible por 1, 2, 3 y 6

### Test
```input
12
```
```output
6
```
#### Explanation
El 12 es divisible por 1, 2, 3, 4, 6 y 12

### Test
```input
17
```
```output
2
```
#### Explanation
El 17 es divisible por 1 y 17

### Test
```input
0
```
```output
0
```

### Test
```input
1
```
```output
1
```

### Test
```input
2
```
```output
2
```

### Test
```input
60
```
```output
12
```

### Test
```input
5160
```
```output
32
```

### Test
```input
9985
```
```output
4
```

### Test
```input
9973
```
```output
2
```

### Test private
```input
3
```
```output
2
```
