---
slug: subsecuencia-1
---
# Subseqüència

Donades dues seqüències de números, dir si la primera es troba (de forma correlativa) a dintre de la segona.

Exemple 1:

```text
13 21 11
8 34 13 21 11 23
```

SI (La primera seqüència es troba a dintre de la segona)

Exemple 2:

```text
4 1 5
4 1 7 5
```

NO (La primera seqüència no es troba a dintre de la segona)

## Input

La entrada consisteix en una primera seqüència d'  números, i una segona d'  números.

## Output

"SI" o "NO"

## Tests

### Test 8.33
```input
3    100 200 300
3    100 200 300
```
```output
SI
```

### Test 8.33
```input
2 111 111
2 111 111
```
```output
SI
```

### Test private 8.33
```input
4    11 22 33 44
3    11 22 33
```
```output
NO
```

### Test private 8.33
```input
4    11 22 33 44
5    11 22 33 55 44
```
```output
NO
```

### Test private 8.33
```input
3     7 8 9
10    1 2 3 4 5 6 7 8 9 10
```
```output
SI
```

### Test private 8.33
```input
1    1
4    2 3 1 4
```
```output
SI
```

### Test private 8.33
```input
3    11 22 33
3    33 22 11
```
```output
NO
```

### Test private 8.33
```input
3    4 6 5
5    3 2 465 7 8
```
```output
NO
```

### Test private 8.33
```input
3    3 5 4
6    3 5 4 3 5 4
```
```output
SI
```

### Test private 8.33
```input
3    3 5 4
5    1 2 3 5 4
```
```output
SI
```

### Test private 8.33
```input
3   7 8 9
8   1 7 8 1 1 7 8 9
```
```output
SI
```

### Test private 8.37
```input
3   7 8 9
5   1 1 1 7 8
```
```output
NO
```
