---
slug: c4-l4-2-nearest-neighbour-interpolation
tags: [scanner, i/o]
---
# Nearest-neighbour interpolation

Nearest-neighbour interpolation és un algoritme d'escalat d'imatges.
Quan fem una imatge més gran, l'algoritme Nearest-neighbour genera els nous pixels a partir dels originals més propers:

![image](c4-l4-2-nearest-neighbour-interpolation-img0.png)

Aquest algoritme funciona bé per a imatges 'pixel-art', però no és el més adequat per a imatges fotogràfiques ja que crea "dents de serra".

## Input

La entrada consisteix en una imatge en ASCII-ART.
En primer lloc ve el tamany en línies  de la imatge, i a continuació la imatge.

Finalment venen el factor d'escalat horitzontal  i el vertical .

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
ddd888PPP'''         
```
```explanation
ddd888PPP'''
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
