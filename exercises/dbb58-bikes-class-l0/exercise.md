---
slug: dbb58-bikes-class-l0
tags: [classes]
---
# Bikes

Implementa el mètode Race.fastest()

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Bike {
    int speed;

    public Bike(int speed) {
        this.speed = speed;
    }
}

class Race {
    Bike[] bikes;

  	// escriu el codi aqui

}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Race race = new Race();

        int numBikes = scanner.nextInt();
      
        race.bikes = new Bike[numBikes];

        for (int i = 0; i < numBikes; i++) {
            race.bikes[i] = new Bike(scanner.nextInt());
        }

        Bike fastest = race.fastest();

        System.out.println(fastest == null ? "No bikes" : fastest.speed);
    }
}
```

## Tests

### Test 25
```input
3
10 20 30
```
```output
30
```

### Test 25
```input
4
20 30 20 10
```
```output
30
```

### Test private 25
```input
2
40 30
```
```output
40
```

### Test private 25
```input
0
```
```output
No bikes
```
