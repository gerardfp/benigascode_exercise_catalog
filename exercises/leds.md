---
slug: leds
tags: [class, L0]
difficulty: 5
---
# Leds

Implementa els mètodes switchOn() i switchOff() de la classe Led.

- switchOn() canvia la variable 'state' a 'true'
- switchOff() canvia la variable 'state' a 'false'

## Input

-

## Output

-

## Solutions

```java
class Led {
    boolean state;

    void switchOn() {
        state = true;
    }

    void switchOff() {
        state = false;
    }

    void draw() {
        if (state) {
            IO.print("(*)");
        } else {
            IO.print("( )");
        }
    }
}

void main() {
    Led l1 = new Led();
    Led l2 = new Led();

    l1.draw();
    l2.draw();

    l1.switchOn();

    IO.println();
    l1.draw();
    l2.draw();

    l2.switchOn();

    IO.println();
    l1.draw();
    l2.draw();

    l1.switchOff();

    IO.println();
    l1.draw();
    l2.draw();
}
```

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Led {
    boolean state;
    
    void draw(){
        if(state){
            System.out.print("(*)");
        } else {
            System.out.print("( )");
        }
    }
}

public class Main {

    public static void main(String[] args) {
        Led l1 = new Led();
        Led l2 = new Led();

        l1.draw();
        l2.draw();

        l1.switchOn();

        System.out.println();
        l1.draw();
        l2.draw();

        l2.switchOn();

        System.out.println();
        l1.draw();
        l2.draw();

        l1.switchOff();

        System.out.println();
        l1.draw();
        l2.draw();
    }
}
```

## Tests

### Test
```input
```
```output
( )( )
(*)( )
(*)(*)
( )(*)
```

### Test private
```input
```
```output
( )( )
(*)( )
(*)(*)
( )(*)
```
