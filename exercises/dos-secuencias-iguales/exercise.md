---
slug: dos-secuencias-iguales
---
# Dues seqüències iguals

Donades dues seqüències de nombres, dir si són iguals.

## Input

La entrada consta de dues seqüències.

Per a cada seqüència, el primer nombre  indica la quantitat de nombres de dita seqüencia. A continuació ve la seqüència.

## Output

si les seqüències són iguals

 si les seqüències no són iguals

## Tests

### Test 11.11
```input
3    1 2 3
3    1 2 3
```
```output
true
```

### Test 11.11
```input
3    100 200 300
3    100 200 300
```
```output
true
```

### Test private 11.11
```input
3    100 200 300
4    100 200 300 400
```
```output
false
```

### Test private 11.11
```input
5    1 2 3 4 5
5    1 2 3 4 5
```
```output
true
```

### Test private 11.11
```input
5    1 2 3 4 5
5    1 2 3 4 4
```
```output
false
```

### Test private 11.11
```input
3    23 34 45
2    23 45
```
```output
false
```

### Test private 11.11
```input
5    1 2 3 4 5
1    5
```
```output
false
```

### Test private 11.11
```input
1 3
1 5
```
```output
false
```

### Test private 11.12
```input
2 3 4
1 2
```
```output
false
```
