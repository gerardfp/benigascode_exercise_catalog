---
slug: superbowling
---
# Superbowling

En el juego de bolos, los bolos se colocan en filas de manera que en la primera fila hay un bolo, y en cada fila hay un bolo más que en la anterior.

![image](1548249910-2030623bda-Untitleddrawing.png)

Dado un número de bolos, determina si es posible organizarlos para que se forme un triangulo completo, es decir que ninguna fila quede incompleta.

## Input

Un numero N de bolos

## Output

true | false

## Tests

### Test
```input
6
```
```output
true
```
```explanation
6 bolos se pueden colocar perfectamente:

```
o o o
 o o
  o
```
```

### Test
```input
8
```
```output
false
```
```explanation
8 bolos no se pueden colocar de forma perfecta. Quedaría incompleto.

```
o o
 o o o
  o o
   o
```
```

### Test
```input
21
```
```output
true
```
```explanation
21 bolos se pueden colocar perfectamente:

```
o o o o o o
 o o o o o
  o o o o
   o o o
    o o
     o
```
```

### Test
```input
4
```
```output
false
```
```explanation
Con 4 bolos el triángulo queda incompleto:

```
o
 o o
  o
```
```

### Test
```input
91
```
```output
true
```

### Test
```input
78
```
```output
true
```

### Test
```input
1
```
```output
true
```

### Test
```input
990
```
```output
true
```

### Test
```input
9870
```
```output
true
```

### Test
```input
998991
```
```output
true
```

### Test
```input
997570
```
```output
false
```

### Test
```input
27
```
```output
false
```

### Test private
```input
3
```
```output
true
```
