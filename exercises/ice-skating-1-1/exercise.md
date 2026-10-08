---
slug: ice-skating-1-1
---
# Ice skating

![image](ice-skating-1-1-img5.png)

En un videojuego hay un mapa en forma de tablero con unas flechas en algunas casillas que apuntan en una dirección: Norte, Sur, Este y Oeste.

![image](ice-skating-1-1-img4.png)

El personaje empieza en la casilla 0,0, y desliza en la dirección de la flecha hasta que encuentra otra flecha, y entonces desliza en la dirección de esa flecha. Y así sucesivamente hasta que en un momento dado sale del tablero.

## Input

Los dos primeros números  y  indican el ancho y alto del tablero.

A continuación viene la definición del tablero:

- Un caracter `.` indica que la casilla no tiene flecha

- En las casillas con flecha se indica su dirección: `N`, `S`, `E`, `W`

## Output

Indicar las coordenadas (x y) de la última casilla del tablero por la cual sale el personaje.

## Tests

### Test
```input
4 4
E . . S
. . . .
. . S W
. . E .
```
```output
3 3
```

### Test
```input
5 4
S . . N .
. E . . .
S N W . S
E . N . W
```
```output
4 1
```

### Test
```input
4 6
E . E S
. N . .
. S . .
. S . W
. . W E
. W . .
```
```output
0 5
```
