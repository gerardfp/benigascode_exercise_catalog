---
slug: primeros-iguales-a-ultimos
---
# Primeros iguales a últimos

Para cada caso de prueba, se deben ir leyendo números hasta que se lea un 0. El programa debe mostrar "SI" en caso de que el primer número leído sea igual al último número leído antes que el 0. En caso contrario debe mostrar "NO".

## Input

El primer número (T) indica el número de casos de prueba.
A continuación viene una secuencia de N números por cada caso de prueba.
Cada secuencia finaliza con un 0.

## Output

Un "SI" o un "NO" por cada caso de prueba, separados por un salto de linea "\n"

## Tests

### Test
```input
1
1 2 3 1 0
```
```output
SI
```

### Test
```input
1
1 2 3 4 0
```
```output
NO
```

### Test
```input
2
1 2 3 1 0
1 2 2 1 0
```
```output
SI
SI
```

### Test
```input
2
1 2 3 1 0
1 2 3 4 0
```
```output
SI
NO
```

### Test
```input
3
1 0
1 2 0
1 2 1 0
```
```output
SI
NO
SI
```

### Test
```input
4
1 2 1 2 0
1 1 1 2 0
1 2 2 1 1 0
-1 0
```
```output
NO
NO
SI
SI
```

### Test
```input
3
5 4 2 0
6 4 3 6 0
4 0
```
```output
NO
SI
SI
```

### Test private
```input
2
6 7 4 9 0
9 9 9 8 0
```
```output
NO
NO
```
