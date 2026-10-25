---
slug: fireball
difficulty: 3.0
tags: [arrays, loops]
---
# Fireball

![image](assets/fireball-img0.png)

En un videojoc els enemics es disposen en una fila. El jugador els hi pot llançar boles de foc i provocar un dany a l'enemic en el qual impacta i també als que estiguin a l'abast de la bola de foc.

Cada enemic té un nivell de vida, i quan els alcança la bola de foc els hi resta una quantitat determinada de vida. Quan un enemic té nivell zero, ja no se li pot restar més vida.

## Input

- El primer nombre $N$ indica la quantitat d'enemics.
- A continuació venen els nivells de vida de cadascun dels $N$ enemics.
- Després venen les dades de les boles de foc. Tres números per cada bola de foc:

    - El primer nombre $P$ indica la posició (començant per `0`) de l'enemic al qual impacta la bola de foc
    - El segon nombre $R$ indica l'abast de la bola de foc
    - El tercer nombre $D$ indica el dany que causa la bola de foc.

- L'entrada finalitza amb tres `-1`

<p>Per exemple, la següent bola de foc impacta a l'enemic en la posició `4` i té un abast `2`:

![image](assets/fireball-img1.png)

## Output

Per cada bola llançada, s'imprimirà en una nova línia el nivell de vida resultant dels enemics, separats per espais.

## Tests

### Test
```input
5
100 50 30 20 10
1 1 10
2 2 5
-1 -1 -1
```
```output
90 40 20 20 10
85 35 15 15 5
```

### Test
```input
3 
50 50 50
1 0 25
-1 -1 -1
```
```output
50 25 50
```

### Test
```input
3
30 10 30
1 1 10
1 1 10
1 1 10
-1 -1 -1
```
```output
20 0 20
10 0 10
0 0 0
```

### Test private
```input
5
100 100 100 100 100
2 0 10
2 1 10
2 2 10
2 3 10
-1 -1 -1
```
```output
100 100 90 100 100
100 90 80 90 100
90 80 70 80 90
80 70 60 70 80
```
