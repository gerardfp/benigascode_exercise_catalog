---
slug: esquemes-comptadors-parells
difficulty: 3.0
tags: [arrays, loops, for-loop, operators, modulo, counters]
---
# Comptadors: parells

Escriu un programa que llegix una sèrie de números, i compta quants són parells.

## Entrada

A la primera línia hi ha el número `N`, que indica la quantitat de números de la sèrie.

Després ve la sèrie de números, cadascun en una línia.

## Salida

Imprimix la quantitat de números parells.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int x = sc.nextInt();
        if (x % 2 == 0) {
            count++;
        }
    }
    IO.println(count);
}
```

## Tests

### Test
```input
4
101
200
301
400
```
```output
2
```

### Test
```input
4
444
333
111
222
```
```output
2
```

### Test
```input
5
24579
3241
45693
4567
355
```
```output
0
```
