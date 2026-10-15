---
slug: esquemes-comptadors-interval
tags: [arrays, loops, for-loop, operators, relational-operators, counters]
difficulty: 3
---
# Comptadors: nombres en un interval

Escriu un programa que llegeix una seqüència de nombres enters, i posteriorment dos valors $A$ i $B$, i compta quants nombres de la seqüència estan compresos dins de l'interval $[A, B]$ (és a dir, $A \le x \le B$).

## Entrada

A la primera línia hi ha el número $N$, que indica la quantitat de nombres de la seqüència.

A continuació venen els $N$ nombres enters, cadascun en una línia.

Per últim venen dos nombres enters $A$ i $B$ en una línia separats per un espai (amb $A \le B$), que defineixen l'interval tancat $[A, B]$.

## Salida

Imprimeix la quantitat de nombres de la seqüència que compleixen $A \le x \le B$.

## Plantillas

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) {
        nums[i] = sc.nextInt();
    }
    int a = sc.nextInt();
    int b = sc.nextInt();

    // TODO: Implementa el comptador per a l'interval [a, b]
}
```

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) {
        nums[i] = sc.nextInt();
    }
    int a = sc.nextInt();
    int b = sc.nextInt();
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] >= a && nums[i] <= b) {
            count++;
        }
    }
    IO.println(count);
}
```

## Tests

### Test
```input
5
10
25
5
30
15
10 25
```
```output
3
```

### Test
```input
4
1
2
3
4
10 20
```
```output
0
```

### Test
```input
6
-5
0
5
10
15
20
-5 5
```
```output
3
```

### Test
```input
3
7
7
7
7 7
```
```output
3
```
