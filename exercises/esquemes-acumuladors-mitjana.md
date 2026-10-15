---
slug: esquemes-acumuladors-mitjana
tags: [arrays, loops, for-loop, operators, arithmetic, accumulators, formatting]
difficulty: 3
---
# Acumuladors: mitjana aritmètica

Escriu un programa que llegeix una seqüència de nombres enters i en calcula la mitjana aritmètica exacta amb dos decimals de precisió.

## Entrada

A la primera línia hi ha el número $N$ ($N \ge 1$).

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix la mitjana aritmètica formatada amb 2 decimals (`%.2f`).

## Solutions

```java
void main() {
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    double suma = 0;
    for (int i = 0; i < n; i++) {
        suma += sc.nextInt();
    }
    double mitjana = suma / n;
    IO.println(String.format(Locale.US, "%.2f", mitjana));
}
```

## Tests

### Test
```input
4
5
7
8
10
```
```output
7.50
```

### Test
```input
3
1
2
3
```
```output
2.00
```

### Test
```input
2
4
5
```
```output
4.50
```

### Test
```input
1
9
```
```output
9.00
```
