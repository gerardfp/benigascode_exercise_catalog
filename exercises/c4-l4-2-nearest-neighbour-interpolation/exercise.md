---
slug: c4-l4-2-nearest-neighbour-interpolation
---
# Nearest-neighbour interpolation

Nearest-neighbour interpolation és un algoritme d'escalat d'imatges.
Quan fem una imatge més gran, l'algoritme Nearest-neighbour genera els nous pixels a partir dels originals més propers:

![image](1559147189-0ee013341f-nninterpolation.png)

Aquest algoritme funciona bé per a imatges 'pixel-art', però no és el més adequat per a imatges fotogràfiques ja que crea "dents de serra".

## Input

La entrada consisteix en una imatge en ASCII-ART.
En primer lloc ve el tamany en línies <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> de la imatge, i a continuació la imatge.

Finalment venen el factor d'escalat horitzontal <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M228 637Q194 637 192 641Q191 643 191 649Q191 673 202 682Q204 683 219 683Q260 681 355 681Q389 681 418 681T463 682T483 682Q499 682 499 672Q499 670 497 658Q492 641 487 638H485Q483 638 480 638T473 638T464 637T455 637Q416 636 405 634T387 623Q384 619 355 500Q348 474 340 442T328 395L324 380Q324 378 469 378H614L615 381Q615 384 646 504Q674 619 674 627T617 637Q594 637 587 639T580 648Q580 650 582 660Q586 677 588 679T604 682Q609 682 646 681T740 680Q802 680 835 681T871 682Q888 682 888 672Q888 645 876 638H874Q872 638 869 638T862 638T853 637T844 637Q805 636 794 634T776 623Q773 618 704 340T634 58Q634 51 638 51Q646 48 692 46H723Q729 38 729 37T726 19Q722 6 716 0H701Q664 2 567 2Q533 2 504 2T458 2T437 1Q420 1 420 10Q420 15 423 24Q428 43 433 45Q437 46 448 46H454Q481 46 514 49Q520 50 522 50T528 55T534 64T540 82T547 110T558 153Q565 181 569 198Q602 330 602 331T457 332H312L279 197Q245 63 245 58Q245 51 253 49T303 46H334Q340 38 340 37T337 19Q333 6 327 0H312Q275 2 178 2Q144 2 115 2T69 2T48 1Q31 1 31 10Q31 12 34 24Q39 43 44 45Q48 46 59 46H65Q92 46 125 49Q139 52 144 61Q147 65 216 339T285 628Q285 635 228 637Z"></path></g></svg></span> i el vertical <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-3-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.787ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 769.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M52 648Q52 670 65 683H76Q118 680 181 680Q299 680 320 683H330Q336 677 336 674T334 656Q329 641 325 637H304Q282 635 274 635Q245 630 242 620Q242 618 271 369T301 118L374 235Q447 352 520 471T595 594Q599 601 599 609Q599 633 555 637Q537 637 537 648Q537 649 539 661Q542 675 545 679T558 683Q560 683 570 683T604 682T668 681Q737 681 755 683H762Q769 676 769 672Q769 655 760 640Q757 637 743 637Q730 636 719 635T698 630T682 623T670 615T660 608T652 599T645 592L452 282Q272 -9 266 -16Q263 -18 259 -21L241 -22H234Q216 -22 216 -15Q213 -9 177 305Q139 623 138 626Q133 637 76 637H59Q52 642 52 648Z"></path></g></svg></span>.

## Output

S'imprimirà la imatge escalada segons els factors horitzontal i vertical.

## Tests

### Test
```input
3
#..
.%.
..=
4 4
```
```output
####........
####........
####........
####........
....%%%%....
....%%%%....
....%%%%....
....%%%%....
........====
........====
........====
........====
```

### Test
```input
3
#..
.%.
..=
4 4
```
```output
####........
####........
####........
####........
....%%%%....
....%%%%....
....%%%%....
....%%%%....
........====
........====
........====
........====
```

### Test
```input
3
#..
.%.
..=
6 2
```
```output
######............
######............
......%%%%%%......
......%%%%%%......
............======
............======
```

### Test
```input
3
#..
.%.
..=
2 6
```
```output
##....
##....
##....
##....
##....
##....
..%%..
..%%..
..%%..
..%%..
..%%..
..%%..
....==
....==
....==
....==
....==
....==
```

### Test
```input
5
 ,od8888bn.      ,.od88bo,
d8P'   `*88bn. ,       `Y8b
88'      `*888b.        `D8
Y8b        ,`*Y8bn.    ,d8P
`*Y8bn,. ;     `*+88888P*'
1 3
```
```output
 ,od8888bn.      ,.od88bo,
 ,od8888bn.      ,.od88bo,
 ,od8888bn.      ,.od88bo,
d8P'   `*88bn. ,       `Y8b
d8P'   `*88bn. ,       `Y8b
d8P'   `*88bn. ,       `Y8b
88'      `*888b.        `D8
88'      `*888b.        `D8
88'      `*888b.        `D8
Y8b        ,`*Y8bn.    ,d8P
Y8b        ,`*Y8bn.    ,d8P
Y8b        ,`*Y8bn.    ,d8P
`*Y8bn,. ;     `*+88888P*'
`*Y8bn,. ;     `*+88888P*'
`*Y8bn,. ;     `*+88888P*'
```

### Test
```input
5
 ,od8888bn.      ,.od88bo,
d8P'   `*88bn. ,       `Y8b
88'      `*888b.        `D8
Y8b        ,`*Y8bn.    ,d8P
`*Y8bn,. ;     `*+88888P*'
3 2
```
```output
   ,,,oooddd888888888888bbbnnn...                  ,,,...oooddd888888bbbooo,,,
   ,,,oooddd888888888888bbbnnn...                  ,,,...oooddd888888bbbooo,,,
ddd888PPP'''         ```***888888bbbnnn...   ,,,                     ```YYY888bbb
ddd888PPP'''         ```***888888bbbnnn...   ,,,                     ```YYY888bbb
888888'''                  ```***888888888bbb...                        ```DDD888
888888'''                  ```***888888888bbb...                        ```DDD888
YYY888bbb                        ,,,```***YYY888bbbnnn...            ,,,ddd888PPP
YYY888bbb                        ,,,```***YYY888bbbnnn...            ,,,ddd888PPP
```***YYY888bbbnnn,,,...   ;;;               ```***+++888888888888888PPP***'''
```***YYY888bbbnnn,,,...   ;;;               ```***+++888888888888888PPP***'''
```

### Test
```input
9
_________________
`$$$$$$$$$$$$$$$'
 $$'`$'`$'`$'`$$
 $$bd$bd$bd$bd$$
 $$$$*"` `"*$$$$
 $$$`       `$$$
 $$[         ]$$
 $$[         ]$$
j$$[         ]$$$L
2 1
```
```output
__________________________________
``$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$''
  $$$$''``$$''``$$''``$$''``$$$$
  $$$$bbdd$$bbdd$$bbdd$$bbdd$$$$
  $$$$$$$$**""``  ``""**$$$$$$$$
  $$$$$$``              ``$$$$$$
  $$$$[[                  ]]$$$$
  $$$$[[                  ]]$$$$
jj$$$$[[                  ]]$$$$$$LL
```

### Test private
```input
9
_________________
`$$$$$$$$$$$$$$$'
 $$'`$'`$'`$'`$$
 $$bd$bd$bd$bd$$
 $$$$*"` `"*$$$$
 $$$`       `$$$
 $$[         ]$$
 $$[         ]$$
j$$[         ]$$$L
1 2
```
```output
_________________
_________________
`$$$$$$$$$$$$$$$'
`$$$$$$$$$$$$$$$'
 $$'`$'`$'`$'`$$
 $$'`$'`$'`$'`$$
 $$bd$bd$bd$bd$$
 $$bd$bd$bd$bd$$
 $$$$*"` `"*$$$$
 $$$$*"` `"*$$$$
 $$$`       `$$$
 $$$`       `$$$
 $$[         ]$$
 $$[         ]$$
 $$[         ]$$
 $$[         ]$$
j$$[         ]$$$L
j$$[         ]$$$L
```
