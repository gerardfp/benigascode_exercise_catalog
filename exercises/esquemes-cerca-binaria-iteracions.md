---
slug: esquemes-cerca-binaria-iteracions
difficulty: 4.0
tags: [arrays, loops, while-loop, search, counters]
---
# Cerca binària: comptador d'iteracions

Donat un array de $N$ nombres enters ordenats en ordre creixent i un valor objectiu $X$, compta quantes iteracions del bucle de cerca binària es realitzen fins a trobar $X$ o fins a comprovar que no és present (calculant el punt mig amb `mid = left + (right - left) / 2`).

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters ordenats en ordre creixent.

A l'última línia hi ha el valor objectiu $X$.

## Salida

Imprimeix el nombre total d'iteracions realitzades.

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
    int iteracions = 0;
    while (left <= right) {
        iteracions++;
        int mid = left + (right - left) / 2;
        if (nums[mid] == x) {
            break;
        } else if (nums[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    IO.println(iteracions);
}
```

## Tests

### Test
```input
7
1
2
3
4
5
6
7
4
```
```output
1
```

### Test
```input
7
1
2
3
4
5
6
7
1
```
```output
3
```

### Test
```input
4
10
20
30
40
25
```
```output
2
```

### Test
```input
1
100
100
```
```output
1
```
