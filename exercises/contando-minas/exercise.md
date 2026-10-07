---
slug: contando-minas
---
# Comptant mines

![image](1579771811-79189ea78e-1556787479-4e31cd8cf3-buscaminas.jpg)

Donat un tauler de buscamines, dir per a cada casella sense mina, quantes caselles amb mina té al seu voltant.

## Input

L'entrada consta en primer lloc de dos números  i  que indiquen el tamany (files i columnes) del tauler.

A continuación venen les caselles del tauler. (0=no hi ha mina, 1=hi ha mina)

## Output

S'imprimirá el tauler amb les casellas separades amb un espai i les files separades per un salt de línia.

En cada casella sense mina s'escriurà el número de mines que té al seu voltant.

Les caselles amb mina es deixaran igual, és a dir, amb un 1.

## Tests

### Test
```input
5 5
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
```
```output
0 0 0 0 0
0 1 1 1 0
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0
```

### Test
```input
5 5
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 0 0 0
```
```output
1 1 1 0 0
1 1 1 0 0
1 1 2 1 1
0 0 1 1 1
0 0 1 1 1
```

### Test
```input
3 3

1 0 0
0 0 0
0 0 0
```
```output
1 1 0
1 1 0
0 0 0
```

### Test
```input
3 3

1 1 1
1 0 1
1 1 1
```
```output
1 1 1
1 8 1
1 1 1
```

### Test
```input
4 4

0 0 0 0
1 1 0 0
1 1 0 0
0 0 0 0
```
```output
2 2 1 0
1 1 2 0
1 1 2 0
2 2 1 0
```

### Test
```input
1 4

1 0 1 0
```
```output
1 2 1 1
```

### Test
```input
5 5

0 0 0 0 0
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
0 0 0 0 0
```
```output
1 1 2 1 1
2 1 3 1 2
1 4 1 4 1
2 1 3 1 2
1 1 2 1 1
```

### Test
```input
4 1

0
1
0
0
```
```output
1
1
1
0
```

### Test
```input
8 8

0 0 0 0 0 0 0 1
0 1 0 0 0 0 1 0
1 0 1 0 0 0 0 1
1 1 1 0 0 0 0 0
0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0
1 0 0 1 0 0 0 1
```
```output
1 1 1 0 0 1 2 1 
2 1 2 1 0 1 1 3 
1 6 1 2 0 1 2 1 
1 1 1 3 2 2 2 1 
2 3 2 2 1 1 1 0 
0 0 0 1 2 2 1 0 
1 1 1 1 1 0 1 1 
1 1 1 1 1 0 1 1 
```

### Test
```input
2 2
1 0
0 0
```
```output
1 1
1 1
```
