---
slug: c6-l2-2-equation
tags: [scanner, i/o]
---
# Equation

Implementa el mètode Equation.calculateSolution()

Aquest mètode ha d'emmagatzemar en la variable 'x' la solució a l'equació:

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

class Equation {
    float a, b;
    float x;

}

public class Main {

    public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);

        Equation equation = new Equation();

        while((equation.a = scanner.nextFloat()) != 0) {
            equation.b = scanner.nextFloat();

            equation.calculateSolution();
            System.out.format("%.2f * %.2f + %.2f = 0%n", equation.a, equation.x, equation.b);
        }
    }
}
```

## Tests

### Test
```input
10 5
5 10
2.5 5
0
```
```output
10.00 * -0.50 + 5.00 = 0
5.00 * -2.00 + 10.00 = 0
2.50 * -2.00 + 5.00 = 0
```

### Test
```input
10 5
5 10
2.5 5
0
```
```output
10.00 * -0.50 + 5.00 = 0
5.00 * -2.00 + 10.00 = 0
2.50 * -2.00 + 5.00 = 0
```

### Test
```input
100 500
1 5
2 10
5 25
0
```
```output
100.00 * -5.00 + 500.00 = 0
1.00 * -5.00 + 5.00 = 0
2.00 * -5.00 + 10.00 = 0
5.00 * -5.00 + 25.00 = 0
```
