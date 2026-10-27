---
slug: esquemes-cerca-binaria-verificacio
difficulty: 7.0
tags: [arrays, loops, while-loop, nested-loops, search, flags]
---
# Cerca binària: consultes d'existència múltiples

Donat un array de $N$ enters ordenats en ordre creixent i una llista de $Q$ consultes independents, respon per a cadascuna d'elles si el número consultat és present a l'array mitjançant cerca binària.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters ordenats.

Després hi ha el número $Q$, que indica la quantitat de consultes.

Finalment venen els $Q$ valors a consultar, cadascun en una línia.

## Salida

Per a cadascuna de les $Q$ consultes, imprimeix `SI` si el número existeix a l'array o `NO` en cas contrari.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();

    int q = sc.nextInt();
    for (int k = 0; k < q; k++) {
        int x = sc.nextInt();
        int left = 0, right = n - 1;
        boolean trobat = false;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == x) {
                trobat = true;
                break;
            } else if (nums[mid] < x) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        IO.println(trobat ? "SI" : "NO");
    }
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
3
20
25
50
```
```output
SI
NO
SI
```

### Test
```input
3
1
3
5
2
2
4
```
```output
NO
NO
```

### Test
```input
1
42
1
42
```
```output
SI
```
