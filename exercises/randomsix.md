---
slug: randomsix
---
# RandomSix

Donat un nombre inicial de dues xifres (al que anomenarem llavor), genera una seqüència de nombres a partir d'aquest.

Per generar un nou nombre, multiplica la xifra de les unitats per sis, i suma-li la xifra de les desenes. El nombre generat pasarà a ser la llavor per al següent nombre.

Exemple:

Llavor inicial = 13

13 --> 19 --> 55 --> 35 --> 33 --> 21 --> 08 --> 35 --> ...

```text
13 => 1 + 3*6 = 19
19 => 1 + 9*6 = 55
55 => 5 + 5*6 = 35
35 => 3 + 5*6 = 33
33 => 3 + 3*6 = 21
21 => 2 + 1*6 = 8
8  => 0 + 8*6 = 48
48 => 4 + 8*6 = 52
...
```

## Input

La entrada consisteix en dos nombres.

El primer nombre  és la llavor inicial.

El segon nombre  és la quantitat de nombres a generar.

## Output

La seqüència de nombres generada, separats per un salt de línía.

## Tests

### Test
```input
13
10
```
```output
19
55
35
33
21
8
48
52
17
43
```

### Test
```input
35
4
```
```output
33
21
8
48
```

### Test
```input
27
5
```
```output
44
28
50
5
30
```

### Test
```input
10
3
```
```output
1
6
36
```

### Test
```input
1
1
```
```output
6
```

### Test
```input
1 19
```
```output
6
36
39
57
47
46
40
4
24
26
38
51
11
7
42
16
37
45
34
```

### Test
```input
99 20
```
```output
63
24
26
38
51
11
7
42
16
37
45
34
27
44
28
50
5
30
3
18
```
