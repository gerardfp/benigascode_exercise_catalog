---
slug: paella
---
# Paella

Suposant que una paella es pot cuinar exclusivament amb arròs i gambes (que es molt suposar), i que per cada 4 persones s'utilitza mig kilo d'arròs i un quart de kilo de gambes, escriu un programa que llegeixi el número de comensals, el preu per kilo d'arròs i el preu per kilo de gambes, i mostri les quantitats necessàries i el cost de cada ingredient, i el cost total de la paella.

## Input

Un enter  indicant el número de comensals.

Un float  indicant el preu per kilo d'arròs.

Un float  indicant el preu per kilo de gambes.

## Output

El programa imprimeix:

- La quantitat d'arròs necessària expressada en kilos.

- La quantitat de gambes necessàrias expressada en kilos.

- El preu de l'arròs necessari per a la paella.

- El preu de les gambes necessàries per a la paella.

- El cost total de la paella.

amb el format següent:

```text
0.5 kg arros
0.25 kg gambes
0.5 euros arros
3.0 euros gambes
TOTAL: 3.5 euros
```

## Tests

### Test 25
```input
4
1.00
12.00
```
```output
0.5 kg arros
0.25 kg gambes
0.5 euros arros
3.0 euros gambes
TOTAL: 3.5 euros
```

### Test 25
```input
8
1.5
15
```
```output
1.0 kg arros
0.5 kg gambes
1.5 euros arros
7.5 euros gambes
TOTAL: 9.0 euros
```

### Test private 25
```input
22
2
20
```
```output
2.75 kg arros
1.375 kg gambes
5.5 euros arros
27.5 euros gambes
TOTAL: 33.0 euros
```

### Test private 25
```input
24
16
8
```
```output
3.0 kg arros
1.5 kg gambes
48.0 euros arros
12.0 euros gambes
TOTAL: 60.0 euros
```
