---
slug: cuentas-de-numeros
---
# Cuentas de números

Para cada caso de prueba, se deben ir leyendo números hasta que se lea un 0. El programa debe mostrar la cantidad de números leídos antes del 0.

## Input

El primer número (T) indica la cantidad de casos de prueba que vienen a continuación.
Cada caso de prueba consta de una secuencia de N números que termina con un 0.

## Output

Por cada caso de prueba, un entero indicando la cantidad de números leídos; y separados por un salto de línea.

## Tests

### Test
```input
0
```
```output
0
```

### Test
```input
1
0
```
```output
0
```

### Test
```input
1
1 0
```
```output
1
```

### Test
```input
3
1 2 3 4 0
1 2 3 0
1 2 0
```
```output
4
3
2
```

### Test
```input
3
2 6 7 3 0
4 5 0
9 0
```
```output
4
2
1
```

### Test private
```input
2
9 9 9 0
8 5 3 0
```
```output
3
3
```
