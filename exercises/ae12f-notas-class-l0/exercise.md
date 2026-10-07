---
slug: ae12f-notas-class-l0
---
# Notas

Crea la classe Alumne

## Input

-

## Output

-

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

## Tests

### Test 50
```input
5
9 5.6 7 7.5 6.4
```
```output
Nota media: 7.1
```

### Test private 50
```input
3
10 5 0
```
```output
Nota media: 5.0
```
