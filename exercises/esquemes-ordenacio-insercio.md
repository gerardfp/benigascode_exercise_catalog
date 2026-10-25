---
slug: esquemes-ordenacio-insercio
difficulty: 4.0
tags: [arrays, loops, nested-loops, while-loop, sorting]
---
# Ordenació: inserció directa (Insertion Sort)

Implementa l'algoritme d'ordenació per **inserció directa** (**Insertion Sort**) per ordenar un array de $N$ nombres enters en ordre creixent.

En cada pas $i$, desplaça els elements majors cap a la dreta i insereix l'element actual a la seva posició correcta.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix els $N$ elements ordenats en ordre creixent en una única línia, separats per un espai.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] a = new int[n];
    for (int i = 0; i < n; i++) a[i] = sc.nextInt();

    for (int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }

    for (int i = 0; i < n; i++) {
        IO.print(a[i] + (i < n - 1 ? " " : "\n"));
    }
}
```

## Tests

### Test
```input
6
12
11
13
5
6
7
```
```output
5 6 7 11 12 13
```

### Test
```input
4
9
7
5
3
```
```output
3 5 7 9
```

### Test
```input
3
2
2
1
```
```output
1 2 2
```

### Test
```input
1
15
```
```output
15
```
