---
slug: esquemes-banderes-elements-unics
difficulty: 4.0
tags: [arrays, loops, nested-loops, booleans, flags]
---
# Banderes: elements únics sense duplicats

Escriu un programa que comprova si tots els elements d'una seqüència de $N$ nombres enters són únics entre si (és a dir, no hi ha cap nombre repetit a la seqüència).

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix `SI` si tots els elements són únics, o `NO` si n'hi ha algun de duplicat.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();

    boolean totsUnics = true;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] == nums[j]) {
                totsUnics = false;
                break;
            }
        }
        if (!totsUnics) break;
    }
    IO.println(totsUnics ? "SI" : "NO");
}
```

## Tests

### Test
```input
4
1
5
9
12
```
```output
SI
```

### Test
```input
5
1
5
9
5
12
```
```output
NO
```

### Test
```input
1
42
```
```output
SI
```

### Test
```input
3
7
7
7
```
```output
NO
```
