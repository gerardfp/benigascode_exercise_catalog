---
slug: c3-l2-3-l33t
tags: [for]
---
# l33t

El l33t no té regles, però un algoritme sí. Posem aquestes:

1. Es substitueixen aquestes lletres:

```
A: 4
B: 8
E: 3
G: 6
I: !
L: 1
M: /\/\
O: 0
S: 5
T: 7
U: |_|
V: \\//
W: \/\/
Z: 2
```

1. La resta de lletres s'escriuen alternant minúscules i majúscules
2. S'eliminen els punts i les comes

## Input

Un text amb <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.583ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 681.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M228 637Q194 637 192 641Q191 643 191 649Q191 673 202 682Q204 683 217 683Q271 680 344 680Q485 680 506 683H518Q524 677 524 674T522 656Q517 641 513 637H475Q406 636 394 628Q387 624 380 600T313 336Q297 271 279 198T252 88L243 52Q243 48 252 48T311 46H328Q360 46 379 47T428 54T478 72T522 106T564 161Q580 191 594 228T611 270Q616 273 628 273H641Q647 264 647 262T627 203T583 83T557 9Q555 4 553 3T537 0T494 -1Q483 -1 418 -1T294 0H116Q32 0 32 10Q32 17 34 24Q39 43 44 45Q48 46 59 46H65Q92 46 125 49Q139 52 144 61Q147 65 216 339T285 628Q285 635 228 637Z"></path></g></svg></span> linies.
El text acaba amb una línia amb la paraula <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="5.764ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 2481.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M492 213Q472 213 472 226Q472 230 477 250T482 285Q482 316 461 323T364 330H312Q311 328 277 192T243 52Q243 48 254 48T334 46Q428 46 458 48T518 61Q567 77 599 117T670 248Q680 270 683 272Q690 274 698 274Q718 274 718 261Q613 7 608 2Q605 0 322 0H133Q31 0 31 11Q31 13 34 25Q38 41 42 43T65 46Q92 46 125 49Q139 52 144 61Q146 66 215 342T285 622Q285 629 281 629Q273 632 228 634H197Q191 640 191 642T193 659Q197 676 203 680H757Q764 676 764 669Q764 664 751 557T737 447Q735 440 717 440H705Q698 445 698 453L701 476Q704 500 704 528Q704 558 697 578T678 609T643 625T596 632T532 634H485Q397 633 392 631Q388 629 386 622Q385 619 355 499T324 377Q347 376 372 376H398Q464 376 489 391T534 472Q538 488 540 490T557 493Q562 493 565 493T570 492T572 491T574 487T577 483L544 351Q511 218 508 216Q505 213 492 213Z"></path><g transform="translate(764,0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g><g transform="translate(1653,0)"><path stroke-width="1" d="M287 628Q287 635 230 637Q207 637 200 638T193 647Q193 655 197 667T204 682Q206 683 403 683Q570 682 590 682T630 676Q702 659 752 597T803 431Q803 275 696 151T444 3L430 1L236 0H125H72Q48 0 41 2T33 11Q33 13 36 25Q40 41 44 43T67 46Q94 46 127 49Q141 52 146 61Q149 65 218 339T287 628ZM703 469Q703 507 692 537T666 584T629 613T590 629T555 636Q553 636 541 636T512 636T479 637H436Q392 637 386 627Q384 623 313 339T242 52Q242 48 253 48T330 47Q335 47 349 47T373 46Q499 46 581 128Q617 164 640 212T683 339T703 469Z"></path></g></g></svg></span>.

## Output

El text en llengua l33t

## Tests

### Test
```input
Hello world
END
```
```output
h3110 \/\/0R1d
```

### Test
```input
Hello leet
END
```
```output
h3110 1337
```

### Test
```input
goodbye world
END
```
```output
600d8Y3 \/\/0r1D
```

### Test
```input
all your base are belong to us
END
```
```output
411 y0|_|R 8453 4r3 8310N6 70 |_|5
```

### Test
```input
Lorem ipsum 
dolor sit amet, 
consectetur adipiscing elit.
END
```
```output
10r3/\/\ !P5|_|/\/\ 
d010R 5!7 4/\/\37 
c0N53c737|_|R 4d!P!5c!N6 31!7
```

### Test
```input
This isn't even, 
my final form.
END
```
```output
7h!5 !5N'7 3\\//3N 
/\/\y F!n41 F0r/\/\
```

### Test
```input
If the Tao is great, then the operating system is great. 
If the operating system is great, then the compiler is great. 
If the compiler is great, then the application is great. 
The user is pleased, and there is harmony in the world.
END
```
```output
!f 7H3 740 !5 6r347 7H3n 7H3 0p3R47!n6 5Y573/\/\ !5 6r347 
!F 7h3 0P3r47!N6 5y573/\/\ !5 6R347 7h3N 7h3 C0/\/\p!13R !5 6r347 
!F 7h3 C0/\/\p!13R !5 6r347 7H3n 7H3 4pP1!c47!0N !5 6r347 
7H3 |_|53r !5 P13453d 4Nd 7H3r3 !5 H4r/\/\0Ny !N 7h3 \/\/0R1d
```

### Test private
```input
It's over 9000!
END
```
```output
!7'5 0\\//3R 9000!
```
