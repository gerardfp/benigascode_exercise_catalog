---
slug: el-club-de-la-lucha
---
# El club de la lucha

En el club de la lucha, los combatientes luchan hasta agotar sus fuerzas.

A partir de los nombres de todos los miembros del club y sus fuerzas, determina quien quedará en pie después de una serie de combates.

En cada combate, los dos luchadores pierden la misma cantidad de fuerza hasta que uno queda completamente agotado.

## Input

El primer número  indica el número de luchadores.
A continuación vienen los  nombres de cada luchador (una palabra).
A continuación vienen las  fuerzas de cada luchador (un entero).

El siguiente número  indica la cantidad de combates.
Por cada combate se indican los nombres de cada luchador.

## Output

Se imprimirán los nombres y las fuerzas de los luchadores que aun sigan en pie, cada uno en una línea, y con el formato: `nombre: fuerza`

## Plantillas

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
      	
      	
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

### Test
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
