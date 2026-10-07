---
slug: c5-l1-2
tags: [arrays, estructuras-de-datos]
---
# Array de leds

Implementa el mètode switchLed de la classe LedArray. El mètode rep com a paràmetre la posició d'un led, i inverteix el seu estat.

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

class OLed {
    boolean state;

    void switchOn(){
        state = true;
    }

    void switchOff(){
        state = false;
    }

    void draw(){
        if(state){
            System.out.print("(*)");
        } else {
            System.out.print("( )");
        }
    }
}

class LedArray {
    OLed[] leds;

    LedArray(int size){
        leds = new OLed[size];
        for (int i = 0; i < size; i++) {
            leds[i] = new OLed();
        }
    }

    void draw(){
        for(OLed led : leds){
            led.draw();
        }
    }
}


public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        LedArray ledArray = new LedArray(5);

        int position;
        while((position = scanner.nextInt()) != -1){
            ledArray.switchLed(position);

            ledArray.draw();
            System.out.println();
        }
    }
}
```

## Tests

### Test 20
```input
1 2 3 2  -1
```
```output
( )(*)( )( )( )
( )(*)(*)( )( )
( )(*)(*)(*)( )
( )(*)( )(*)( )
```

### Test 20
```input
1 2 3 2   -1
```
```output
( )(*)( )( )( )
( )(*)(*)( )( )
( )(*)(*)(*)( )
( )(*)( )(*)( )
```

### Test private 20
```input
0 4 2   -1
```
```output
(*)( )( )( )( )
(*)( )( )( )(*)
(*)( )(*)( )(*)
```

### Test private 20
```input
0 3 2 4 1 0 4 0 3 2 1   -1
```
```output
(*)( )( )( )( )
(*)( )( )(*)( )
(*)( )(*)(*)( )
(*)( )(*)(*)(*)
(*)(*)(*)(*)(*)
( )(*)(*)(*)(*)
( )(*)(*)(*)( )
(*)(*)(*)(*)( )
(*)(*)(*)( )( )
(*)(*)( )( )( )
(*)( )( )( )( )
```

### Test private 20
```input
0 2 4 1 3 0 2 4 1 3  -1
```
```output
(*)( )( )( )( )
(*)( )(*)( )( )
(*)( )(*)( )(*)
(*)(*)(*)( )(*)
(*)(*)(*)(*)(*)
( )(*)(*)(*)(*)
( )(*)( )(*)(*)
( )(*)( )(*)( )
( )( )( )(*)( )
( )( )( )( )( )
```
