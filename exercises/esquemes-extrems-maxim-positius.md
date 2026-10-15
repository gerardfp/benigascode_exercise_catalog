---
slug: esquemes-extrems-maxim-positius
tags: [arrays, loops, for-loop, operators, relational-operators, min-max, filtering]
difficulty: 3
---
# Extrems: màxim dels positius

Escriu un programa que troba el valor més gran exclusivament entre els nombres estrictament positius ($> 0$) d'una seqüència de $N$ nombres enters. Si a la seqüència no hi ha cap nombre positiu, ha d'imprimir la paraula `CAP`.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix el valor màxim dels positius, o el text `CAP` si no n'hi ha cap.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int maxPos = -1;
    boolean trobat = false;
    for (int i = 0; i < n; i++) {
        int x = sc.nextInt();
        if (x > 0) {
            if (!trobat || x > maxPos) {
                maxPos = x;
                trobat = true;
            }
        }
    }
    if (trobat) {
        IO.println(maxPos);
    } else {
        IO.println("CAP");
    }
}
```

## Tests

### Test
```input
5
-10
25
-5
30
-2
```
```output
30
```

### Test
```input
4
-1
-2
-3
0
```
```output
CAP
```

### Test
```input
3
10
20
15
```
```output
20
```

### Test
```input
1
5
```
```output
5
```
