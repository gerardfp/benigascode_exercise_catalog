---
slug: suma-els-n-primers-nombres
tags: [recursion, operators, arithmetic, math]
difficulty: 2
---
# Suma els n primers nombres

Escriu un algorisme recursiu per a sumar els n primers nombres.

Exemple:

```
n=10 -> 1+2+3+4+5+6+7+8+9+10=55
```

## Input

Un nombre enter

## Output

La suma

## Solutions

```java
int sum(int n) {
    if (n <= 1) return n;
    return n + sum(n - 1);
}

void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    IO.println(sum(n));
}
```

## Tests

### Test
```input
1
```
```output
1
```

### Test
```input
1
```
```output
1
```

### Test
```input
3
```
```output
6
```

### Test
```input
5
```
```output
15
```

### Test
```input
10
```
```output
55
```

### Test
```input
20
```
```output
210
```

### Test private
```input
1000
```
```output
500500
```
