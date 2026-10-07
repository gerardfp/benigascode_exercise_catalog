---
slug: esta-la-palabra-si-o-no
---
# Está la palabra? si o no?

Dada una lista de palabras, imprime si se encuentra o no la palabra indicada

Algoritmo:

- Lee de la entrada la cantidad de palabras

- Crea un array para almacenar esas palabras

- Rellena el array con las palabras de la entrada

- Lee la palabra a buscar

- Recorre el array de palabras, y por cada palabra del array:

Si la palabra que estás viendo del array es igual a la palabra a buscar

Guarda en una variable boolean que has encontrado la palabra. En este punto, puedes cortar el bucle con break, porque si ya has encontrado la palabra no tiene sentido seguir buscando.

- Imprime `YES` si la variable boolean te indica que has encontrado la palabra. `NO` en caso contrario

## Input

El primer número  indica la cantidad de palabras

A continuación vienen las  palabras.

## Output

`YES` | `NO`

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

### Test
```input
5
main class void static main

main
```
```output
YES
```

### Test
```input
6
public static void main string args

void
```
```output
YES
```

### Test
```input
3
char int string

float
```
```output
NO
```

### Test
```input
13
continue for switch boolean do if break else case int char float while

break
```
```output
YES
```
