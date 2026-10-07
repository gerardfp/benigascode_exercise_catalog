---
slug: posicion-de-una-letra
tags: [array]
---
# Posició d'una lletra en un text

Donat un text i una lletra, troba la posició de la primera ocurrència de la lletra al text.

## Input

A la primera línia hi ha el text.

A la següent hi ha la lletra.

## Output

Un enter indicant la posició de la lletra. Si la lletra no hi és al text, s'imprimirà <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.971ex" height="2.343ex" style="vertical-align: -0.505ex;" viewBox="0 -791.3 1279 1008.6" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M84 237T84 250T98 270H679Q694 262 694 250T679 230H98Q84 237 84 250Z"></path><g transform="translate(778,0)"><path stroke-width="1" d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z"></path></g></g></svg></span>

## Tests

### Test
```input
hola mon!
o
```
```output
1
```

### Test
```input
hola mon!
m
```
```output
5
```

### Test
```input
hola mon!
z
```
```output
-1
```

### Test
```input
hola mons
s
```
```output
8
```

### Test
```input
a
a
```
```output
0
```

### Test
```input
hola hola
h
```
```output
0
```

### Test private
```input
fadsfds
d
```
```output
2
```
