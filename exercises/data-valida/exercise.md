---
slug: data-valida
---
# Data vàlida

Una data és vàlida si el número de dia està dintre dels dies del mes.

Cal tenir en compte que un any pot ser bixest. Un any és bixest si és divisible entre quatre i, o bé no és divisible entre 100 o és divisible entre 400.

## Input

Tres nombres corresponents a una data en format `dd/mm/yyyy`

## Output

`true` si la data és vàlida

`false` si no ho és

## Tests

### Test 6.25
```input
1 10 2000
```
```output
true
```

### Test 6.25
```input
1 1 2000
```
```output
true
```

### Test private 6.25
```input
32 10 2000
```
```output
false
```

### Test private 6.25
```input
31 10 2000
```
```output
true
```

### Test private 6.25
```input
31 11 2000
```
```output
false
```

### Test private 6.25
```input
29 2 2000
```
```output
true
```

### Test private 6.25
```input
29 2 1900
```
```output
false
```

### Test private 6.25
```input
29 2 1904
```
```output
true
```

### Test private 6.25
```input
28 2 1994
```
```output
true
```

### Test private 6.25
```input
29 2 2020
```
```output
true
```

### Test private 6.25
```input
29 2 2100
```
```output
false
```

### Test private 6.25
```input
31 8 2024
```
```output
true
```

### Test private 6.25
```input
31 9 2024
```
```output
false
```

### Test private 6.25
```input
30 6 2024
```
```output
true
```

### Test private 6.25
```input
31 4 2024
```
```output
false
```

### Test private 6.25
```input
0 1 2020
```
```output
false
```
