---
slug: afe43-amaga-les-columnes
---
# Amaga les columnes

![image](1579623863-f2d38217d1-excel.png)

Els programes de Full de Càlcul solen tenir la funció d'amagar columnes.

Tractem d'implementar aquesta funcionalitat...

## Input

L'entrada consta en primer lloc d'un Full de càlcul:

- Els dos primers números <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.442ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 1051.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"></path></g></svg></span> i <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indiquen la quantitat de files i columnes
- A continuació ve la taula amb les dades (Les files separades per un salt de línia i les columnes separades per espai en blanc)

<p>En segon lloc venen les columnes que cal ocultar:

- S'inidica el número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-3-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.766ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 760.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M50 252Q50 367 117 473T286 641T490 704Q580 704 633 653Q642 643 648 636T656 626L657 623Q660 623 684 649Q691 655 699 663T715 679T725 690L740 705H746Q760 705 760 698Q760 694 728 561Q692 422 692 421Q690 416 687 415T669 413H653Q647 419 647 422Q647 423 648 429T650 449T651 481Q651 552 619 605T510 659Q484 659 454 652T382 628T299 572T226 479Q194 422 175 346T156 222Q156 108 232 58Q280 24 350 24Q441 24 512 92T606 240Q610 253 612 255T628 257Q648 257 648 248Q648 243 647 239Q618 132 523 55T319 -22Q206 -22 128 53T50 252Z"></path></g></svg></span> de columnes que s'han d'ocultar
- Després venen els índexs d'aquestes columnes (començant per 1)

## Output

S'imprimirà la taula, sense mostrar les columnes indicades.
Tots els camps de la taula han d'ocupar **10 espais i aliniats a l'esquerra**

## Tests

### Test
```input
4 6
Nombre  Apellidos UF1 UF2 UF3 FINAL
Juan    Perez     5   6   6   6
Pepe    Alvarez   1   2   1   1
Eloy    Lopez     7   8   7   7

3
3 4 5
```
```output
Nombre    Apellidos FINAL     
Juan      Perez     6         
Pepe      Alvarez   1         
Eloy      Lopez     7      
```

### Test
```input
4 6
Nombre  Apellidos UF1 UF2 UF3 FINAL
Juan    Perez     5   6   6   6
Pepe    Alvarez   1   2   1   1
Eloy    Lopez     7   8   7   7

1
2
```
```output
Nombre    UF1       UF2       UF3       FINAL     
Juan      5         6         6         6         
Pepe      1         2         1         1         
Eloy      7         8         7         7  
```

### Test
```input
6 3
Columna1 Columna2 Columna3
Campo11  Campo12  Campo13
Campo21  Campo22  Campo23
Campo31  Campo32  Campo33
Campo41  Campo42  Campo43
Campo51  Campo52  Campo53

2
2 3
```
```output
Columna1  
Campo11   
Campo21   
Campo31   
Campo41   
Campo51  
```

### Test private
```input
6 3
Columna1 Columna2 Columna3
Campo11  Campo12  Campo13
Campo21  Campo22  Campo23
Campo31  Campo32  Campo33
Campo41  Campo42  Campo43
Campo51  Campo52  Campo53

2
1 3
```
```output
Columna2  
Campo12   
Campo22   
Campo32   
Campo42   
Campo52 
```
