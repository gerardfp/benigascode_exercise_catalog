---
slug: esquemes-acumuladors-producte
tags: [arrays, loops, for-loop, operators, arithmetic, accumulators]
difficulty: 3
---
# Acumuladors: producte de no-zeros

Escriu un programa que llegeix una seqüència de $N$ nombres enters i calcula el producte acumulat de tots els elements que siguin diferents de zero ($x \neq 0$). Si tots els elements són zero o $N = 0$, el resultat ha de ser `0`.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix el producte dels elements no nuls (o `0` si tots són zero).

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    long prod = 1;
    boolean hiHaNoZero = false;
    for (int i = 0; i < n; i++) {
        int x = sc.nextInt();
        if (x != 0) {
            prod *= x;
            hiHaNoZero = true;
        }
    }
    IO.println(hiHaNoZero ? prod : 0);
}
```

## Tests

### Test
```input
4
2
0
3
4
```
```output
24
```

### Test
```input
3
0
0
0
```
```output
0
```

### Test
```input
4
-2
3
-4
5
```
```output
120
```

### Test
```input
1
7
```
```output
7
```
