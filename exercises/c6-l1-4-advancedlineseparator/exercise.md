---
slug: c6-l1-4-advancedlineseparator
tags: [class, L0]
---
# AdvancedLineSeparator

Completa la classe AdvancedLineSeparator:

- Afegeix els camps que hi manquen

Completa el mètode Solution.main():

- Crida adequadament al mètode AdvancedLineSeparator.print()

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

class AdvancedLineSeparator {

    void print(){
        for (int i = 0; i < size; i++) {
            System.out.print(charSeparator);
        }
        System.out.println();
    }
}


public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        AdvancedLineSeparator lineSeparator = new AdvancedLineSeparator();

        String line;
        while(!(line = scanner.nextLine()).equals("__END__")) {
            lineSeparator.charSeparator = line.charAt(0);
            lineSeparator.size = scanner.nextInt();
            scanner.nextLine();

            System.out.format("Aqui sota apareix una linea de %s %s%n", lineSeparator.size,lineSeparator.charSeparator);
        }
    }
}
```

## Tests

### Test
```input
*
30
-
35
__END__
```
```output
Aqui sota apareix una linea de 30 *
******************************
Aqui sota apareix una linea de 35 -
-----------------------------------
```

### Test
```input
*
30
-
35
__END__
```
```output
Aqui sota apareix una linea de 30 *
******************************
Aqui sota apareix una linea de 35 -
-----------------------------------
```

### Test private
```input
^
30
#
40
=
50
__END__
```
```output
Aqui sota apareix una linea de 30 ^
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Aqui sota apareix una linea de 40 #
########################################
Aqui sota apareix una linea de 50 =
==================================================
```
