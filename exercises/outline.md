---
slug: outline
difficulty: 5.0
tags: [arrays, matrices, 2d-arrays, loops, nested-loops]
---
# Outline

Dadas unas figuras, dibuja su contorno.

Los ángulos se marcarán con un `+`

Las líneas verticales con un `|`

Las líneas horizontales con un `-`

## Input

Los números $M$ y $N$ indican el ancho y alto del lienzo.

A continuación vienen los $MxN$ píxeles:

Un símbolo `#` representa el relleno de la figura

Un símbolo `.` representa el fondo del lienzo.

## Output

Se imprimirá el lienzo resultante conforme los casos de prueba.

## Tests

### Test
```input
5 5
. . . . . 
. # # # .
. # # # .
. # # # .
. . . . . 
```
```output
. . . . .
. + - + .
. |   | .
. + - + .
. . . . .
```

### Test
```input
8 7
. . . . . . . .
. # # # # . . .
. # # # # . . .
. # # # # # # .
. # # # # # # .
. # # # # # # .
. . . . . . . . 
```
```output
. . . . . . . .
. + - - + . . .
. |     | . . .
. |     + - + .
. |         | .
. + - - - - + .
. . . . . . . . 
```

### Test
```input
6 7
. . . . . .
# # # # # .
# # # # # .
# # # # # .
. . # # # .
. . # # # .
. . . . . .
```
```output
. . . . . .
+ - - - + .
|       | .
+ - +   | .
. . |   | .
. . + - + .
. . . . . .
```

### Test
```input
7 5
# # # # # . .
# # # # # . .
# # # # # # #
. . # # # # #
. . # # # # #
```
```output
+ - - - + . .
|       | . .
+ - +   + - +
. . |       |
. . + - - - +
```

### Test
```input
13 15
. . . . . . . . . . . . .
. . . # # # . # # # . . .
. . . # # # . # # # . . . 
. # # # # # # # # # # # .
. # # # # # # # # # # # .
. # # # # # # # # # # # .
. . . # # # . # # # . . .
. . . # # # . # # # . . .
. . . # # # . # # # . . .
. # # # # # # # # # # # .
. # # # # # # # # # # # .
. # # # # # # # # # # # .
. . . # # # . # # # . . .
. . . # # # . # # # . . .
. . . . . . . . . . . . .
```
```output
. . . . . . . . . . . . .
. . . + - + . + - + . . .
. . . |   | . |   | . . . 
. + - +   + - +   + - + .
. |                   | .
. + - +   + - +   + - + .
. . . |   | . |   | . . .
. . . |   | . |   | . . .
. . . |   | . |   | . . .
. + - +   + - +   + - + .
. |                   | .
. + - +   + - +   + - + .
. . . |   | . |   | . . .
. . . + - + . + - + . . .
. . . . . . . . . . . . .
```

### Test private
```input
11 13
. . # # # . # # # . .
. . # # # . # # # . . 
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
. . # # # . # # # . .
. . # # # . # # # . .
. . # # # . # # # . .
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
. . # # # . # # # . .
. . # # # . # # # . .
```
```output
. . + - + . + - + . .
. . |   | . |   | . . 
+ - +   + - +   + - +
|                   |
+ - +   + - +   + - +
. . |   | . |   | . .
. . |   | . |   | . .
. . |   | . |   | . .
+ - +   + - +   + - +
|                   |
+ - +   + - +   + - +
. . |   | . |   | . .
. . + - + . + - + . .
```
