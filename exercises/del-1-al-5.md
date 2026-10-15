---
slug: del-1-al-5
difficulty: 5
---
# Del 1 al 5

Dada una secuencia de números, que termina con un 0, decir si contiene los números del 1 al 5.

Ej1:
1 2 3 4 5 6 0  => SI
1 2 3 4 0 => NO
9 1 8 2 7 3 6 4 5 0 => SI

## Input

La entrada consta de varios casos de prueba.
El primer número T indica el número de casos de prueba.
Cada caso de prueba consta de una secuencia de N números que termina con un 0.

## Output

Un "SI" o un "NO" por cada caso de prueba, separados por un salto de linea

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int t = sc.nextInt();
    for (int i = 0; i < t; i++) {
        boolean[] seen = new boolean[6];
        int num;
        while ((num = sc.nextInt()) != 0) {
            if (num >= 1 && num <= 5) {
                seen[num] = true;
            }
        }
        boolean allSeen = seen[1] && seen[2] && seen[3] && seen[4] && seen[5];
        IO.println(allSeen ? "SI" : "NO");
    }
}
```

## Tests

### Test
```input
1
1 2 3 4 5 0
```
```output
SI
```

### Test
```input
2
1 2 3 4 5 0
1 0
```
```output
SI
NO
```

### Test
```input
3
1 2 3 4 0
2 1 4 3 5 0
7 6 5 4 3 2 1 0
```
```output
NO
SI
SI
```

### Test private
```input
4
7 6 5 4 3 2 0
5 8 4 7 3 6 2 5 1 0
1 1 2 2 3 3 4 4 5 5 0
1 1 1 1 1 1 1 1 1 1 0
```
```output
NO
SI
SI
NO
```
