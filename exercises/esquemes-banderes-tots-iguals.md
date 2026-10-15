---
slug: esquemes-banderes-tots-iguals
tags: [arrays, loops, for-loop, booleans, flags]
difficulty: 3
---
# Banderes: tots els elements iguals

Escriu un programa que determina si tots els elements d'una seqüència de $N$ nombres enters són iguals entre ells.

## Entrada

A la primera línia hi ha el número $N$ ($N \ge 1$).

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix `SI` si tots els elements són idèntics, o `NO` si hi ha algun valor diferent.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int primer = sc.nextInt();
    boolean totsIguals = true;
    for (int i = 1; i < n; i++) {
        int x = sc.nextInt();
        if (x != primer) {
            totsIguals = false;
        }
    }
    IO.println(totsIguals ? "SI" : "NO");
}
```

## Tests

### Test
```input
4
7
7
7
7
```
```output
SI
```

### Test
```input
4
7
7
8
7
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
1
2
3
```
```output
NO
```
