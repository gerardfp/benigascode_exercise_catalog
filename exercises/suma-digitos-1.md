---
slug: suma-digitos-1
tags: [strings, loops]
difficulty: 2
---
# Suma dígitos 1

Dado un número entero positivo, realiza la suma de sus dígitos.

## Input

Un número entero positvo N.

## Output

Un número entero

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    String s = sc.next();
    int sum = 0;
    for (int i = 0; i < s.length(); i++) {
        sum += s.charAt(i) - '0';
    }
    IO.println(sum);
}
```

## Tests

### Test
```input
123
```
```output
6
```

### Test
```input
11111
```
```output
5
```

### Test
```input
100000
```
```output
1
```

### Test
```input
2147483647
```
```output
46
```

### Test private
```input
1
```
```output
1
```
