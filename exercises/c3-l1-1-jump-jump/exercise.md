---
slug: c3-l1-1-jump-jump
---
# Jump, jump!

En un joc de plataformes, el personatge ha d'anar fent salts per a poder avançar. En la situació següent, per exemple, haurà de fer 3 salts per a arribar al final:

![image](1556708844-15036d2a78-mariojump.png)

Podem entendre el mapa del joc com una succesió de nombres que indiquen l'altura del terreny. En el cas anterior es podria definir com:

```text
1 2 1 2 2 3 2 1
```

En cada salt, el personatge pot avançar només 1 casella.

## Input

La entrada consta d'una successió de N nombres que indiquen l'altura H del terreny . La successió acaba amb un -1 (que no s'ha tenir en compte).

## Output

S'imprimirà el nombre mínim de salts que necessita donar per a arribar al final.

## Tests

### Test 12.5
```input
1 2 1 2 2 3 2 1   -1
```
```output
3
```

### Test 12.5
```input
1 2 1 2 1 2 3 1   -1
```
```output
4
```

### Test private 12.5
```input
2 2 1 1 1 2 3 1   -1
```
```output
2
```

### Test private 12.5
```input
3 3 2 2 1   -1
```
```output
0
```

### Test private 12.5
```input
1 2 3 4   -1
```
```output
3
```

### Test private 12.5
```input
1   -1
```
```output
0
```

### Test private 12.5
```input
1 2 3 4 1 2 3 4 5 6 7 8 1   -1
```
```output
10
```

### Test private 12.5
```input
9 5 1 2 3 1 2  -1
```
```output
3
```
