---
slug: randomsix
tags: [for]
---
# RandomSix

Donat un nombre inicial de dues xifres (al que anomenarem llavor), genera una seqüència de nombres a partir d'aquest.

Per generar un nou nombre, multiplica la xifra de les unitats per sis, i suma-li la xifra de les desenes. El nombre generat pasarà a ser la llavor per al següent nombre.

Exemple:

Llavor inicial = 13

13 --> 19 --> 55 --> 35 --> 33 --> 21 --> 08 --> 35 --> ...

```
13 => 1 + 3*6 = 19
19 => 1 + 9*6 = 55
55 => 5 + 5*6 = 35
35 => 3 + 5*6 = 33
33 => 3 + 3*6 = 21
21 => 2 + 1*6 = 8
8  => 0 + 8*6 = 48
48 => 4 + 8*6 = 52
...
```

## Input

La entrada consisteix en dos nombres.

El primer nombre <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.499ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 645.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M308 24Q367 24 416 76T466 197Q466 260 414 284Q308 311 278 321T236 341Q176 383 176 462Q176 523 208 573T273 648Q302 673 343 688T407 704H418H425Q521 704 564 640Q565 640 577 653T603 682T623 704Q624 704 627 704T632 705Q645 705 645 698T617 577T585 459T569 456Q549 456 549 465Q549 471 550 475Q550 478 551 494T553 520Q553 554 544 579T526 616T501 641Q465 662 419 662Q362 662 313 616T263 510Q263 480 278 458T319 427Q323 425 389 408T456 390Q490 379 522 342T554 242Q554 216 546 186Q541 164 528 137T492 78T426 18T332 -20Q320 -22 298 -22Q199 -22 144 33L134 44L106 13Q83 -14 78 -18T65 -22Q52 -22 52 -14Q52 -11 110 221Q112 227 130 227H143Q149 221 149 216Q149 214 148 207T144 186T142 153Q144 114 160 87T203 47T255 29T308 24Z"></path></g></svg></span> és la llavor inicial.

El segon nombre <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> és la quantitat de nombres a generar.

## Output

La seqüència de nombres generada, separats per un salt de línía.

## Tests

### Test
```input
13
10
```
```output
19
55
35
33
21
8
48
52
17
43
```

### Test
```input
35
4
```
```output
33
21
8
48
```

### Test
```input
27
5
```
```output
44
28
50
5
30
```

### Test
```input
10
3
```
```output
1
6
36
```

### Test
```input
1
1
```
```output
6
```

### Test
```input
1 19
```
```output
6
36
39
57
47
46
40
4
24
26
38
51
11
7
42
16
37
45
34
```

### Test private
```input
99 20
```
```output
63
24
26
38
51
11
7
42
16
37
45
34
27
44
28
50
5
30
3
18
```
