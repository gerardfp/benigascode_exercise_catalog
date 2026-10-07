---
slug: ebeac-fighters-class-l0
---
# Fighters

Implementa el mètode Fight.winner()

El resultat del combat es decideix en funció de les característiques dels combatents. Guanya el que tingui la suma de força, velocitat i agilitat més alta. Si els dos combatents tenen la mateixa es produeix un DOBLE KO.

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


class Fighter {
    String name;
    float strength;
    float speed;
    float agility;

    Fighter(String name, float strength, float speed, float agility) {
        this.name = name;
        this.strength = strength;
        this.speed = speed;
        this.agility = agility;
    }

    float getSum(){
        return strength + speed + agility;
    }
}

class Fight {
    // escriu el codi aqui
}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Fighter f1 = new Fighter(scanner.next(), scanner.nextFloat(), scanner.nextFloat(), scanner.nextFloat());
        Fighter f2 = new Fighter(scanner.next(), scanner.nextFloat(), scanner.nextFloat(), scanner.nextFloat());

        Fighter winner = new Fight().winner(f1, f2);

        System.out.println(winner == null ? "DOUBLE KO" : winner.name);
    }
}
```

## Tests

### Test 33.33
```input
ryu 80 90 80
honda 100 60 50
```
```output
ryu
```

### Test private 33.33
```input
blanka 80 80 80
chun-li 60 90 100
```
```output
chun-li
```

### Test private 33.34
```input
ryu 80 90 80
ken 80 80 90
```
```output
DOUBLE KO
```
