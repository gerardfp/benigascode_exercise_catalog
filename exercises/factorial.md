---
slug: factorial
tags: [recursion, operators, arithmetic, math]
difficulty: 3
---
# Factorial

Escriu un algorisme recursiu per a calcular el factorial d'un nombre:

Exemple

```
5! = 5*4*3*2*1 = 120
```

## Input

Un nombre enter

## Output

El factorial

## Solutions

```java
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int n = sc.nextInt();
    IO.println(factorial(n));
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
2
```
```output
2
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
120
```

### Test
```input
10
```
```output
3628800
```

### Test private
```input
15
```
```output
2004310016
```
