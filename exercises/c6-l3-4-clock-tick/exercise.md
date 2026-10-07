---
slug: c6-l3-4-clock-tick
---
# Clock tick

Implementa els següents mètodes:
- Clock.tick() : augmenta en un segon el temps del rellotge
- Clock.reset() : posa a 0 el temps del rellotge
- Clock.getTime() : ha de retornar el temps del rellotge en format hh:mm:ss

## Input

La entrada consisteix en un seqüencia de números. Un número positiu indica la quantitat de ticks que s'han de fer al rellotge. Un zero significa 'reset'.

## Output

S'ha d'imprimir el temps del rellotge en format "hh:mm:ss" després de cada número llegit de l'entrada.

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Clock {
    int hours;
    int minutes;
    int seconds;

}

public class E12 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Clock clock = new Clock();

        int t;
        while((t = scanner.nextInt()) != -1){
            if(t == 0) clock.reset();
            else for (int i = 0; i < t; i++) clock.tick();
            System.out.println(clock.getTime());
        }
    }
}
```

## Tests

### Test
```input
1 60 3600 0   -1
```
```output
00:00:01
00:01:01
01:01:01
00:00:00
```

### Test
```input
1 60 3600 0   -1
```
```output
00:00:01
00:01:01
01:01:01
00:00:00
```

### Test
```input
1 0 60 0 3600    -1
```
```output
00:00:01
00:00:00
00:01:00
00:00:00
01:00:00
```

### Test
```input
1 1 1 1 60 60 60 3600 3600   -1
```
```output
00:00:01
00:00:02
00:00:03
00:00:04
00:01:04
00:02:04
00:03:04
01:03:04
02:03:04
```

### Test
```input
34 456 23 32435 0 34235    -1
```
```output
00:00:34
00:08:10
00:08:33
09:09:08
00:00:00
09:30:35
```
