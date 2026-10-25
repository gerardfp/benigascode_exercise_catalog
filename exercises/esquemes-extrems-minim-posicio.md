---
slug: esquemes-extrems-minim-posicio
difficulty: 3.0
tags: [arrays, loops, for-loop, operators, relational-operators, min-max]
---
# Extrems: mínim i la seva posició

Escriu un programa que troba el valor mínim d'una seqüència de $N$ nombres enters i l'índex (posició base 0) de la seva primera aparició.

## Entrada

A la primera línia hi ha el número $N$ ($N \ge 1$).

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix dos nombres separats per un espai: el valor mínim i la posició (índex de 0 a $N-1$) on apareix per primer cop.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();

    int min = nums[0];
    int posMin = 0;
    for (int i = 1; i < n; i++) {
        if (nums[i] < min) {
            min = nums[i];
            posMin = i;
        }
    }
    IO.println(min + " " + posMin);
}
```

## Tests

### Test
```input
5
40
10
25
5
30
```
```output
5 3
```

### Test
```input
4
3
8
1
9
```
```output
1 2
```

### Test
```input
3
-20
-5
-20
```
```output
-20 0
```

### Test
```input
1
42
```
```output
42 0
```
