---
slug: ete1
---
# Primero igual al último

Se deben ir leyendo números hasta que se lea un 0. El programa debe mostrar "SI" en caso de que el primer número leído sea igual al último número leído antes que el 0. En caso contrario debe mostrar "NO".

## Input

Un secuencia de N números enteros que finaliza con un 0.

1 <= N <= 10^7

## Output

"SI" o "NO"

## Tests

### Test 12.5
```input
1 2 3 2 1 0
```
```output
SI
```

### Test 12.5
```input
1 0
```
```output
SI
```

### Test private 12.5
```input
1 2 0
```
```output
NO
```

### Test private 12.5
```input
1 2 1 2 1 2 1 0
```
```output
SI
```

### Test private 12.5
```input
1 2 1 2 0
```
```output
NO
```

### Test private 12.5
```input
-1 1 -1 1 -1 0
```
```output
SI
```

### Test private 12.5
```input
 1 2 3 4 1 0
```
```output
SI
```

### Test private 12.5
```input
1 2 3 4 0
```
```output
NO
```
