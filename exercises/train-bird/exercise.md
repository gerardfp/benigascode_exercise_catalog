---
slug: train-bird
---
# Train bird

![image](train-bird-img0.gif)

El problema "A train and a bird" diu així:

*Un tren es troba a 20km de l'estació i s'aproxima a 10km/h cap a l'estació. Al mateix temps, un ocell vola a 30km/h des de l'estació en direcció al tren. Quan l'ocell arriba fins al tren, dona mitja volta i torna cap a l'estació, i quan arriba a l'estació fa una altra vegada mitja volta  fins al tren... i així fins que el tren arriba a l'estació.*

Quants kms recorrerà l'ocell fins que el tren arribi a l'estació?

## Input

L'entrada són tres números decimals:

- Distancia del tren

- Velocitat del tren

- Velocitat de l'ocell

## Output

S'imprimirà la distància recorreguda per l'ocell en format `float`

**Suggerència per a la solució**

En primer lloc cal esbrinar el temps que triga el tren en arribar a l'estació.

Després, segons aquest temps i la velocitat a la que vola l'ocell, es calcula la distància recorreguda per l'ocell.

## Tests

### Test
```input
10
10
30
```
```output
30.0
```

### Test
```input
50
10
100
```
```output
500.0
```

### Test
```input
15
30
80
```
```output
40.0
```

### Test
```input
32.5
65
55.5
```
```output
27.75
```

### Test
```input
200.5
43.25
55.35
```
```output
256.59363
```

### Test
```input
10
1
2
```
```output
20.0
```
