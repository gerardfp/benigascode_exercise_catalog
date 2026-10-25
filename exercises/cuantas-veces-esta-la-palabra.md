---
slug: cuantas-veces-esta-la-palabra
difficulty: 3.0
tags: [arrays, strings, loops, for-loop, counters, search]
---
# Cuántas veces está la palabra?

Dada una lista de palabras, imprime la cantidad de veces que aparece la palabra indicada

<details>
<summary>Sugerencia para la solución</summary>
Algoritmo:

``` 
- Lee de la entrada la cantidad de palabras
- Crea un array para almacenar esas palabras
- Rellena el array con las palabras de la entrada
- Lee la palabra a buscar
- Recorre el array de palabras, y por cada palabra del array:
    - Si la palabra que estás viendo del array es igual a la palabra a buscar
        - Augmenta una variable contador.
- Imprime la variable contador
```
</details>

## Input

El primer número $N$ indica la cantidad de palabras

A continuación vienen las $N$ palabras.

## Output

entero

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    String[] words = new String[n];
    for (int i = 0; i < n; i++) {
        words[i] = sc.next();
    }
    String target = sc.next();
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (words[i].equals(target)) {
            count++;
        }
    }
    IO.println(count);
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
2
```

### Test
```input
6
public static void main string args

void
```
```output
1
```

### Test
```input
3
char int string

float
```
```output
0
```

### Test private
```input
13
continue for switch boolean do if break else case int char float while

break
```
```output
1
```
