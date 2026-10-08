---
slug: c6-l3-1-triangle
---
# Triangle

Implementa el mètodes de la classe Triangle:

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

class Triangle {
    float base, height;
}


public class Main {

    public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

	    Triangle t1 = new Triangle();
        Triangle t2 = new Triangle();

	    t1.base = scanner.nextFloat();
	    t1.height = scanner.nextFloat();

        System.out.format("Area triangle1: %.2f%n", t1.calculateArea());

        t2.base = scanner.nextFloat();
        t2.height = scanner.nextFloat();

        System.out.format("Area triangle2: %.2f%n", t2.calculateArea());
    }
}
```

## Tests

### Test
```input
3 4
2 5
```
```output
Area triangle1: 6.00
Area triangle2: 5.00
```

### Test
```input
3 4
2 5
```
```output
Area triangle1: 6.00
Area triangle2: 5.00
```

### Test
```input
30.77 23.5
22.9 5.1
```
```output
Area triangle1: 361.55
Area triangle2: 58.39
```

### Test
```input
0 89
103 0
```
```output
Area triangle1: 0.00
Area triangle2: 0.00
```
