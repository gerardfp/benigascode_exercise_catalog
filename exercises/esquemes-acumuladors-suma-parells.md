---
slug: esquemes-acumuladors-suma-parells
tags: [arrays, loops, for-loop, operators, arithmetic, modulo, accumulators, filtering]
difficulty: 3
---
# Acumuladors: suma de parells positius

Escriu un programa que llegeix una seqüència de nombres enters i calcula la suma exclusiva dels nombres que siguin simultàniament **parells** i **estrictament positius** ($> 0$). Si no n'hi ha cap, la suma ha de ser `0`.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix la suma acumulada dels valors parells i positius.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int suma = 0;
    for (int i = 0; i < n; i++) {
        int x = sc.nextInt();
        if (x > 0 && x % 2 == 0) {
            suma += x;
        }
    }
    IO.println(suma);
}
```

## Tests

### Test
```input
5
4
-2
6
3
8
```
```output
18
```

### Test
```input
3
-4
-6
-8
```
```output
0
```

### Test
```input
4
1
3
5
7
```
```output
0
```

### Test
```input
4
2
4
6
0
```
```output
12
```
