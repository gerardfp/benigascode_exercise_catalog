---
slug: estan-todos
---
# Hi sou tots i totes?

En una sortida escolar, la mestra posa una enganxina a cada nen i nena amb un número correlatiu.

Quan arriba el moment de pujar a l'autobús els nens i nenes van pujant i la mestra va marcant a la seva llibreta els números dels que hi van pujant.

![image](1556784726-b0d72bdd6a-schoolsbus.png)

Quan han pujat tots els alumnes, la mestra revisa les seves anotacions per veure si estan tots els alumnes.

## Input

El primer número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica el nombre d'alumnes. A continuació ve la seqüència de números.

## Output

"SI" si han pujat tots els alumnes.
"NO" en cas contrari.

## Tests

### Test
```input
3 
1 2 3
```
```output
SI
```

### Test
```input
5 
1 2 3 4 5
```
```output
SI
```

### Test
```input
5 
1 1 2 3 4
```
```output
NO
```

### Test
```input
10 
3 2 4 5 3 6 5 7 8 9
```
```output
NO
```

### Test
```input
10 
5 3 4 10 6 8 7 1 9 2
```
```output
SI
```

### Test
```input
1 
1
```
```output
SI
```

### Test
```input
1 
23
```
```output
NO
```

### Test
```input
10 
3 2 4 5 3 6 5 7 8 10
```
```output
NO
```

### Test private
```input
3
1 3 11
```
```output
NO
```
