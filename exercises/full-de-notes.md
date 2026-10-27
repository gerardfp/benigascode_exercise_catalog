---
slug: full-de-notes
difficulty: 4.0
tags: [loops, while-loop, accumulators, min-max]
---
# Full de notes

![image](assets/full-de-notes-img0.png)

## Input

La entrada és la matriu de notes

## Output

S'imprimirà la matriu de notes, afegint la columna de la mitjana.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int rows = sc.nextInt();
    int cols = sc.nextInt();
    for (int r = 0; r < rows; r++) {
        float sum = 0;
        for (int c = 0; c < cols; c++) {
            int val = sc.nextInt();
            sum += val;
            IO.print(val + " ");
        }
        IO.println(sum / cols);
    }
}
```

## Tests

### Test
```input
3 4
4 6 5 5
8 8 6 6
4 5 6 5
```
```output
4 6 5 5 5.0
8 8 6 6 7.0
4 5 6 5 5.0
```

### Test
```input
4 3
4 6 5
8 8 6
4 5 6
9 6 5
```
```output
4 6 5 5.0
8 8 6 7.3333335
4 5 6 5.0
9 6 5 6.6666665
```

### Test
```input
2 6
4 6 5 8 8 6
4 5 6 9 6 5
```
```output
4 6 5 8 8 6 6.1666665
4 5 6 9 6 5 5.8333335
```

### Test private
```input
2 2
4 6
4 5
```
```output
4 6 5.0
4 5 4.5
```
