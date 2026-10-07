---
slug: c1-l4-1-piramide-lego
tags: [operadors]
---
# Piràmide lego

Amb peces de lego de 4x4 pots construir piràmides com aquesta de 3 pisos:

![image](1556381326-670e308ced-lego2.png)

Per a construir-la hem utilitzat 14 peces:

![image](1556381474-cb0adb7ecc-lego1.png)

¿Quantes peces es necessiten per a construir un piràmide d'un determinat nombre de pisos?

## Input

La entrada consta d'un nombre de pisos <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span>

## Output

El nombre de peces necessàries

## Tests

### Test
```input
1
```
```output
1
```
```explanation
![image](1556382453-eca1a030c5-lego3.png)
```

### Test
```input
2
```
```output
5
```

### Test
```input
3
```
```output
14
```
```explanation
![image](1556382656-90785cc9b1-lego4.png)
```

### Test
```input
4
```
```output
30
```

### Test
```input
5
```
```output
55
```

### Test
```input
6
```
```output
91
```

### Test
```input
10
```
```output
385
```

### Test
```input
1000
```
```output
333833500
```

### Test
```input
765892
```
```output
149755297914942910
```

### Test private
```input
1000000
```
```output
333333833333500000
```
