---
slug: c6a99-cromos-repetits
---
# Cromos repetits

![image](1580224281-7dc0beb855-Mounstruos-Diablicos-2.jpg)

David s'està fent una col·lecció de cromos. S'ha fet una app per a portar l'inventari de cromos que té. Ara vol que l'app li digui quins cromos té repetits.

En total hi ha 68 cromos. Estan identificats amb números consecutius de l'1 al 68.

## Input

Un número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica la quantitat de cromos.

A continuació venen els identificadors de cada cromo.

## Output

S'imprimirà l'identificador dels cromos que té repetits, i quantes vegades el té repetit. Ordenats per identificador i en línies diferents.

El format és:

```
id: vegades
```

## Tests

### Test
```input
5
11 3 9 11 5
```
```output
11: 2
```
```explanation
El cromo 11 el té repetit 2 vegades
```

### Test
```input
5
11 33 11 11 33
```
```output
11: 3
33: 2
```
```explanation
El cromo 11 el té repetit 3 vegades
El cromo 33 el té repetit 2 vegades
```

### Test
```input
5
1 2 3 4 5
```
```output
```
```explanation
No té cap cromo repetit
```

### Test
```input
9
1 2 3 1 2 3 1 2 3
```
```output
1: 3
2: 3
3: 3
```

### Test
```input
5
1 68 1 68 1
```
```output
1: 3
68: 2
```

### Test
```input
100
9 25 57 61 37 4 26 44 29 61 18 66 33 24 20 20 2 51 4 55 44 32 31 21 7 51 52 68 43 27 60 9 42 23 23 47 26 24 50 52 60 26 5 24 23 55 43 44 35 6 30 22 18 1 51 29 34 36 35 10 56 54 66 1 62 29 60 63 35 1 5 5 13 40 20 21 62 18 35 35 12 38 23 51 59 44 68 8 51 55 60 64 20 34 64 21 13 48 66 57
```
```output
1: 3
4: 2
5: 3
9: 2
13: 2
18: 3
20: 4
21: 3
23: 4
24: 3
26: 3
29: 3
34: 2
35: 5
43: 2
44: 4
51: 5
52: 2
55: 3
57: 2
60: 4
61: 2
62: 2
64: 2
66: 3
68: 2
```

### Test private
```input
3
66 66 66
```
```output
66: 3
```
