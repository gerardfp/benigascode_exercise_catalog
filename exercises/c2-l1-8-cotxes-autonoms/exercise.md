---
slug: c2-l1-8-cotxes-autonoms
tags: [if]
---
# Cotxes autònoms

Els cotxes autònoms ha de prendre decisions sobre la conducció a partir del les dades que perceben els seus sensors de l'entorn.

![image](1557227574-8acd780630-path3911-4.png)

El nostre cotxe elèctric ha de decidir si pot continuar la marxa en funció de les dades que li arriben del sensors. Aquestes dades són:

- Estat del semàfor: `r` = vermell, `g` = verd, `o` = àmbar
- Vianants creuant el carrer: `true`, `false`
- Agent de circulació: `0` = no hi ha agent, `1` = ens dona pas, `2` = ens fa stop

La decisió de continuar o no, en base a les combinacions de les dades del sensor es reflecteix en aquesta taula:

```
semafor   r r r r r r g g g g g g o o o o o o
vianants  f f f t t t f f f t t t f f f t t t
agent     0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2    
---------------------------------------------
creuar    f t f f f f t t f f f f t t f f f f
```

## Input

En primer lloc l'estat del semàfor `S`, després la presència de vianants `V`, finalment l'estat de l'agent de circulació `A`.

## Output

S'imprimirà `CONTINUAR` o `NO CONTINUAR`

## Tests

### Test 10
```input
r false 0
```
```output
NO CONTINUAR
```

### Test 10
```input
r false 0
```
```output
NO CONTINUAR
```

### Test 10
```input
r false 1
```
```output
CONTINUAR
```

### Test 10
```input
r false 2
```
```output
NO CONTINUAR
```

### Test 10
```input
r true 0
```
```output
NO CONTINUAR
```

### Test 10
```input
r true 1
```
```output
NO CONTINUAR
```

### Test 10
```input
r true 2
```
```output
NO CONTINUAR
```

### Test 10
```input
g false 0
```
```output
CONTINUAR
```

### Test 10
```input
g false 1
```
```output
CONTINUAR
```

### Test 10
```input
g false 2
```
```output
NO CONTINUAR
```

### Test 10
```input
g true 0
```
```output
NO CONTINUAR
```

### Test 10
```input
g true 1
```
```output
NO CONTINUAR
```

### Test 10
```input
g true 2
```
```output
NO CONTINUAR
```

### Test 10
```input
o false 0
```
```output
CONTINUAR
```

### Test 10
```input
o false 1
```
```output
CONTINUAR
```

### Test 10
```input
o false 2
```
```output
NO CONTINUAR
```

### Test 10
```input
o true 0
```
```output
NO CONTINUAR
```

### Test 10
```input
o true 1
```
```output
NO CONTINUAR
```

### Test private 10
```input
o true 2
```
```output
NO CONTINUAR
```
