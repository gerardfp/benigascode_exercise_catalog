---
slug: dos-secuencias-iguales
difficulty: 4.0
tags: [arrays, loops, for-loop, relational-operators, flags]
---
# Dues seqüències iguals

Donades dues seqüències de nombres, dir si són iguals.

## Input

La entrada consta de dues seqüències.

Per a cada seqüència, el primer nombre $N$ indica la quantitat de nombres de la seqüencia. A continuació ve la seqüència.

## Output

`true` si les seqüències són iguals

`false` si les seqüències no són iguals

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n1 = sc.nextInt();
    int[] a = new int[n1];
    for (int i = 0; i < n1; i++) {
        a[i] = sc.nextInt();
    }
    int n2 = sc.nextInt();
    int[] b = new int[n2];
    for (int i = 0; i < n2; i++) {
        b[i] = sc.nextInt();
    }
    if (n1 != n2) {
        IO.println(false);
        return;
    }
    boolean equal = true;
    for (int i = 0; i < n1; i++) {
        if (a[i] != b[i]) {
            equal = false;
            break;
        }
    }
    IO.println(equal);
}
```

## Tests

### Test
```input
3    1 2 3
3    1 2 3
```
```output
true
```

### Test
```input
3    100 200 300
3    100 200 300
```
```output
true
```

### Test
```input
3    100 200 300
4    100 200 300 400
```
```output
false
```

### Test
```input
5    1 2 3 4 5
5    1 2 3 4 5
```
```output
true
```

### Test
```input
5    1 2 3 4 5
5    1 2 3 4 4
```
```output
false
```

### Test
```input
3    23 34 45
2    23 45
```
```output
false
```

### Test
```input
5    1 2 3 4 5
1    5
```
```output
false
```

### Test
```input
1 3
1 5
```
```output
false
```

### Test private
```input
2 3 4
1 2
```
```output
false
```
