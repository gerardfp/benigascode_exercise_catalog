---
slug: c1-l3-4-hardy-ramanujan
---
# Hardy-Ramanujan

Desde que va llegir sobre el matemàtic Ramanujan, busca el nombre 1729 per tot arreu: a les matrícules dels cotxes, als números de telèfon, a les tarjetes bancàries, ...

Especialment a les tarjetes busca que sigui un dels grups de nombres de 4 xifres.

![image](assets/c1-l3-4-hardy-ramanujan-img0.png)

## Input

La entrada consisteix en un nombre  de tarjeta bancària.

## Output

si el 1729 es un dels grups de 4 xifres

 si no ho és

## Tests

### Test
```input
1111222233334444
```
```output
false
```

### Test
```input
1111222233334444
```
```output
false
```

### Test
```input
1111222233331729
```
```output
true
```

### Test
```input
1111222217294444
```
```output
true
```

### Test
```input
1111172933334444
```
```output
true
```

### Test
```input
1729222233334444
```
```output
true
```

### Test
```input
1117292233334444
```
```output
false
```

### Test
```input
1111221729334444
```
```output
false
```

### Test
```input
1111222233317294
```
```output
false
```

### Test
```input
0
```
```output
false
```

### Test
```input
0000000017290000
```
```output
true
```

### Test
```input
0000000000001729
```
```output
true
```

### Test
```input
1234567891234567
```
```output
false
```
