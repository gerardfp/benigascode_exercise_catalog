---
slug: esquemes-cerca-binaria-basica
tags: [arrays, loops, while-loop, search]
difficulty: 4
---
# Cerca binària: índex en array ordenat

Donat un array de $N$ nombres enters **ordenats en ordre creixent** i un valor objectiu $X$, implementa l'algoritme de **cerca binària** per trobar l'índex (posició base 0) de $X$. Si no hi apareix, imprimeix `-1`.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters ordenats en ordre creixent.

A l'última línia hi ha el valor objectiu $X$.

## Salida

Imprimeix l'índex on es troba $X$, o `-1` si no existeix.

## Plantillas

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
    int x = sc.nextInt();

    int left = 0;
    int right = n - 1;
    int pos = -1;

    // TODO: Implementa el bucle while de la cerca binària
    
    IO.println(pos);
}
```

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
    int x = sc.nextInt();

    int left = 0;
    int right = n - 1;
    int pos = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == x) {
            pos = mid;
            break;
        } else if (nums[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    IO.println(pos);
}
```

## Tests

### Test
```input
5
10
20
30
40
50
30
```
```output
2
```

### Test
```input
6
2
4
6
8
10
12
5
```
```output
-1
```

### Test
```input
1
42
42
```
```output
0
```

### Test
```input
4
1
3
5
7
7
```
```output
3
```
