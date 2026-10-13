---
slug: estadistiques-al-teatre-for
tags: [for]
---
# Estadístiques al teatre

El Gran Teatre necessita tenir estadístiques sobre les edats dels assistents.

A partir del registre d'entrada s'ha indicar quantes persones en cada franja d'edat han acudit els divendres, dissabtes o diumenges.

Les franjes d'edat són:

- Menors de 18 anys
- Entre 18 i 65 anys
- Majors de 65 anys

## Input

L'entrada comença amb un enter <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> que indica el número registres que hi ha.

Per a cada registre s'indica el dia de la setmana: `DIVENDRES`, `DISSABTE`, `DIUMENGE` i, a la següent línia, una seqüència d'enters que indiquen les edats dels assistents aquell dia (la seqüència acaba amb `-1`).

## Output

Es mostrarà el resultat amb el següent format:

```
nom_dia
0-17 : a
18-65: b
+65  : c
```

nom_dia = `divendres` | `dissabte` | `diumenge`

a = total persones menors de 18

b = total persones entre 18-65

c = total persones majors de 65

## Tests

### Test
```input
5
divendres
10 15 80   -1
dissabte
30 35 33   -1
diumenge
80 85 83 82   -1
divendres
11 11 82   -1
diumenge
82 81   -1
```
```output
divendres
0-17 : 4
18-65: 0
+65  : 2

dissabte
0-17 : 0
18-65: 3
+65  : 0

diumenge
0-17 : 0
18-65: 0
+65  : 6
```

### Test
```input
1
divendres
17 18 65 66    -1
```
```output
divendres
0-17 : 1
18-65: 2
+65  : 1

dissabte
0-17 : 0
18-65: 0
+65  : 0

diumenge
0-17 : 0
18-65: 0
+65  : 0
```

### Test
```input
10
divendres
10 15 80 35 45 67 23   -1
dissabte
30 35 33 33 23 65 67 45  -1
diumenge
80 85 83 82   -1
divendres
11 11 27 34 36 67 69   -1
diumenge
82 81 1 9 2  -1
divendres
10 15 80 17 18 19  -1
dissabte
30 35 33 55 43 52 41   -1
diumenge
80 85 83 82 78 69 70  -1
divendres
11 11 4 13 17 16 14   -1
diumenge
82 81 66 67 66  -1
```
```output
divendres
0-17 : 14
18-65: 8
+65  : 5

dissabte
0-17 : 0
18-65: 14
+65  : 1

diumenge
0-17 : 3
18-65: 0
+65  : 18
```

### Test private
```input
1
divendres
1   -1
```
```output
divendres
0-17 : 1
18-65: 0
+65  : 0

dissabte
0-17 : 0
18-65: 0
+65  : 0

diumenge
0-17 : 0
18-65: 0
+65  : 0
```
