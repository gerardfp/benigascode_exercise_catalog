---
slug: c1-l1-7-temps-de-descarrega
tags: [operadors, aritmetics]
---
# Temps de descàrrega

![image](1555864526-a951892bed-Sinttulo.png)

S'està realitzant un programa per a gestionar descàrregues d'arxius.
Aquest programa ha de mostrar a l'usuari el temps estimat que trigarà la descàrrega, en funció de la velocitat i el tamany de l'arxiu.

## Input

El primer nombre <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.787ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 769.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M52 648Q52 670 65 683H76Q118 680 181 680Q299 680 320 683H330Q336 677 336 674T334 656Q329 641 325 637H304Q282 635 274 635Q245 630 242 620Q242 618 271 369T301 118L374 235Q447 352 520 471T595 594Q599 601 599 609Q599 633 555 637Q537 637 537 648Q537 649 539 661Q542 675 545 679T558 683Q560 683 570 683T604 682T668 681Q737 681 755 683H762Q769 676 769 672Q769 655 760 640Q757 637 743 637Q730 636 719 635T698 630T682 623T670 615T660 608T652 599T645 592L452 282Q272 -9 266 -16Q263 -18 259 -21L241 -22H234Q216 -22 216 -15Q213 -9 177 305Q139 623 138 626Q133 637 76 637H59Q52 642 52 648Z"></path></g></svg></span> indica la velocitat de descàrrega (en KB per segon).

El segon nombre <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.499ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 645.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M308 24Q367 24 416 76T466 197Q466 260 414 284Q308 311 278 321T236 341Q176 383 176 462Q176 523 208 573T273 648Q302 673 343 688T407 704H418H425Q521 704 564 640Q565 640 577 653T603 682T623 704Q624 704 627 704T632 705Q645 705 645 698T617 577T585 459T569 456Q549 456 549 465Q549 471 550 475Q550 478 551 494T553 520Q553 554 544 579T526 616T501 641Q465 662 419 662Q362 662 313 616T263 510Q263 480 278 458T319 427Q323 425 389 408T456 390Q490 379 522 342T554 242Q554 216 546 186Q541 164 528 137T492 78T426 18T332 -20Q320 -22 298 -22Q199 -22 144 33L134 44L106 13Q83 -14 78 -18T65 -22Q52 -22 52 -14Q52 -11 110 221Q112 227 130 227H143Q149 221 149 216Q149 214 148 207T144 186T142 153Q144 114 160 87T203 47T255 29T308 24Z"></path></g></svg></span> indica el tamany de l'arxiu (en MB).

** Cal tenir en compte que 1MB = 1024 KB

## Output

Els segons que trigarà la descàrrega (sense decimals).

## Tests

### Test
```input
1 1
```
```output
1024
```
```explanation
El tamany de l'arxiu és 2MB, que són 2048 KB
Si la velocitat és d' 1KB per segon, trigará 2048 segons
```

### Test
```input
1 2
```
```output
2048
```
```explanation
El tamany de l'arxiu és d' 1MB, que són 1024 KB
Si la valocitat és de 1024KB per segon, trigará 1 segon
```

### Test
```input
1024 1
```
```output
1
```

### Test
```input
512 10
```
```output
20
```

### Test private
```input
4096 1024
```
```output
256
```
