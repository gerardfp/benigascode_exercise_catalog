---
slug: esquemes-acumuladors-suma-ponderada
tags: [arrays, loops, for-loop, operators, arithmetic, accumulators]
difficulty: 3
---
# Acumuladors: suma ponderada de dos vectors

Donats dos arrays de longitud $N$, el primer amb valors $V$ i el segon amb pesos enters $P$, calcula la suma ponderada del producte dels seus elements corresponents: $\sum_{i=0}^{N-1} (V[i] \times P[i])$.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres del vector de valors $V$.

Finalment venen els $N$ nombres del vector de pesos $P$.

## Salida

Imprimeix el valor de la suma ponderada.

## Plantillas

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] v = new int[n];
    for (int i = 0; i < n; i++) v[i] = sc.nextInt();

    int[] p = new int[n];
    for (int i = 0; i < n; i++) p[i] = sc.nextInt();

    // TODO: Calcula la suma ponderada
}
```

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] v = new int[n];
    for (int i = 0; i < n; i++) v[i] = sc.nextInt();
    int[] p = new int[n];
    for (int i = 0; i < n; i++) p[i] = sc.nextInt();

    long sumaPonderada = 0;
    for (int i = 0; i < n; i++) {
        sumaPonderada += (long) v[i] * p[i];
    }
    IO.println(sumaPonderada);
}
```

## Tests

### Test
```input
3
2
4
6
1
2
3
```
```output
28
```

### Test
```input
2
10
20
3
2
```
```output
70
```

### Test
```input
4
1
2
3
4
0
0
0
0
```
```output
0
```

### Test
```input
3
-1
5
2
3
2
4
```
```output
15
```
