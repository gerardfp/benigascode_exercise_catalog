---
slug: c2-l0-3-calculadora-amb-menu
tags: [if, switch]
---
# Calculadora amb menú

Realitza un programa que soliciti dos nombres i mostri per pantalla el següent menú:

```
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
```

L'usuari escullirà una opció i el programa finalitzarà mostrant el resultat per pantalla.

## Input

L'entrada consta de 3 nombres:

- Els dos primers <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="3.226ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 1389 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path><g transform="translate(888,0)"><path stroke-width="1" d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z"></path></g></g></svg></span> i <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="3.226ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 1389 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path><g transform="translate(888,0)"><path stroke-width="1" d="M109 429Q82 429 66 447T50 491Q50 562 103 614T235 666Q326 666 387 610T449 465Q449 422 429 383T381 315T301 241Q265 210 201 149L142 93L218 92Q375 92 385 97Q392 99 409 186V189H449V186Q448 183 436 95T421 3V0H50V19V31Q50 38 56 46T86 81Q115 113 136 137Q145 147 170 174T204 211T233 244T261 278T284 308T305 340T320 369T333 401T340 431T343 464Q343 527 309 573T212 619Q179 619 154 602T119 569T109 550Q109 549 114 549Q132 549 151 535T170 489Q170 464 154 447T109 429Z"></path></g></g></svg></span> son els operands.
- El tercer nombre <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-3-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="3.519ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 1515 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M740 435Q740 320 676 213T511 42T304 -22Q207 -22 138 35T51 201Q50 209 50 244Q50 346 98 438T227 601Q351 704 476 704Q514 704 524 703Q621 689 680 617T740 435ZM637 476Q637 565 591 615T476 665Q396 665 322 605Q242 542 200 428T157 216Q157 126 200 73T314 19Q404 19 485 98T608 313Q637 408 637 476Z"></path><g transform="translate(763,0)"><path stroke-width="1" d="M287 628Q287 635 230 637Q206 637 199 638T192 648Q192 649 194 659Q200 679 203 681T397 683Q587 682 600 680Q664 669 707 631T751 530Q751 453 685 389Q616 321 507 303Q500 302 402 301H307L277 182Q247 66 247 59Q247 55 248 54T255 50T272 48T305 46H336Q342 37 342 35Q342 19 335 5Q330 0 319 0Q316 0 282 1T182 2Q120 2 87 2T51 1Q33 1 33 11Q33 13 36 25Q40 41 44 43T67 46Q94 46 127 49Q141 52 146 61Q149 65 218 339T287 628ZM645 554Q645 567 643 575T634 597T609 619T560 635Q553 636 480 637Q463 637 445 637T416 636T404 636Q391 635 386 627Q384 621 367 550T332 412T314 344Q314 342 395 342H407H430Q542 342 590 392Q617 419 631 471T645 554Z"></path></g></g></svg></span> és l'opció del menú seleccionada

## Output

S'imprimirà el resultat de l'operació

## Tests

### Test
```input
1 1     1
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2
```

### Test
```input
1 1     1
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2
```

### Test
```input
1 1     2
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
0
```

### Test
```input
1 1     3
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
1
```

### Test
```input
1 1     4
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
1
```

### Test
```input
2 2     1
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
4
```

### Test
```input
2 3     2
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
-1
```

### Test
```input
2 5     3
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
10
```

### Test
```input
10 5     4
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2
```

### Test private
```input
3456 678     3
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2343168
```
