---
slug: del-reves
difficulty: 3.0
tags: [arrays, loops, for-loop, reverse]
---
# Del revés

Donada una seqüència de números, mostrar-la en ordre invers.

## Input

El primer número $N$ indica la quantitat de números que hi ha en la seqüència. 

A continuació venen els números de la seqüència.

## Output

La seqüència de números en ordre invers, separats per espais.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int n = sc.nextInt();
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
        arr[i] = sc.nextInt();
    }
    for (int i = n - 1; i >= 0; i--) {
        IO.print(arr[i] + (i > 0 ? " " : ""));
    }
    IO.println();
}
```

## Tests

### Test
```input
2 23 45
```
```output
45 23
```

### Test
```input
5 
100 200 300 400 500
```
```output
500 400 300 200 100
```

### Test
```input
3 
23 56 45
```
```output
45 56 23
```

### Test
```input
1 
1000
```
```output
1000
```

### Test private
```input
10 
3 1 4 2 6 5 4 7 6 9
```
```output
9 6 7 4 5 6 2 4 1 3
```
