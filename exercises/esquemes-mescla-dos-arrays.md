---
slug: esquemes-mescla-dos-arrays
difficulty: 4.0
tags: [arrays, loops, while-loop, merge, two-pointers]
---
# Mescla: fusió de dos arrays ordenats

Donats dos arrays de nombres enters prèviament ordenats en ordre creixent, fusiona'ls en un únic array ordenat de mida $N+M$ utilitzant l'esquema de **mescla** (algorisme de dos punters en temps lineal $O(N+M)$).

## Entrada

A la primera línia hi ha la mida $N$ del primer array, seguida dels seus $N$ valors ordenats.

A continuació hi ha la mida $M$ del segon array, seguida dels seus $M$ valors ordenats.

## Salida

Imprimeix la seqüència fusionada ordenada en una sola línia, separada per espais.

## Plantillas

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] a = new int[n];
    for (int i = 0; i < n; i++) a[i] = sc.nextInt();

    int m = sc.nextInt();
    int[] b = new int[m];
    for (int i = 0; i < m; i++) b[i] = sc.nextInt();

    int[] res = new int[n + m];
    int i = 0, j = 0, k = 0;

    // TODO: Bucle de mescla amb dos punters
    while (i < n && j < m) {
        // ...
    }
    // TODO: bolcar elements restants
}
```

## Tests

### Test
```input
3
1
3
5
3
2
4
6
```
```output
1 2 3 4 5 6
```

### Test
```input
2
10
20
3
5
15
25
```
```output
5 10 15 20 25
```

### Test
```input
1
5
1
3
```
```output
3 5
```

### Test
```input
3
1
2
3
2
4
5
```
```output
1 2 3 4 5
```
