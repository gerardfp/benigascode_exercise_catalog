---
slug: c3-l2-1-pics-i-valls
---
# Pics i valls

Els gràfics de línes mostren la informació en una sèrie de punts de dades connectats per segments de línies rectes. Es tracta d'un tipus bàsic de taula comú en molts camps.

![image](1556716980-037e3ea795-chart1.png)

Un element d'anàlisi d'aquests gràfics és dels pics i valls. Un pic és un valor local màxim, i una vall és un valor local mínim. És a dir, un pic és aquell valor el qual el seu anterior és menor que ell i el seu posterior és menor o igual que ell. I una vall és quan el seu anterior és major que ell i el seu posterior és major o igual que ell.

Al gràfic de dalt trobem dos pics (5 i 7) i dues valls (2 i 2). El primer i l'últim valor no els hem de comptar.

## Input

La entrada consta d'una seqüència de  valors. La seqüència acaba amb un -1 que no s'ha de comptar.

## Output

S'imprimirà el nombre de pics i el nombre de valls. També s'imprimirà el valor màxim i el valor mínim.

## Tests

### Test 9.09
```input
1 3 5 2 4 6 7 3 2 4     -1
```
```output
2
2
7
1
```

### Test 9.09
```input
2 3 5 6 4 7 5 3 2 4     -1
```
```output
2
2
7
2
```

### Test private 9.09
```input
4 3 5 6 4 8 5 6 2 3     -1
```
```output
3
4
8
2
```

### Test private 9.09
```input
4 3 2 1 2 3 5     -1
```
```output
0
1
5
1
```

### Test private 9.09
```input
4 4 2 2 3 3 1     -1
```
```output
1
1
4
1
```

### Test private 9.09
```input
1 1 1 2 3 3 1 1 3 4 5 5 6     -1
```
```output
2
1
6
1
```

### Test private 9.09
```input
45 45 45 89 89 1 3 25 25 24 25 24 2     -1
```
```output
3
2
89
1
```

### Test private 9.09
```input
1 1     -1
```
```output
0
0
1
1
```

### Test private 9.09
```input
4 5     -1
```
```output
0
0
5
4
```

### Test private 9.09
```input
7 5     -1
```
```output
0
0
7
5
```

### Test private 9.1
```input
1 4 3 5 2 6 4 9     -1
```
```output
3
3
9
1
```
