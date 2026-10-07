---
slug: sucesion-capicua
tags: [arrays]
---
# Capicua

Donada una seqüència de números, dir si és capicua.

## Input

El primer número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica la quantitat de números que hi ha en la seqüència. A continuació ve la seqüència.

## Output

"SI" si la seqüència és capicua.
"NO" si no ho és.

## Tests

### Test
```input
3    1 2 1
```
```output
SI
```

### Test
```input
5    100 200 300 200 100
```
```output
SI
```

### Test
```input
6    100 200 300 300 200 100
```
```output
SI
```

### Test
```input
1    100
```
```output
SI
```

### Test
```input
2    100 100
```
```output
SI
```

### Test
```input
4    100 100 200 100
```
```output
NO
```

### Test
```input
3    100 100 200
```
```output
NO
```

### Test
```input
20    1 2 3 4 5 6 7 8 9 10 10 9 8 7 6 5 4 3 2 1
```
```output
SI
```

### Test
```input
7
1 2 3 4 3 90 1
```
```output
NO
```

### Test private
```input
6
1 2 3 3 90 1
```
```output
NO
```
