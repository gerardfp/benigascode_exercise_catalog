---
slug: sucesion-capicua
tags: [scanner, i/o]
---
# Capicua

Donada una seqüència de números, dir si és capicua.

## Input

El primer número  indica la quantitat de números que hi ha en la seqüència. A continuació ve la seqüència.

## Output

"SI" si la seqüència és capicua.
"NO" si no ho és.

## Tests

### Test
```input
3    1 2 1
```
```output
SI
```

### Test
```input
5    100 200 300 200 100
```
```output
SI
```

### Test
```input
6    100 200 300 300 200 100
```
```output
SI
```

### Test
```input
1    100
```
```output
SI
```

### Test
```input
2    100 100
```
```output
SI
```

### Test
```input
4    100 100 200 100
```
```output
NO
```

### Test
```input
3    100 100 200
```
```output
NO
```

### Test
```input
20    1 2 3 4 5 6 7 8 9 10 10 9 8 7 6 5 4 3 2 1
```
```output
SI
```

### Test
```input
7
1 2 3 4 3 90 1
```
```output
NO
```

### Test
```input
6
1 2 3 3 90 1
```
```output
NO
```
