---
slug: class-fusion
tags: [class]
difficulty: 5
---
# Fusion

Crea el mètode `Fusion.fusionar()`

## Solutions

```java
class Personaje {
    int fuerza;
    int velocidad;

    Personaje(int fuerza, int velocidad) {
        this.fuerza = fuerza;
        this.velocidad = velocidad;
    }

    @Override
    public String toString() {
        return "fuerza=" + fuerza + ", velocidad=" + velocidad;
    }
}

class Fusion {
    Personaje fusionar(Personaje a, Personaje b) {
        return new Personaje(a.fuerza + b.fuerza, a.velocidad + b.velocidad);
    }
}

void main() {
    Personaje goku = new Personaje(100, 100);
    Personaje vegeta = new Personaje(90, 90);
    Personaje goten = new Personaje(80, 100);
    Personaje trunks = new Personaje(70, 90);

    Personaje gotenks = new Fusion().fusionar(goten, trunks);
    Personaje gogeta = new Fusion().fusionar(goku, vegeta);

    IO.println("Goku: " + goku);
    IO.println("Vegeta: " + vegeta);
    IO.println("Goten: " + goten);
    IO.println("Trunks: " + trunks);
    IO.println("Gotenks: " + gotenks);
    IO.println("Gogeta: " + gogeta);
}
```

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Personaje {
    int fuerza;
    int velocidad;

    Personaje(int fuerza, int velocidad) {
        this.fuerza = fuerza;
        this.velocidad = velocidad;
    }

    @Override
    public String toString() {
        return "fuerza=" + fuerza + ", velocidad=" + velocidad;
    }
}

class Fusion {
    // escriu el codi aqui
}

public class Main {

    public static void main(String[] args) {

        Personaje goku = new Personaje(100, 100);
        Personaje vegeta = new Personaje(90, 90);
        Personaje goten = new Personaje(80, 100);
        Personaje trunks = new Personaje(70, 90);

        Personaje gotenks = new Fusion().fusionar(goten, trunks);
        Personaje gogeta = new Fusion().fusionar(goku, vegeta);

        System.out.println("Goku: " + goku);
        System.out.println("Vegeta: " + vegeta);
        System.out.println("Goten: " + goten);
        System.out.println("Trunks: " + trunks);
        System.out.println("Gotenks: " + gotenks);
        System.out.println("Gogeta: " + gogeta);
    }
}
```

## Tests

### Test
```input
```
```output
Goku: fuerza=100, velocidad=100
Vegeta: fuerza=90, velocidad=90
Goten: fuerza=80, velocidad=100
Trunks: fuerza=70, velocidad=90
Gotenks: fuerza=150, velocidad=190
Gogeta: fuerza=190, velocidad=190
```
