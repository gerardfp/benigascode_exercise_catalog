---
slug: esquemes-mescla-sense-duplicats
difficulty: 4.0
tags: [arrays, loops, while-loop, merge, two-pointers, filtering]
---
# Mescla: unió sense duplicats

Donats dos arrays de nombres enters ordenats en ordre creixent de mides $N$ i $M$, mescla'ls obtenint la seva unió en ordre creixent i sense cap element duplicat.

## Entrada

A la primera línia hi ha la mida $N$ del primer array, seguida dels seus $N$ enters ordenats.

A continuació hi ha la mida $M$ del segon array, seguida dels seus $M$ enters ordenats.

## Salida

Imprimeix els elements únics resultants de la unió en ordre creixent, separats per espais.

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
    int[] temp = new int[n + m];
    int k = 0;

    while (i < n && j < m) {
        int val;
        if (a[i] < b[j]) {
            val = a[i++];
        } else if (b[j] < a[i]) {
            val = b[j++];
        } else {
            val = a[i++];
            j++;
        }
        if (k == 0 || temp[k - 1] != val) {
            temp[k++] = val;
        }
    }
    while (i < n) {
        int val = a[i++];
        if (k == 0 || temp[k - 1] != val) {
            temp[k++] = val;
        }
    }
    while (j < m) {
        int val = b[j++];
        if (k == 0 || temp[k - 1] != val) {
            temp[k++] = val;
        }
    }

    for (int p = 0; p < k; p++) {
        IO.print(temp[p] + (p < k - 1 ? " " : "\n"));
    }
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
3
4
5
```
```output
1 3 4 5
```

### Test
```input
2
2
4
2
2
4
```
```output
2 4
```

### Test
```input
3
1
2
3
3
4
5
6
```
```output
1 2 3 4 5 6
```

### Test
```input
1
10
1
10
```
```output
10
```
