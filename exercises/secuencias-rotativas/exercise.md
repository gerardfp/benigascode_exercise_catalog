---
slug: secuencias-rotativas
---
# Parin les rotatives!

A la redacció del periòdic arriba una notícia molt important... parin les rotatives!!

La màquina rotativa del periòdic és així:

![image](1556790353-d3d6097268-rodillo1.png)

En un rodet està el text que es va a imprimir. Aleshores el rodet comença a rodar i el paper va corrent per sota.

## Input

El primer número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica el tamany de la seqüència. A continuació ve la seqüència de números a imprimir.

Després ve la quantitat de números <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.838ex" height="2.509ex" style="vertical-align: -0.671ex;" viewBox="0 -791.3 791.5 1080.4" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M399 -80Q399 -47 400 -30T402 -11V-7L387 -11Q341 -22 303 -22Q208 -22 138 35T51 201Q50 209 50 244Q50 346 98 438T227 601Q351 704 476 704Q514 704 524 703Q621 689 680 617T740 435Q740 255 592 107Q529 47 461 16L444 8V3Q444 2 449 -24T470 -66T516 -82Q551 -82 583 -60T625 -3Q631 11 638 11Q647 11 649 2Q649 -6 639 -34T611 -100T557 -165T481 -194Q399 -194 399 -87V-80ZM636 468Q636 523 621 564T580 625T530 655T477 665Q429 665 379 640Q277 591 215 464T153 216Q153 110 207 59Q231 38 236 38V46Q236 86 269 120T347 155Q372 155 390 144T417 114T429 82T435 55L448 64Q512 108 557 185T619 334T636 468ZM314 18Q362 18 404 39L403 49Q399 104 366 115Q354 117 347 117Q344 117 341 117T337 118Q317 118 296 98T274 52Q274 18 314 18Z"></path></g></svg></span> que s'havien imprés en el moment en que es para la rotativa.

## Output

La seqüència de números impresos separada per espais.

## Tests

### Test
```input
3    1 2 3
3
```
```output
1 2 3
```

### Test
```input
3    100 200 300
5
```
```output
100 200 300 100 200
```

### Test
```input
3    100 200 300
7
```
```output
100 200 300 100 200 300 100
```

### Test
```input
3    100 200 300
2
```
```output
100 200
```

### Test
```input
5    100 200 300 400 500
4
```
```output
100 200 300 400
```

### Test
```input
3    10 20 30
10
```
```output
10 20 30 10 20 30 10 20 30 10
```

### Test private
```input
3    1 2 3
20
```
```output
1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2
```
