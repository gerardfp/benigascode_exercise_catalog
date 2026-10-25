---
slug: esquemes-banderes-tots-positius
difficulty: 3.0
tags: [arrays, loops, for-loop, booleans, flags]
---
# Banderes: tots positius

Escriu un programa que determina si tots els elements d'una seqüència de $N$ nombres enters són estrictament positius ($> 0$).

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix `SI` si tots els elements són estrictament positius, o `NO` en cas contrari.

## Plantillas

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();

    boolean totsPositius = true;
    // TODO: Comprova si algun element és <= 0 i actualitza la bandera
    
    IO.println(totsPositius ? "SI" : "NO");
}
```

## Tests

### Test
```input
4
5
12
8
100
```
```output
SI
```

### Test
```input
4
5
-1
8
100
```
```output
NO
```

### Test
```input
3
1
0
3
```
```output
NO
```

### Test
```input
1
7
```
```output
SI
```
