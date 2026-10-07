---
slug: c6-l2-1-termometre
tags: [class, L0]
---
# Termòmetre

Implementa els mètodes de la classe Thermometer:

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

class Thermometer {
    float celsius;
  
}


public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Thermometer thermometer1 = new Thermometer();
        Thermometer thermometer2 = new Thermometer();

        float a, b;
        while((a = scanner.nextFloat()) >= -273.1f) {
            thermometer1.celsius = a;
            thermometer2.celsius = scanner.nextFloat();

            System.out.println("Termometre 1");
            thermometer1.printCelsius();
            thermometer1.printFahrenheit();
            thermometer1.printKelvin();

            System.out.println("Termometre 2");
            thermometer2.printCelsius();
            thermometer2.printFahrenheit();
            thermometer2.printKelvin();
          
            System.out.println("--------");
        }
    }
}
```

## Tests

### Test
```input
0
100

-273.1
232.778

-274
```
```output
Termometre 1
   0.00C
  32.00F
 273.15K
Termometre 2
 100.00C
 212.00F
 373.15K
--------
Termometre 1
-273.10C
-459.58F
   0.05K
Termometre 2
 232.78C
 451.00F
 505.93K
--------
```

### Test
```input
0
100

-273.1
232.778

-274
```
```output
Termometre 1
   0.00C
  32.00F
 273.15K
Termometre 2
 100.00C
 212.00F
 373.15K
--------
Termometre 1
-273.10C
-459.58F
   0.05K
Termometre 2
 232.78C
 451.00F
 505.93K
--------
```

### Test private
```input
100
100

451
-173

36.8
5000

-275
```
```output
Termometre 1
 100.00C
 212.00F
 373.15K
Termometre 2
 100.00C
 212.00F
 373.15K
--------
Termometre 1
 451.00C
 843.80F
 724.15K
Termometre 2
-173.00C
-279.40F
 100.15K
--------
Termometre 1
  36.80C
  98.24F
 309.95K
Termometre 2
5000.00C
9032.00F
5273.15K
--------
```
