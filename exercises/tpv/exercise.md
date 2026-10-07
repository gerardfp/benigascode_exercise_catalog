---
slug: tpv
tags: [array]
---
# TPV

![image](1613469413-94063dea8e-tpv.jpg)

Estamos desarrollando una aplicación para un Terminal de Punto de Venta de un restaurante de comida rápida.

El cliente va seleccionando los productos que desea pedir y el terminal le muestra el precio total del pedido.

## Input

En primer lugar se indican los datos de la carta de productos:

- El primer número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"></path></g></svg></span> indica la cantidad de productos disponibles en la carta.
- A continuación vienen los <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> nombres de cada producto (una palabra)
- A continuación vienen los <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-3-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> precios de cada producto (float)

<p>Luego vienen los datos del pedido:

- El primer número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-4-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.745ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 751.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"></path></g></svg></span> indica la cantidad de líneas que hay en el pedido
- Por cada línea se indica, el nombre del producto y la cantidad de unidades pedidas

<p>En el pedido puede haber productos repetidos en distintas líneas.

## Output

Se imprimirá el precio total del pedido en formato float.

## Plantillas

```java
import java.util.Locale;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.ENGLISH);
      	
      	
    }
}
```

## Tests

### Test
```input
5
Hamburguesa Refresco Patatas Ensalada Tarta
4           1        2       3        5

3
Hamburguesa 2
Refresco 2
Tarta 1
```
```output
15.0
```
```explanation
2*4 + 2*1 + 1*5 = 15
```

### Test
```input
3
Pizza Frankfurt Sandwich
4     2.5       1.25   

2
Pizza 3
Frankfurt 2
```
```output
17.0
```
```explanation
3*4 + 2.5*2 = 17
```

### Test
```input
6
Pizza Burguer Hotdog Chips Kebab Burrito
4.25  3.75    2.25   0.75  3.5   3.5

4
Pizza 2
Burguer 2
Hotdog 3
Burrito 1
```
```output
26.25
```

### Test private
```input
3
Hamburguesa Patatas Bebida
3           2       1

5
Hamburguesa 2
Patatas 1
Hamburguesa 1
Bebida 2
Patatas 2
```
```output
17.0
```
