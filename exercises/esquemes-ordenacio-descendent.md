---
slug: esquemes-ordenacio-descendent
difficulty: 4.0
tags: [arrays, loops, nested-loops, sorting]
---
# Ordenació: ordre descendent

Donat un array de $N$ nombres enters, ordena'l en ordre **descendent** (és a dir, de major a menor).

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix els $N$ elements ordenats de major a menor en una línia, separats per un espai.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] a = new int[n];
    for (int i = 0; i < n; i++) a[i] = sc.nextInt();

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] < a[j + 1]) {
                int tmp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = tmp;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        IO.print(a[i] + (i < n - 1 ? " " : "\n"));
    }
}
```

## Tests

### Test
```input
5
10
40
20
50
30
```
```output
50 40 30 20 10
```

### Test
```input
4
1
2
3
4
```
```output
4 3 2 1
```

### Test
```input
3
-5
10
0
```
```output
10 0 -5
```

### Test
```input
1
99
```
```output
99
```
