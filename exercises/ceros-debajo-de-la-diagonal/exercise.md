---
slug: ceros-debajo-de-la-diagonal
tags: [for]
---
# Zeros sota la diagonal

![image](1572515447-3bfc4d932d-zerosdiagonal.png)

Donada una matriu quadrada de nombres, digues si tots els nombres per sota de la diagonal són 0.

## Input

El primer nombre <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica el tamany de la matriu (<span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span>x<span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-3-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span>).

A continuació venen els nombres de la matriu.

## Output

{ SI | NO }

## Tests

### Test
```input
2
1 1
0 1
```
```output
SI
```

### Test
```input
2
1 2
0 4
```
```output
SI
```

### Test
```input
3
0 0 0
0 0 0
0 0 0
```
```output
SI
```

### Test
```input
4
1 2 3 4
0 2 3 4
0 0 3 4
0 0 0 4
```
```output
SI
```

### Test
```input
3
0 0 0
1 0 0
0 0 0
```
```output
NO
```

### Test
```input
3
0 0 0
0 1 0
0 0 0
```
```output
SI
```

### Test
```input
3
0 0 0
0 0 0
1 0 0
```
```output
NO
```

### Test
```input
3
0 0 0
0 0 0
0 1 0
```
```output
NO
```

### Test
```input
5
11 12 13 14 15
21 22 23 24 25
31 32 33 34 35
41 42 43 44 45
51 52 53 54 55
```
```output
NO
```

### Test
```input
5
11 12 13 14 15
 0 22 23 24 25
 0  0 33 34 35
 0  0  0 44 45
 0  0  0  0 55
```
```output
SI
```
```explanation
```
1 2 0 3   =>    1 2
                0 3
```
```

### Test
```input
2
1 2 0 3
```
```output
SI
```
```explanation
```
1 2 3
1 2 3 0 4 5 0 0 6   =>   0 4 5
                         0 0 6
```
```

### Test
```input
3
1 2 3 0 4 5 0 0 6
```
```output
SI
```

### Test
```input
9
 1  5  7  3  6  4  0  0  9 
 0  7  8  5  0  9  3  6  3 
 0  0  6  8  9  6  8  1  5 
 0  0  0  3  4  8  8  5  9 
 0  0  0  0  0  1  8  8  8 
 0  0  0  0  0  8  7  3  1 
 0  0  0  0  0  0  1  3  4 
 0  0  0  0  0  0  0  0  6 
 0  0  0  0  0  0  0  0  2
```
```output
SI
```

### Test
```input
13
 8  4  7  6  8  2  6  9  4  1  7  9  4 
 6  5  5  0  1  8  8  1  3  3  4  2  0 
 7  1  2  4  6  4  0  2  4  9  3  6  6 
 2  7  3  5  7  6  0  0  2  7  3  2  3 
 3  7  8  7  1  6  0  3  0  9  6  7  9 
 4  5  0  3  1  7  1  1  9  3  4  0  4 
 1  2  4  7  1  4  2  3  3  2  0  0  0 
 7  6  9  1  9  4  6  2  3  7  1  1  5 
 7  7  1  7  5  6  7  1  2  1  1  5  0 
 4  8  8  3  7  1  3  9  6  1  7  5  4 
 4  5  9  0  1  0  0  3  8  6  3  1  0 
 2  8  1  2  6  1  5  0  1  0  3  0  9 
 7  5  5  0  3  3  9  1  6  0  0  3  2
```
```output
NO
```

### Test
```input
5
 6  8  1  3  6 
 7  1  9  4  0 
 1  9  8  4  3 
 5  6  5  8  0 
 4  0  5  8  2
```
```output
NO
```

### Test private
```input
9
 0  6  6  9  1  7  0  8  7 
 0  2  4  1  8  6  8  0  4 
 0  0  5  6  2  5  2  0  8 
 0  0  0  6  9  9  1  3  2 
 0  0  0  0  2  8  5  5  5 
 0  0  0  0  0  5  6  5  0 
 0  0  0  0  0  0  2  1  1 
 0  0  0  0  0  0  0  8  5 
 0  0  0  0  0  0  0  0  4 
```
```output
SI
```
