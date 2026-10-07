---
slug: c6-l3-2-equation2d
tags: [scanner, i/o]
---
# Equation2d

Implementa el mètode de la classe Equation2D amb la solució a l'equació:

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

class Equation2D {

    float a, b, c;

}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Equation2D equation2D = new Equation2D();

        equation2D.a = scanner.nextFloat();
        equation2D.b = scanner.nextFloat();
        equation2D.c = scanner.nextFloat();

        float[] x = equation2D.solve();

        System.out.format("%1$.2f * %4$.2f * %4$.2f  + %2$.2f * %4$.2f + %3$.2f = 0%n",
                equation2D.a, equation2D.b, equation2D.c, x[0]);
        System.out.format("%1$.2f * %4$.2f * %4$.2f  + %2$.2f * %4$.2f + %3$.2f = 0%n",
                equation2D.a, equation2D.b, equation2D.c, x[1]);
    }
}
```

## Tests

### Test
```input
1 -5 6
```
```output
1.00 * 3.00 * 3.00  + -5.00 * 3.00 + 6.00 = 0
1.00 * 2.00 * 2.00  + -5.00 * 2.00 + 6.00 = 0
```

### Test
```input
1 -5 6
```
```output
1.00 * 3.00 * 3.00  + -5.00 * 3.00 + 6.00 = 0
1.00 * 2.00 * 2.00  + -5.00 * 2.00 + 6.00 = 0
```

### Test
```input
2 -10 12
```
```output
2.00 * 3.00 * 3.00  + -10.00 * 3.00 + 12.00 = 0
2.00 * 2.00 * 2.00  + -10.00 * 2.00 + 12.00 = 0
```

### Test
```input
1 4 0
```
```output
1.00 * 0.00 * 0.00  + 4.00 * 0.00 + 0.00 = 0
1.00 * -4.00 * -4.00  + 4.00 * -4.00 + 0.00 = 0
```

### Test
```input
1 0 -1
```
```output
1.00 * 1.00 * 1.00  + 0.00 * 1.00 + -1.00 = 0
1.00 * -1.00 * -1.00  + 0.00 * -1.00 + -1.00 = 0
```

### Test
```input
15 -6.5 -2.7
```
```output
15.00 * 0.69 * 0.69  + -6.50 * 0.69 + -2.70 = 0
15.00 * -0.26 * -0.26  + -6.50 * -0.26 + -2.70 = 0
```
