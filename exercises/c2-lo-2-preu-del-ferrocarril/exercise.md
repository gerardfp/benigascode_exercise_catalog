---
slug: c2-lo-2-preu-del-ferrocarril
tags: [if]
---
# Preu del ferrocarril

Escriu un programa que determini el preu d'un bolet d'anada i tornada en ferrocarril, donada la distància a recòrrer i la quantitat en dies en el destí, sabent que:

- Si l'estada és de més de 7 dies i la distància és més de 800km, el bolet té un descompte del 30%.
- El preu per quilòmetre és de 0.35 euros.

## Input

La distància <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.924ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 828.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M287 628Q287 635 230 637Q207 637 200 638T193 647Q193 655 197 667T204 682Q206 683 403 683Q570 682 590 682T630 676Q702 659 752 597T803 431Q803 275 696 151T444 3L430 1L236 0H125H72Q48 0 41 2T33 11Q33 13 36 25Q40 41 44 43T67 46Q94 46 127 49Q141 52 146 61Q149 65 218 339T287 628ZM703 469Q703 507 692 537T666 584T629 613T590 629T555 636Q553 636 541 636T512 636T479 637H436Q392 637 386 627Q384 623 313 339T242 52Q242 48 253 48T330 47Q335 47 349 47T373 46Q499 46 581 128Q617 164 640 212T683 339T703 469Z"></path></g></svg></span> a del viatge (float).

La quantitat <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.838ex" height="2.509ex" style="vertical-align: -0.671ex;" viewBox="0 -791.3 791.5 1080.4" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M399 -80Q399 -47 400 -30T402 -11V-7L387 -11Q341 -22 303 -22Q208 -22 138 35T51 201Q50 209 50 244Q50 346 98 438T227 601Q351 704 476 704Q514 704 524 703Q621 689 680 617T740 435Q740 255 592 107Q529 47 461 16L444 8V3Q444 2 449 -24T470 -66T516 -82Q551 -82 583 -60T625 -3Q631 11 638 11Q647 11 649 2Q649 -6 639 -34T611 -100T557 -165T481 -194Q399 -194 399 -87V-80ZM636 468Q636 523 621 564T580 625T530 655T477 665Q429 665 379 640Q277 591 215 464T153 216Q153 110 207 59Q231 38 236 38V46Q236 86 269 120T347 155Q372 155 390 144T417 114T429 82T435 55L448 64Q512 108 557 185T619 334T636 468ZM314 18Q362 18 404 39L403 49Q399 104 366 115Q354 117 347 117Q344 117 341 117T337 118Q317 118 296 98T274 52Q274 18 314 18Z"></path></g></svg></span> de dies en el destí (int).

## Output

El preu del bolet.

## Tests

### Test
```input
100.0 1
```
```output
35.0
```

### Test
```input
200.0 1
```
```output
70.0
```

### Test
```input
900.0 1
```
```output
315.0
```

### Test
```input
100.0 10
```
```output
35.0
```

### Test
```input
900.0 10
```
```output
220.5
```

### Test
```input
800.0 7
```
```output
280.0
```

### Test
```input
801.0 7
```
```output
280.35
```

### Test
```input
800.0 8
```
```output
280.0
```

### Test
```input
801.0 8
```
```output
196.245
```

### Test private
```input
234.5 1
```
```output
82.075
```
