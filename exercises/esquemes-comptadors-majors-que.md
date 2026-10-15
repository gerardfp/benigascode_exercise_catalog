---
slug: esquemes-comptadors-majors-que
tags: [arrays, esquemes]
difficulty: 3
---
# Comptadors: majors que

Escriu un programa que llegix una sèrie de números, i un número mínim, i compta quants són majors que aquest mínim.

## Entrada

A la primera línia hi ha el número `N`, que indica la quantitat de números de la sèrie.

Després ve la sèrie de números, cadascun en una línia.

A la última línia hi ha el número mínim.

## Salida

Imprimix la quantitat de números majors que el mínim.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) {
        nums[i] = sc.nextInt();
    }
    int min = sc.nextInt();
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] > min) {
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
200
300
100
400
150
```
```output
3
```

### Test
```input
4
444
333
111
222
10
```
```output
4
```

### Test
```input
5
24579
3241
45693
4567
355
4567
```
```output
2
```
