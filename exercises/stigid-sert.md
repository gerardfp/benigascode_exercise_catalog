---
slug: stigid-sert
tags: [operators, arithmetic, modulo, math]
difficulty: 1
---
# stigid serT

Escriu un progarma que llegeixi un número de xifres, calcula un nou número invertint els dígits, i l'imprimeix.

## Input

Un enter de 3 xifres

## Output

-

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int n = sc.nextInt();
    int c = n % 10;
    int b = (n / 10) % 10;
    int a = n / 100;
    int res = c * 100 + b * 10 + a;
    IO.println(res);
}
```

## Tests

### Test
```input
976
```
```output
679
```

### Test
```input
123
```
```output
321
```

### Test
```input
320
```
```output
23
```

### Test
```input
100
```
```output
1
```

### Test private
```input
812
```
```output
218
```
