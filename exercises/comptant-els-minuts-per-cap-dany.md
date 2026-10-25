---
slug: comptant-els-minuts-per-cap-dany
difficulty: 1.0
tags: [operators, arithmetic, modulo]
---
# Comptant els minuts per cap d'any

Ramon es passa el dia de cap d'any mirant el rellotge comptant els minuts que falten per al raïm.

## Input

El primer nombre $H$ indica les hores que marca el rellotge

El segon nombre $M$ indica els minuts que marca el rellotge

## Output

Els minuts que falten per a les campanades.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int h = sc.nextInt();
    int m = sc.nextInt();
    int remaining = 1440 - (h * 60 + m);
    IO.println(remaining);
}
```

## Tests

### Test
```input
23 59
```
```output
1
```
#### Explanation
Falta 1 minut per a les campanades

### Test
```input
23 59
```
```output
1
```

### Test
```input
23 00
```
```output
60
```
#### Explanation
Queden 1440 minuts (tot el dia)

### Test
```input
00 00
```
```output
1440
```

### Test private
```input
12 33
```
```output
687
```
