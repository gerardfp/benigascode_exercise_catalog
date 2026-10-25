---
slug: esquemes-extrems-segon-maxim
difficulty: 4.0
tags: [arrays, loops, for-loop, operators, relational-operators, min-max]
---
# Extrems: segon màxim

Escriu un programa que troba el segon valor més gran estrictament diferent del màxim en una seqüència de $N$ nombres enters.

Es garanteix que a l'entrada hi ha almenys dos valors numèrics diferents.

## Entrada

A la primera línia hi ha el número $N$ ($N \ge 2$).

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix el segon valor màxim estricte de la seqüència.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();

    int max1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        if (nums[i] > max1) {
            max1 = nums[i];
        }
    }
    int max2 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        if (nums[i] != max1 && nums[i] > max2) {
            max2 = nums[i];
        }
    }
    IO.println(max2);
}
```

## Tests

### Test
```input
5
10
40
20
40
30
```
```output
30
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
3
```

### Test
```input
3
-10
-5
-20
```
```output
-10
```

### Test
```input
5
100
50
100
75
25
```
```output
75
```
