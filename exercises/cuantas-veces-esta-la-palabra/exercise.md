---
slug: cuantas-veces-esta-la-palabra
---
# Cuántas veces está la palabra?

Dada una lista de palabras, imprime la cantidad de veces que aparece la palabra indicada

Algoritmo:

- Lee de la entrada la cantidad de palabras

- Crea un array para almacenar esas palabras

- Rellena el array con las palabras de la entrada

- Lee la palabra a buscar

- Recorre el array de palabras, y por cada palabra del array:

Si la palabra que estás viendo del array es igual a la palabra a buscar

Augmenta una variable contador.

- Imprime la variable contador

## Input

El primer número  indica la cantidad de palabras

A continuación vienen las  palabras.

## Output

entero

## Tests

### Test 25
```input
5
main class void static main

main
```
```output
2
```

### Test 25
```input
6
public static void main string args

void
```
```output
1
```

### Test private 25
```input
3
char int string

float
```
```output
0
```

### Test private 25
```input
13
continue for switch boolean do if break else case int char float while

break
```
```output
1
```
