---
slug: esquemes-extrems-rang
difficulty: 4.0
tags: [arrays, loops, for-loop, operators, arithmetic, min-max]
---
# Extrems: rang (màxim - mínim)

Escriu un programa que calcula el rang d'una seqüència de $N$ nombres enters, definit com la diferència entre el valor màxim i el valor mínim de la seqüència: $\text{rang} = \text{màxim} - \text{mínim}$.

## Entrada

A la primera línia hi ha el número $N$ ($N \ge 1$).

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix el rang de la seqüència.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();

    int min = nums[0];
    int max = nums[0];
    for (int i = 1; i < n; i++) {
        if (nums[i] < min) min = nums[i];
        if (nums[i] > max) max = nums[i];
    }
    IO.println(max - min);
}
```

## Tests

### Test
```input
5
10
2
8
15
3
```
```output
13
```

### Test
```input
4
5
5
5
5
```
```output
0
```

### Test
```input
3
-10
0
10
```
```output
20
```

### Test
```input
2
-5
-1
```
```output
4
```
