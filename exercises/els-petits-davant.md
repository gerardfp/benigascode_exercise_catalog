---
slug: els-petits-davant
tags: [operadors, relacionals]
difficulty: 2
---
# Els petits davant

Escriu un programa que llegeixi tres números i digui si estan ordenats de menor a major.

## Input

tres números enters

## Output

`true` | `false`

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int a = sc.nextInt();
    int b = sc.nextInt();
    int c = sc.nextInt();
    IO.println(a <= b && b <= c);
}
```

## Tests

### Test
```input
1 2 3
```
```output
true
```

### Test
```input
1 3 2
```
```output
false
```

### Test
```input
2 1 3
```
```output
false
```

### Test
```input
2 3 1
```
```output
false
```

### Test
```input
3 1 2
```
```output
false
```

### Test
```input
3 2 1
```
```output
false
```

### Test
```input
1 1 1
```
```output
true
```

### Test
```input
1 1 2
```
```output
true
```

### Test
```input
1 2 1
```
```output
false
```

### Test
```input
1 2 2
```
```output
true
```

### Test
```input
10 1000 1000000
```
```output
true
```

### Test
```input
213 213 123
```
```output
false
```

### Test private
```input
100 100 1000
```
```output
true
```
