---
slug: esquemes-comptadors-divisibles
tags: [arrays, loops, for-loop, operators, modulo, counters]
difficulty: 3
---
# Comptadors: divisibles

Escriu un programa que llegix una sèrie de números, i un número divisor, i compta quants són divisibles per aquest divisor.

## Entrada

A la primera línia hi ha el número `N`, que indica la quantitat de números de la sèrie.

Després ve la sèrie de números, cadascun en una línea.

A la última línia hi ha el número divisor.

## Salida

Imprimix la quantitat de números divisibles pel divisor.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) {
        nums[i] = sc.nextInt();
    }
    int divisor = sc.nextInt();
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] % divisor == 0) {
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
13
27
17
29
3
```
```output
1
```

### Test
```input
4
425
333
111
225
5
```
```output
2
```

### Test
```input
10
24579
3241
45693
4567
355
4567
453435
56826
86863
3228565
12
```
```output
0
```
