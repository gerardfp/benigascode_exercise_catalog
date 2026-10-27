---
slug: class-notas
difficulty: 3.0
tags: [class]
---
# Notas

Crea la classe `Alumno`

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// escriu el codi aqui

public class Main {

    public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
      
      	Alumno alumno = new Alumno();

      	int numeroNotas = scanner.nextInt();
      
      	alumno.notas = new float[numeroNotas];
      
        for(int i=0; i<numeroNotas; i++){
         	alumno.notas[i] = scanner.nextFloat();
        }
      
        float suma = 0;
        for(int i=0; i<numeroNotas; i++){
        	suma += alumno.notas[i];
        }
      
        System.out.println("Nota media: " + suma/numeroNotas);
    }
}
```

## Solutions

```java
class Alumno {
    double[] notas;
}

void main() {
    Scanner scanner = new Scanner(System.in);
    Alumno alumno = new Alumno();

    int numeroNotas = scanner.nextInt();
    alumno.notas = new double[numeroNotas];

    for (int i = 0; i < numeroNotas; i++) {
        alumno.notas[i] = scanner.nextDouble();
    }

    double suma = 0;
    for (int i = 0; i < numeroNotas; i++) {
        suma += alumno.notas[i];
    }

    IO.println("Nota media: " + suma / numeroNotas);
}
```

## Tests

### Test
```input
5
9 5.6 7 7.5 6.4
```
```output
Nota media: 7.1
```

### Test private
```input
3
10 5 0
```
```output
Nota media: 5.0
```
