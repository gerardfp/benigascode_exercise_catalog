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

### Test 11.11
```input
beca
3
```
```output
ehfd
```

### Test 11.11
```input
beca
3
```
```output
ehfd
```

### Test private 11.11
```input
beca
5
```
```output
gjhf
```

### Test private 11.11
```input
hola
10
```
```output
ryvk
```

### Test private 11.11
```input
java
20
```
```output
dupu
```

### Test private 11.11
```input
zeta
27
```
```output
afub
```

### Test private 11.11
```input
char
78
```
```output
char
```

### Test private 11.11
```input
long
112
```
```output
twvo
```

### Test private 11.12
```input
byte
0
```
```output
byte
```
