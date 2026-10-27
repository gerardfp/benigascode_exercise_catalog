---
slug: esquemes-comptadors-paraules
difficulty: 4.0
tags: [arrays, strings, loops, for-loop, counters, search]
---
# Comptadors: paraules

Escriu un programa que llegix una sèrie de paraules, després llegeix una paraula a comparar, i compta quantes són iguals a esta última paraula.

## Entrada

A la primera línia hi ha el número `N`, que indica la quantitat de paraules.

Després venen les paraules, cadascuna en una línia.

Per últim ve la paraula a comparar.

## Salida

Imprimix la quantitat de paraules iguals a la paraula a comparar.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    String[] words = new String[n];
    for (int i = 0; i < n; i++) {
        words[i] = sc.next();
    }
    String target = sc.next();
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (words[i].equals(target)) {
            count++;
        }
    }
    IO.println(count);
}
```

## Tests

### Test
```input
4
hola
que
tal
estas
que
```
```output
1
```

### Test
```input
4
java
python
java
javascript
java
```
```output
2
```

### Test
```input
6
casa
coche
perro
casa
coche
gato
casa
```
```output
2
```
