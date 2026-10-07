---
slug: tasca
tags: [arrays]
---
# Tasca

![image](1612522198-d7c82ee0c9-assignment.png)

A la plataforma d'aprenentatge que estem desenvolupant, els alumnes han de poder realitzar trameses dels seus treballs. Aquestes trameses han de tenir una hora límit.
Als alumnes que realitzin la tramesa un cop superada aquesta hora límit, la plataforma els informarà del temps excedit.

Donades les hores de les trameses i l'hora límit, digues quan de temps s'ha excedit cada tramesa.

## Input

El primer número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica la quantitat de trameses.

Per a cada tramesa s'indica: `hora minut segon`

Per últim s'indica l'hora límit: `hora minut segon`

## Output

S'imprimirà `ok` per a aquelles trameses que s'han fet dintre del temps límit.

Les trameses fora de temps s'escriurà: `S'ha excedit 0h 0m 0s` (canviant el `0` pel valor corresponent)

## Tests

### Test
```input
3
12 45 0
10 34 7
9 55 46

10 0 0
```
```output
S'ha excedit 2h 45m 0s
S'ha excedit 0h 34m 7s
ok
```

### Test
```input
6
11 0 0
10 1 0
10 0 1
9 0 0
9 59 0
9 59 59 

10 0 0
```
```output
S'ha excedit 1h 0m 0s
S'ha excedit 0h 1m 0s
S'ha excedit 0h 0m 1s
ok
ok
ok
```

### Test
```input
5
14 55 23
23 59 59
0 0 0
0 0 1
18 0 1

12 0 0
```
```output
S'ha excedit 2h 55m 23s
S'ha excedit 11h 59m 59s
ok
ok
S'ha excedit 6h 0m 1s
```

### Test
```input
2
23 59 59
0 0 0

23 59 59
```
```output
ok
ok
```

### Test private
```input
4
10 16 5
10 20 5
11 15 25
13 15 25

10 15 30
```
```output
S'ha excedit 0h 0m 35s
S'ha excedit 0h 4m 35s
S'ha excedit 0h 59m 55s
S'ha excedit 2h 59m 55s
```
