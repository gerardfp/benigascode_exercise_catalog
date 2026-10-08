---
slug: c1-l3-7-xifratge-cesar
tags: [condicionales, control-de-flujo]
---
# Xifratge cèsar

En criptografia, el xifratge Cèsar, és un tipus de xifratge per substitució en el qual cada lletra del "text clar" es subsititueix per una altra lletra que estigui un determinat nombre fix de posicions desplaçades de l'alfabet. El nombre de posicions que s'ha de desplaçar cada lletra es coneix com a Clau.

## Input

La entrada consta d'una paraula de 4 caracters i una clau  de desplaçacament.

Tots els caracters són de l'alfabet anglès i en minúscules.

## Output

S'escriurà la paraula codificada.

## Tests

### Test
```input
beca
3
```
```output
ehfd
```

### Test
```input
beca
3
```
```output
ehfd
```

### Test
```input
beca
5
```
```output
gjhf
```

### Test
```input
hola
10
```
```output
ryvk
```

### Test
```input
java
20
```
```output
dupu
```

### Test
```input
zeta
27
```
```output
afub
```

### Test
```input
char
78
```
```output
char
```

### Test
```input
long
112
```
```output
twvo
```

### Test
```input
byte
0
```
```output
byte
```
