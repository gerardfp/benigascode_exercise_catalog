---
slug: canastas
tags: [for]
---
# Encistellaments

Al basquetbol es poden anotar cistelles d'1, 2 i 3 punts.

Donada l'evolució de la puntuació d'un equip en un partit, determina el nombre de cistelles anotades d'1, 2 i 3 punts.

Exemple:

Evolució de la puntuació: 

```
2 4 7 8 11 13 14
```

- La primera cistella va estar de 2 punts
- La segona cistella va estar de 2 punts
- La tercera cistella va estar de 3 punts
- La quarta cistella va estar d'1 punt
- La cinquena cistella va estar de 3 punts
- La sisena cistella va estar de 2 punts
- L'última cistella va estar de 1 punt

En total:

- Cistelles d' 1 punt -> 2
- Cistelles de 2 punts -> 3
- Cistelles de 3 punts -> 2

## Input

L'entrada consta d'una seqüència d' <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> nombres que indiquen l'evolució de la puntuació.

L'entrada acaba amb un -1.

## Output

El nombre de cistelles d'1, 2 i 3 punts, en diferents línies.

## Tests

### Test
```input
1 4 6 7 9   -1
```
```output
2
2
1
```
```explanation
La primera cistella va estar d' 1 punt.

La segona cistella va estar de 3 punts

La tercera cistella va estar de 2 punts

La quarta cistella va estar de 1 punt

La cinquena cistella va estar de 2 punts

Total cistelles d' 1 punt -> **2**

Total cistelles de 2 punts -> **2**

Total cistelles de 3 punts -> **1**
```

### Test
```input
3 5 6 9   -1
```
```output
1
1
2
```
```explanation
La primera cistella va estar de 3 punts.

La segona cistella va estar de 2 punts.

La tercera cistella va estar de 1 punt.

La quarta cistella va estar de 3 punts.

Total cistelles de 1 punt -> **1**

Total cistelles de 2 punts -> **1**

Total cistelles de 3 punts -> **2**
```

### Test
```input
3    -1
```
```output
0
0
1
```
```explanation
Només va haver-hi **1 ** cistella i va estar de 3 punts
```

### Test
```input
1 3 6   -1
```
```output
1
1
1
```
```explanation
Una cistella de cada
```

### Test
```input
3 4 7 9 12 15 16 17 20 21 23 25 28    -1
```
```output
4
3
6
```

### Test
```input
2 3 6 7 8 11 14 16 19 20 21 22 25 28 29 31 32 33 34 36 39 41 43 45 48 51 52 55 56 57 58 60 62 63 66 68 70 71 73 75 76 77 78      -1
```
```output
19
13
11
```

### Test
```input
1 4 5 8 10 11 13 14 17 18 20 23 25 27 28 29 31 34 36 38 40 42 44 45 48 49 50 53 54 55 57 60 62 63 65 67 69 70 73 74 75 78 79 81    -1
```
```output
17
17
10
```

### Test
```input
1  -1
```
```output
1
0
0
```

### Test
```input
1  -1
```
```output
1
0
0
```

### Test
```input
-1
```
```output
0
0
0
```

### Test private
```input
2   -1
```
```output
0
1
0
```
