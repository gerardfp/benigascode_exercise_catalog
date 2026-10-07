---
slug: c1-l1-9-sobren-ous
tags: [operadors, ternari]
---
# Sobren ous

Un granjer ha de portar al mercat els ous que ponen les seves gallines.

Par a transportar-los utilitza oueres en les quals caben 24 ous.

Quan arriba el moment de recollir els ous, el granjer necessita saber quantes oueres li calen per a poder transportar-los tots.

A més a més, vol que totes les oueres quedin totalment plenes, de forma, que si a la última ouera li queda espai, espera fins que les gallines posin els ous que li falten.

## Input

Un número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> que indica el nombre d'ous que han posat les gallines.

## Output

S'imprimiran dos nombres separats per un espai en blanc.

El primer nombre és la quantitat d'oueres que es necessiten.

El segon nombre és la quantitat d'ous que fan falta per omplir l'última ouera.

## Tests

### Test
```input
44
```
```output
2 4
```
```explanation
Necessitará 2 oueres, i li faltaran 4 ous
```

### Test
```input
44
```
```output
2 4
```
```explanation
Necesitará 1 ouera, i li faltaran 4 ous per a emplenar-la
```

### Test
```input
20
```
```output
1 4
```
```explanation
No necessitará cap ouera, ni cap ou
```

### Test
```input
0
```
```output
0 0
```

### Test private
```input
48
```
```output
2 0
```
