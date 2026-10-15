---
slug: esquemes-ordenacio-intercanvis
tags: [arrays, loops, nested-loops, sorting, counters]
difficulty: 4
---
# Ordenació: comptador d'intercanvis en Bubble Sort

Ordena un array de $N$ nombres enters utilitzant el mètode de la bombolla (**Bubble Sort**) i compta el nombre total d'intercanvis (swaps) de posicions que cal realitzar fins a deixar l'array ordenat en ordre creixent.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix el nombre total d'intercanvis efectuats.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] a = new int[n];
    for (int i = 0; i < n; i++) a[i] = sc.nextInt();

    int swaps = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                int tmp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = tmp;
                swaps++;
            }
        }
    }
    IO.println(swaps);
}
```

## Tests

### Test
```input
3
3
2
1
```
```output
3
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
0
```

### Test
```input
4
4
3
2
1
```
```output
6
```

### Test
```input
3
1
3
2
```
```output
1
```
