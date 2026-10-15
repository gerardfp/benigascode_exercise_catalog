---
slug: esquemes-cerca-lineal-centinella
tags: [loops, while-loop, sentinel-loop, search, flags]
difficulty: 3
---
# Cerca lineal: cerca fins a centinella

Llegeix en primer lloc un valor objectiu $X$. Després llegeix una seqüència de nombres enters de longitud indeterminada que finalitza amb el valor centinella `0`. Determina si el valor $X$ apareix a la seqüència abans del zero final.

## Entrada

A la primera línia hi ha el valor enter $X$ ($X \neq 0$).

A continuació venen els nombres enters de la seqüència, un per línia, acabant amb un `0`.

## Salida

Imprimeix `SI` si $X$ ha aparegut abans del `0`, o `NO` en cas contrari.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int x = sc.nextInt();
    boolean trobat = false;
    while (sc.hasNextInt()) {
        int v = sc.nextInt();
        if (v == 0) break;
        if (v == x) {
            trobat = true;
        }
    }
    IO.println(trobat ? "SI" : "NO");
}
```

## Tests

### Test
```input
42
10
25
42
15
0
```
```output
SI
```

### Test
```input
7
1
2
3
4
0
```
```output
NO
```

### Test
```input
5
0
```
```output
NO
```

### Test
```input
-3
1
-3
0
```
```output
SI
```
