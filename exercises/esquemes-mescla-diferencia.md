---
slug: esquemes-mescla-diferencia
difficulty: 4.0
tags: [arrays, loops, while-loop, merge, two-pointers, filtering]
---
# Mescla: diferència d'arrays ordenats (A - B)

Donats dos arrays d'enters ordenats $A$ (de mida $N$) i $B$ (de mida $M$), calcula la diferència $A \setminus B$ (els elements que estan a $A$ però no a $B$) aprofitant que ambdós arrays estan ordenats mitjançant la tècnica de mescla en $O(N+M)$.

## Entrada

A la primera línia hi ha la mida $N$ del primer array $A$, seguida dels seus $N$ enters ordenats.

A continuació hi ha la mida $M$ del segon array $B$, seguida dels seus $M$ enters ordenats.

## Salida

Imprimeix els elements de $A \setminus B$ en ordre creixent separats per un espai. Si la diferència és buida, imprimeix una línia buida.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] a = new int[n];
    for (int i = 0; i < n; i++) a[i] = sc.nextInt();

    int m = sc.nextInt();
    int[] b = new int[m];
    for (int i = 0; i < m; i++) b[i] = sc.nextInt();

    int i = 0, j = 0;
    int[] res = new int[n];
    int k = 0;

    while (i < n && j < m) {
        if (a[i] < b[j]) {
            res[k++] = a[i++];
        } else if (a[i] > b[j]) {
            j++;
        } else {
            // són iguals: a[i] és a B, saltem tots els duplicats d'a[i]
            int val = a[i];
            while (i < n && a[i] == val) i++;
        }
    }
    while (i < n) {
        res[k++] = a[i++];
    }

    for (int p = 0; p < k; p++) {
        IO.print(res[p] + (p < k - 1 ? " " : ""));
    }
    IO.println();
}
```

## Tests

### Test
```input
5
1
2
3
4
5
2
2
4
```
```output
1 3 5
```

### Test
```input
3
1
2
3
3
1
2
3
```
```output

```

### Test
```input
3
5
10
15
2
1
2
```
```output
5 10 15
```

### Test
```input
4
1
3
5
7
3
3
5
9
```
```output
1 7
```
