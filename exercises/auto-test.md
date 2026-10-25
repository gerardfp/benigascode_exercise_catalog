---
slug: auto-test
difficulty: 4.0
tags: [arrays, loops, for-loop, accumulators, filtering]
---
# Auto-test

![image](assets/auto-test-img0.png)

En el examen del carnet de conducir hay 30 preguntas, con tres posibles respuestas (a, b, c). Se aprueba si se fallan como máximo 3 respuestas.

Deseamos hacer una programa para auto-corregir un test de examen. Por el momento nos centrarmos solo en las respuestas, y no en las preguntas.

El usuario introducirá las respuestas a cada pregunta, y al finalizar se le mostrará el resultado, indicándole las respuestas correctas a las preguntas que haya fallado.

Las respuestas correctas a las preguntas del test son estas:

```
"a", "b", "a", "c", "a", "b", "b", "c", "b", "c", "a", "c", "b", "a", "a", "a", "c", "c", "b", "a", "c", "b", "c", "c", "a", "a", "c", "a", "a", "c"
```

## Input

La entrada consiste en las respuestas del usuario: 30 letras (`a`, `b`, `c`) separadas por espacios

## Output

1. En la primera línea se imprimirá `TEST SUPENDIDO` o `TEST APROBADO`
2. En la segunda línea se imprimirá `X fallos`
3. En la tercera línea se imprimirán los números de pregunta separados por espacios en blanco. Si el número de pregunta solo ocupa un dígito, se precederá con un espacio.
4. En la cuarta línia se imprimirán las respuestas dadas por el usuario. Cada respuesta irá precedida y sucedida por un espacio en blanco.
5. En la quinta línia se alinearán las respuestas correctas a aquellas preguntas que se hayan fallado.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    String[] correct = {
        "a", "b", "a", "c", "a", "b", "b", "c", "b", "c",
        "a", "c", "b", "a", "a", "a", "c", "c", "b", "a",
        "c", "b", "c", "c", "a", "a", "c", "a", "a", "c"
    };

    String[] user = new String[30];
    for (int i = 0; i < 30; i++) {
        user[i] = sc.next();
    }

    int errors = 0;
    for (int i = 0; i < 30; i++) {
        if (!user[i].equals(correct[i])) {
            errors++;
        }
    }

    if (errors <= 3) {
        IO.println("TEST APROBADO");
    } else {
        IO.println("TEST SUSPENDIDO");
    }
    IO.println(errors + " fallos.");

    String line3 = "";
    for (int i = 1; i <= 30; i++) {
        if (i < 10) {
            line3 += " " + i + " ";
        } else {
            line3 += i + " ";
        }
    }
    IO.println(line3);

    String line4 = "";
    for (int i = 0; i < 30; i++) {
        line4 += " " + user[i] + " ";
    }
    IO.println(line4);

    String line5 = "";
    for (int i = 0; i < 30; i++) {
        if (!user[i].equals(correct[i])) {
            line5 += " " + correct[i] + " ";
        } else {
            line5 += "   ";
        }
    }
    IO.println(line5);
}
```

## Tests

### Test
```input
a b c c a a b c b c a c b a a a c c b a c b c c a a c a a c
```
```output
TEST APROBADO
2 fallos.
 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
 a  b  c  c  a  a  b  c  b  c  a  c  b  a  a  a  c  c  b  a  c  b  c  c  a  a  c  a  a  c 
       a        b                                                                         
```

### Test
```input
a b a c a b b c b c a c b a a a c c b a c b c c a a c a a c 
```
```output
TEST APROBADO
0 fallos.
 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
 a  b  a  c  a  b  b  c  b  c  a  c  b  a  a  a  c  c  b  a  c  b  c  c  a  a  c  a  a  c 
                                                                                          
```

### Test private
```input
a b b c a c a c b a a c b a a a b a b a c a c c a a c c a c 
```
```output
TEST SUSPENDIDO
8 fallos.
 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
 a  b  b  c  a  c  a  c  b  a  a  c  b  a  a  a  b  a  b  a  c  a  c  c  a  a  c  c  a  c 
       a        b  b        c                    c  c           b                 a      
```
