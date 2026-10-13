---
slug: mezcla-de-secuencias
tags: [array]
---
# Mescla de seqüències

Donades dues seqüències de nombres, s'ha d'obtenir una mescla d'elles.

Per a obtenir la mescla s'ha d'agafar un element de cada seqüència alternativament. És a dir, primer un nombre de la primera seqüència, després un altre de la segona, i així successivament. Quan en una seqüència ja no queden més nombres, s'agafaran els nombres que quedin de l'altra.

## Input

La entrada consta de des seqüències.

Per a cada seqüència, el primer nombre <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica el tamany. A continuació ve la seqüència.

## Output

La seqüència resultant.

## Tests

### Test
```input
2 1 2
2 3 4
```
```output
1 3 2 4
```

### Test
```input
3    100 200 300
3    400 500 600
```
```output
100 400 200 500 300 600
```

### Test
```input
5    10 11 12 13 14
5    20 21 22 23 24
```
```output
10 20 11 21 12 22 13 23 14 24
```

### Test
```input
1    1000
1    2000
```
```output
1000 2000
```

### Test
```input
4    1 2 3 4
3    1 2 3
```
```output
1 1 2 2 3 3 4
```

### Test
```input
6    1 2 3 4 5 6
3    1 2 3
```
```output
1 1 2 2 3 3 4 5 6
```

### Test
```input
3    10 20 30
6    10 20 30 40 50 60
```
```output
10 10 20 20 30 30 40 50 60
```

### Test private
```input
6     76 65 98 45 32 21
3     99 88 77
```
```output
76 99 65 88 98 77 45 32 21
```
