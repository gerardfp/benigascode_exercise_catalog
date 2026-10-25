---
slug: divisibles-per-3
difficulty: 2.0
tags: [loops, for-loop, conditionals, operators, modulo]
---
# Divisibles per 3

Imprimeix tots els nombres enters divisibles per 3 que hi ha entre $A$ i $B$ (inclusiu).

## Input

Dos nombres enters $A$ i $B$

## Output

S'imprimirà cada número en una línia.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    for (int i = a; i <= b; i++) {
        if (i % 3 == 0) {
            IO.println(i);
        }
    }
}
```

## Tests

### Test
```input
1 7
```
```output
3
6
```

### Test
```input
1 7
```
```output
3
6
```

### Test
```input
5 10
```
```output
6
9
```

### Test
```input
10 22
```
```output
12
15
18
21
```

### Test
```input
3 7
```
```output
3
6
```

### Test
```input
-1 3
```
```output
0
3
```

### Test
```input
12 45
```
```output
12
15
18
21
24
27
30
33
36
39
42
45
```

### Test
```input
99 102
```
```output
99
102
```

### Test private
```input
3 7
```
```output
3
6
```
