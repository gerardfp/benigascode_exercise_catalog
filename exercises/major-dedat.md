---
slug: major-dedat
tags: [operators, booleans, relational-operators]
difficulty: 1
---
# Major d'edat

Escriu un programa que llegeix l'edat d'una persona i diu si té al menys 18 anys.

## Input

un enter

## Output

-

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int age = sc.nextInt();
    IO.println(age >= 18);
}
```

## Tests

### Test
```input
17
```
```output
false
```

### Test
```input
18
```
```output
true
```

### Test
```input
19
```
```output
true
```

### Test
```input
1
```
```output
false
```

### Test private
```input
20
```
```output
true
```
