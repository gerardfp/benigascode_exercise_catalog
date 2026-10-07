---
slug: cuenta-vocales
---
# Cuenta vocales

Dada una frase (terminada con un salto de línea), cuenta el número de veces que aparece cada vocal.

## Input

Un texto terminado con un salto de línea.

## Output

En la primera linea la cantidad de `a`, en la siguiente linea la cantidad de `e`, etc.

## Tests

### Test
```input
hola mundo
```
```output
1
0
0
2
1
```

### Test
```input
aa ee ii oo uu
```
```output
2
2
2
2
2
```

### Test
```input
xxa xax axx
```
```output
3
0
0
0
0
```

### Test
```input
aa, EE, ii.
```
```output
2
2
2
0
0
```

### Test
```input
aA eE iI oO u
```
```output
2
2
2
2
1
```

### Test
```input
aeiou
```
```output
1
1
1
1
1
```
