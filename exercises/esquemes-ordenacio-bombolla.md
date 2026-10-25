---
slug: esquemes-ordenacio-bombolla
difficulty: 4.0
tags: [arrays, loops, nested-loops, sorting]
---
# Ordenació: mètode de la bombolla (Bubble Sort)

Implementa l'algoritme d'ordenació de la bombolla (**Bubble Sort**) per ordenar un array de $N$ nombres enters en ordre creixent.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix els $N$ elements ordenats en ordre creixent en una única línia, separats per un espai.

## Plantillas

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] a = new int[n];
    for (int i = 0; i < n; i++) a[i] = sc.nextInt();

    // TODO: Implementa l'algorisme Bubble Sort amb dos bucles niats
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            // Compara i intercanvia si cal
        }
    }

    for (int i = 0; i < n; i++) {
        IO.print(a[i] + (i < n - 1 ? " " : "\n"));
    }
}
```

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] a = new int[n];
    for (int i = 0; i < n; i++) a[i] = sc.nextInt();

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
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
64
34
25
12
22
```
```output
12 22 25 34 64
```

### Test
```input
4
5
1
4
2
```
```output
1 2 4 5
```

### Test
```input
1
42
```
```output
42
```

### Test
```input
3
3
2
1
```
```output
1 2 3
```
