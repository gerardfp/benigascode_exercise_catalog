---
slug: suma-de-pares-y-producto-de-impares
difficulty: 3.0
tags: [loops, while-loop, operators, modulo, accumulators]
---
# Suma de parells i producte d'imparells

Escriu un programa que llegeixi una seqüència de números enters positius, i escrigui la suma dels números parells, el producte dels números imparells i la quantitat de números.

## Input

Una seqüència de números enters positius acabada en -1.

## Output

Imprimeix la suma dels números parells en una línia, en la següent línia el producte dels números imparells i en la següent línea el total de números llegits (sense comptar el -1).

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int sumEven = 0;
    int prodOdd = 1;
    int count = 0;
    while (sc.hasNextInt()) {
        int x = sc.nextInt();
        if (x == -1) break;
        count++;
        if (x % 2 == 0) {
            sumEven += x;
        } else {
            prodOdd *= x;
        }
    }
    IO.println(sumEven);
    IO.println(prodOdd);
    IO.println(count);
}
```

## Tests

### Test
```input
2 3 4 6 7 8 -1
```
```output
20
21
6
```

### Test
```input
9 8 7 6 -1
```
```output
14
63
4
```

### Test private
```input
7 4 8 1 2 3 7 3 -1
```
```output
14
441
8
```
