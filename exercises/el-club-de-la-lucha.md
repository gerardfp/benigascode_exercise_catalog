---
slug: el-club-de-la-lucha
difficulty: 7.0
tags: [arrays, loops]
---
# El club de la lucha

En el club de la lucha, los combatientes luchan hasta agotar sus fuerzas.

A partir de los nombres de todos los miembros del club y sus fuerzas, determina quien quedará en pie después de una serie de combates.

En cada combate, los dos luchadores pierden la misma cantidad de fuerza hasta que uno queda completamente agotado.

## Input

El primer número $N$ indica el número de luchadores.
A continuación vienen los $N$ nombres de cada luchador (una palabra).
A continuación vienen las $N$ fuerzas de cada luchador (un entero).

El siguiente número $C$ indica la cantidad de combates.
Por cada combate se indican los nombres de cada luchador.

## Output

Se imprimirán los nombres y las fuerzas de los luchadores que aun sigan en pie, cada uno en una línea, y con el formato: `nombre: fuerza`

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int n = sc.nextInt();
    String[] names = new String[n];
    for (int i = 0; i < n; i++) {
        names[i] = sc.next();
    }
    int[] strength = new int[n];
    for (int i = 0; i < n; i++) {
        strength[i] = sc.nextInt();
    }
    int m = sc.nextInt();
    for (int k = 0; k < m; k++) {
        String f1 = sc.next();
        String f2 = sc.next();
        int idx1 = -1, idx2 = -1;
        for (int i = 0; i < n; i++) {
            if (names[i].equals(f1)) idx1 = i;
            if (names[i].equals(f2)) idx2 = i;
        }
        if (idx1 != -1 && idx2 != -1) {
            int loss = Math.min(strength[idx1], strength[idx2]);
            strength[idx1] -= loss;
            strength[idx2] -= loss;
        }
    }
    for (int i = 0; i < n; i++) {
        if (strength[i] > 0) {
            IO.println(names[i] + ": " + strength[i]);
        }
    }
}
```

## Tests

### Test
```input
4
Richard Tyler Angel Bob 
20      10    30    15

3
Richard Tyler
Angel Bob
Richard Bob
```
```output
Richard: 10
Angel: 15
```

### Test
```input
5
AAA BBB CCC DDD EEE
60  40  20  50  30

5
AAA CCC
BBB DDD
EEE BBB
DDD AAA
CCC EEE
```
```output
AAA: 30
EEE: 30
```

### Test private
```input
10
A B C D E F G H I J
5 6 3 5 4 9 9 8 2 1

11
A B
C E
F I
J C
G D
H B
I A
F C
I B
J E
F H
```
```output
G: 4
```
