---
slug: operadores-perdidos
---
# Operadors perduts

Donats dos operands i un resultat, troba l'operador que satisfà la operació.

Els operadors possibles són: suma, resta, multiplicació, divisió i mòdul.

```text
+ - * / %
```

Si la operació pot ser resolta per més d'un operador, s'ha d'escollir el que estigui primer en la llista.

Si no es pot satisfer amb ninguna operació s'escriurà "IMPOSSIBLE".

## Input

Dos operands O1 i O2. I un resultat R

0 <= O1 <= 10^9

0 <= O2 <= 10^9

0 <= R <= 10^9

## Output

Es mostrarà el símbol de l'operador que satisfà la operació.

```text
+ - * / %
```

En cas de que no es puig satisfer amb cap, es mostrarà:

```text
IMPOSSIBLE
```

## Tests

### Test
```input
1 1 1
```
```output
*
```

### Test
```input
1 2 3
```
```output
+
```

### Test
```input
0 0 0
```
```output
+
```

### Test
```input
10 0 7
```
```output
IMPOSSIBLE
```

### Test
```input
1 3 1
```
```output
%
```

### Test
```input
30 12 6
```
```output
%
```

### Test
```input
13 7 91
```
```output
*
```

### Test
```input
14 7 2
```
```output
/
```

### Test
```input
10 3 1
```
```output
%
```

### Test
```input
55 15 10
```
```output
%
```

### Test
```input
84 0 0
```
```output
*
```

### Test
```input
62 0 21
```
```output
IMPOSSIBLE
```

### Test
```input
99 15 29
```
```output
IMPOSSIBLE
```

### Test
```input
93 49 20
```
```output
IMPOSSIBLE
```
