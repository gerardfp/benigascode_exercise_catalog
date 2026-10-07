---
slug: outline
---
# Outline

Dadas unas figuras, dibuja su contorno.

Los ángulos se marcarán con un `+`

Las líneas verticales con un `|`

Las líneas horizontales con un `-`

## Input

Los números  y  indican el ancho y alto del lienzo.

A continuación vienen los x píxeles:

Un símbolo `#` representa el relleno de la figura

Un símbolo `.` representa el fondo del lienzo.

## Output

Se imprimirá el lienzo resultante conforme los casos de prueba.

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

### Test
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
