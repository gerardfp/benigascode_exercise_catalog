---
slug: teclado-robot
tags: [array]
---
# Teclado robot

![image](1613563726-2ffd5674a4-robotkeyboard.jpg)

Estamos diseñando un robot que sea capaz de escribir usando un teclado.

Para hacerlo más sencillo, hemos diseñado un teclado en el que todas las teclas están en la misma fila:

![image](1613564182-402650a000-laptop-keyboard-computer-isolated-black-key-button-vector-28503589.jpg)

El orden de las teclas es el siguiente:

```
"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"
```

El robot recibe órdenes de desplazarse a izquierda o derecha, y pulsa una tecla en cada movimiento. Es posible que alguna orden de desplazamiento pudiera provocar que el dedo del robot se situase fuera del teclado. En esos casos, el robot no pulsará ninguna tecla, pero su dedo no se moverá más allá de los límites del teclado, quedando sobre la letra `Q` o `M` según el caso. 

Dadas las órdenes de desplazamiento del dedo del robot, indica el texto que escribirá. La posición inicial del robot es `0`, correspondiente a la letra `Q`.

## Input

El primer número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica el número de órdenes de movimiento.

A continuación vienen las <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> órdenes de movimiento: un número positivo para las órdenes de desplazamiento a la derecha, y negativo para la izquierda.

## Output

Se imprimirá el texto final escrito por el robot.

## Tests

### Test
```input
4
16 -6 12 -12
```
```output
JAVA
```

### Test
```input
5
10 -7 0 7 -5 
```
```output
ARRAY
```

### Test
```input
8
11 -7 -50 3 4 50 -1 -10
```
```output
STRING
```

### Test
```input
7
-50 0 6 -50 2 1 2
```
```output
QUERY
```

### Test private
```input
10
50 50 0 -50 -50 10 -3 50 50 -1
```
```output
MAIN
```
