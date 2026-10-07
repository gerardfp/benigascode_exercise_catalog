---
slug: sucesion-de-fibonacci-3
tags: [for]
---
# Successió de Fibonacci

La successió de Fibonacci comença amb els nombres 0 i 1, i a partir d'aquests, «cada terme és la suma dels dos anteriors». 

![image](1556726526-96eb9e42a6-fibo1.png)

Determina si una seqüència de nombres és una successió de Fibonacci.

## Input

Una seqüència de N nombres enters. La seqüència acaba amb un -1.

## Output

"SI" o "NO"

## Tests

### Test
```input
0 1    -1
```
```output
SI
```

### Test
```input
0 1 2     -1
```
```output
NO
```

### Test
```input
0 1 1 2 3 5 8 13 21 34      -1
```
```output
SI
```

### Test
```input
0 1 1    -1
```
```output
SI
```

### Test
```input
0 1 1 2 3 4     -1
```
```output
NO
```

### Test
```input
5 6 11 17 28   -1
```
```output
NO
```

### Test
```input
0 2 2 4 6 10 -1
```
```output
NO
```

### Test private
```input
0 0 0 0 0 -1
```
```output
NO
```
