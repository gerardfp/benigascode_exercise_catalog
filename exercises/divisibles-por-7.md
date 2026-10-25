---
slug: divisibles-por-7
difficulty: 2.0
tags: [loops, while-loop, conditionals, operators, modulo]
---
# Divisibles por 7

A partir de una secuencia de números, decir si cada uno de ellos es divisible por 7 o no.

## Input

Una secuencia de (N) números terminada en 0.

## Output

Un "SI" o un "NO" por cada número leído.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNextInt()) {
        int n = sc.nextInt();
        if (n == 0) {
            break;
        }
        if (n % 7 == 0) {
            IO.println("SI");
        } else {
            IO.println("NO");
        }
    }
}
```

## Tests

### Test
```input
7 4 14 3 21 49 0
```
```output
SI
NO
SI
NO
SI
SI
```

### Test
```input
 7 0
```
```output
SI
```

### Test private
```input
4 4 0
```
```output
NO
NO
```
