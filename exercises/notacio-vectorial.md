---
slug: notacio-vectorial
tags: [for]
---
# Notació arrays

En Java els arrays es poden inicialitzar amb la següent notació:

```
tipus[] identificador = { valor0, valor1, valor2, ..., valorN };
```

Escriu un programa que generi el codi d'inicialització d'un array a partir de les dades d'entrada.

El tipus de dades de l'entrada sempre és `int`, i l'identificador de l'array ha de ser `myArray`.

## Input

El primer número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica la quantitat de nombres que venen a continuació.

Després venen els <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> nombres separats per espais en blanc.

## Output

S'imprimirà la declaració de l'array en el format indicat i en una sola línia.

## Tests

### Test
```input
5
11 13 17 19 23
```
```output
int[] myArray = { 11, 13, 17, 19, 23 };
```

### Test
```input
3
100 200 300
```
```output
int[] myArray = { 100, 200, 300 };
```

### Test
```input
10
23 76 12 54 98 65 67 39 91 83
```
```output
int[] myArray = { 23, 76, 12, 54, 98, 65, 67, 39, 91, 83 };
```

### Test
```input
1
67
```
```output
int[] myArray = { 67 };
```

### Test private
```input
9
11 22 33 44 55 66 77 88 99
```
```output
int[] myArray = { 11, 22, 33, 44, 55, 66, 77, 88, 99 };
```
