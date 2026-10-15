---
slug: class-enemy
tags: [class]
difficulty: 5
---
# Enemy

Implementa les classes necessàries

## Solutions

```java
class Stat {
    int value;
    int max;

    Stat(int value, int max) {
        this.value = value;
        this.max = max;
    }
}

class Enemy {
    Stat health;
    Stat weapon;

    Enemy(String type) {
        if ("guerrero".equalsIgnoreCase(type)) {
            health = new Stat(50, 50);
            weapon = new Stat(60, 60);
        } else if ("amazona".equalsIgnoreCase(type)) {
            health = new Stat(40, 40);
            weapon = new Stat(70, 70);
        } else if ("brujo".equalsIgnoreCase(type)) {
            health = new Stat(30, 30);
            weapon = new Stat(80, 80);
        }
    }
}

void main() {
    Enemy guerrero = new Enemy("guerrero");
    Enemy amazona = new Enemy("amazona");
    Enemy brujo = new Enemy("brujo");

    IO.println("GUERRERO  " +
            "Health: " + guerrero.health.value + "/" + guerrero.health.max + "   " +
            "Weapon: " + guerrero.weapon.value + "/" + guerrero.weapon.max);

    IO.println("AMAZONA   " +
            "Health: " + amazona.health.value + "/" + amazona.health.max + "   " +
            "Weapon: " + amazona.weapon.value + "/" + amazona.weapon.max);

    IO.println("BRUJO     " +
            "Health: " + brujo.health.value + "/" + brujo.health.max + "   " +
            "Weapon: " + brujo.weapon.value + "/" + brujo.weapon.max);
}
```

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// escriu el codi aqui

public class Main {

    public static void main(String[] args) {
      
        Enemy guerrero = new Enemy("guerrero");
        Enemy amazona = new Enemy("amazona");
        Enemy brujo = new Enemy("brujo");

        System.out.println("GUERRERO  " +
                "Health: " + guerrero.health.value + "/" + guerrero.health.max + "   " +
                "Weapon: " + guerrero.weapon.value + "/" + guerrero.weapon.max);

        System.out.println("AMAZONA   " +
                "Health: " + amazona.health.value + "/" + amazona.health.max + "   " +
                "Weapon: " + amazona.weapon.value + "/" + amazona.weapon.max);

        System.out.println("BRUJO     " +
                "Health: " + brujo.health.value + "/" + brujo.health.max + "   " +
                "Weapon: " + brujo.weapon.value + "/" + brujo.weapon.max);
    }
}
```

## Tests

### Test
```input
```
```output
GUERRERO  Health: 50/50   Weapon: 60/60
AMAZONA   Health: 40/40   Weapon: 70/70
BRUJO     Health: 30/30   Weapon: 80/80
```
