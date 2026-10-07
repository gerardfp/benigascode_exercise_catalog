---
slug: separar-los-pares-de-los-impares
tags: [array]
---
# Separar els parells dels imparells

![image](1574079187-6bb595c935-Untitleddrawing3.png)

Donada una seqüència de números, s'ha de separar en base a dos criteris: 

Segons la **posició**:

Se separarà la seqüència original en dues seqüències:

- En una els que ocupen una posició parell,
- En l'altra els que ocupen una posició imparell.

Segons el **valor**:

Se separarà la seqüència original en dues seqüències:

- En una els números parells,
- En l'altra els imparells.

## Input

El primer nombre <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica el tamany de la seqüència. A continuació ve la seqüència.

## Output

S'imprimirán 4 seqüències, entre les dues primeres i les dues últimes s'imprimirà un salt de línia extra.

Les dues primeres seqüències són la separació per posició (posició parell/imparell).

Les dues últimes són la separació per valor (valor parell/imparell).

## Tests

### Test
```input
3    
1 2 3
```
```output
1 3
2

2
1 3
```
```explanation
![image](1574078686-3418215226-Untitleddrawing2.png)

Posició parell: 1, 3

Posició imparell: 2

Valor parell: 2

Valor imparell: 1, 3
```

### Test
```input
5    
5 4 8 6 7
```
```output
5 8 7
4 6

4 8 6
5 7
```

### Test
```input
2   
6 3
```
```output
6
3

6
3
```

### Test
```input
10    
3 6 34 6 2 4 6 23 45 4
```
```output
3 34 2 6 45
6 6 4 23 4

6 34 6 2 4 6 4
3 23 45
```

### Test
```input
5   
2 3 4 5 6
```
```output
2 4 6
3 5

2 4 6
3 5
```

### Test
```input
2  
1 2
```
```output
1
2

2
1
```

### Test private
```input
20
3 5 4 2 6 7 8 0 1 5 3 4 5 6 3 7 8 1 0 4
```
```output
3 4 6 8 1 3 5 3 8 0 
5 2 7 0 5 4 6 7 1 4 

4 2 6 8 0 4 6 8 0 4 
3 5 7 1 5 3 5 3 7 1 
```
