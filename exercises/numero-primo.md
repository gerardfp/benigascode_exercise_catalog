---
slug: numero-primo
difficulty: 3.0
tags: [loops, for-loop, math, flags]
---
# Determinar si un número es primo

Un número entero mayor que 1 es **primo** si únicamente es divisible de manera exacta entre 1 y entre sí mismo. Los números menores o iguales a 1 no se consideran primos.


## Input
Un único número entero `N` leído desde la entrada estándar.

## Output
La palabra `PRIMO` o `NO_PRIMO` en una única línea.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    if (n <= 1) {
        IO.println("NO_PRIMO");
        return;
    }
    boolean isPrime = true;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime) {
        IO.println("PRIMO");
    } else {
        IO.println("NO_PRIMO");
    }
}
```

## Tests

### Test
```input
7
```
```output
PRIMO
```

### Test
```input
12
```
```output
NO_PRIMO
```

### Test
```input
1
```
```output
NO_PRIMO
```

### Test
```input
997
```
```output
PRIMO
```

### Test
```input
0
```
```output
NO_PRIMO
```

### Test
```input
-1
```
```output
NO_PRIMO
```
