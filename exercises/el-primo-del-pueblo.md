---
slug: el-primo-del-pueblo
difficulty: 4.0
tags: [loops, for-loop, math, flags]
---
# El primo del pueblo

Dado un número, di si es primo o no.

## Input

Un número $N$

## Output

`true` | `false`

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    if (n < 2) {
        IO.println(false);
        return;
    }
    boolean prime = true;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            prime = false;
            break;
        }
    }
    IO.println(prime);
}
```

## Tests

### Test
```input
4
```
```output
false
```

### Test
```input
7
```
```output
true
```

### Test
```input
3
```
```output
true
```

### Test
```input
2
```
```output
true
```

### Test
```input
9
```
```output
false
```

### Test
```input
29
```
```output
true
```

### Test
```input
13
```
```output
true
```

### Test
```input
15
```
```output
false
```

### Test
```input
31
```
```output
true
```

### Test private
```input
6
```
```output
false
```
