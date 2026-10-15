---
slug: tres-iguales-seguidos
tags: [loops, while-loop, nested-loops, sentinel-loop, flags]
difficulty: 3
---
# Tres iguales seguidos

A partir de una serie de secuencias de números, decir si en cada una de ellas hay tres números iguales seguidos.

## Input

El primer número T indica la cantidad de secuencias que vienen a continuación.
Cada secuencia de N números termina con un 0.

## Output

Un "SI" o un "NO" por cada secuencia de números leída; separados por un salto de línea.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    for (int i = 0; i < t; i++) {
        boolean found = false;
        int prev = 0;
        int count = 0;
        while (true) {
            int num = sc.nextInt();
            if (num == 0) {
                break;
            }
            if (count == 0) {
                prev = num;
                count = 1;
            } else if (num == prev) {
                count++;
                if (count >= 3) {
                    found = true;
                }
            } else {
                prev = num;
                count = 1;
            }
        }
        if (found) {
            IO.println("SI");
        } else {
            IO.println("NO");
        }
    }
}
```

## Tests

### Test
```input
3
1 4 3 5 5 5 6 8 5 3 8 9 5 5 5 8 7 3 5 0
1 3 5 7 9 0
1 1 1 0
```
```output
SI
NO
SI
```

### Test private
```input
2
4 6 7 9 0
3 3 4 0
```
```output
NO
NO
```
