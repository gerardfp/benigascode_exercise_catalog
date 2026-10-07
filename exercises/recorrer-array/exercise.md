---
slug: recorrer-array
tags: [arrays, estructuras-de-datos]
---
# En qué posiciones está la palabra?

Dada una lista de palabras, imprime en qué posiciones se encuentra la palabra indicada

Algoritmo:

- Lee de la entrada la cantidad de palabras

- Crea un array para almacenar esas palabras

- Rellena el array con las palabras de la entrada

- Lee la palabra a buscar

- Recorre el array de palabras, y por cada palabra del array:

Si la palabra que estás viendo del array es igual a la palabra a buscar

Imprime la posición de la palabra del array que estás viendo (súmale 1 a esa posición para que parezca una posición "normal", y no la posición real en el array)

## Input

El primer número  indica la cantidad de palabras

A continuación vienen las  palabras.

## Output

Se imprimirán las posiciones (empezando por 1) en las que se ha encontrado la palabra a buscar, cada una en una línea.

## Plantillas

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
      	Scanner scanner = new Scanner(System.in);
      	
      	
    }
}
```

## Tests

### Test 25
```input
5
main class void static main

main
```
```output
1
5
```

### Test 25
```input
6
public static void main string args

void
```
```output
3
```

### Test private 25
```input
3
char int string

float
```
```output
```

### Test private 25
```input
13
continue for switch boolean do if break else case int char float while

break
```
```output
7
```
