---
slug: esquemes-cerca-lineal-primer-parell
tags: [arrays, loops, for-loop, operators, modulo, search]
difficulty: 3
---
# Cerca lineal: primer nombre parell

Donada una seqüència de $N$ nombres enters, cerca i imprimeix el valor del primer nombre parell que aparegui. Si no hi ha cap nombre parell, imprimeix la paraula `CAP`.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix el primer nombre parell trobat o la paraula `CAP`.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    boolean trobat = false;
    int resultat = 0;
    for (int i = 0; i < n; i++) {
        int x = sc.nextInt();
        if (x % 2 == 0) {
            resultat = x;
            trobat = true;
            break;
        }
    }
    if (trobat) {
        IO.println(resultat);
    } else {
        IO.println("CAP");
    }
}
```

## Tests

### Test
```input
4
1
3
8
5
```
```output
8
```

### Test
```input
3
1
3
5
```
```output
CAP
```

### Test
```input
4
4
2
6
8
```
```output
4
```

### Test
```input
1
0
```
```output
0
```
