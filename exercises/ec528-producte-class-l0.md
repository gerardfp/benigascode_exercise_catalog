---
slug: ec528-producte-class-l0
tags: [class]
---
# Producte

Assigna els valors als camps de l'objecte `producte` a partir de les dades de l'entrada.

## Input

-

## Output

-

## Plantillas

```java
import java.util.Scanner;


class Producte {
    String nom;
    String descripcio;
    float preu;
    int stock;
}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Producte producte = new Producte();

        // escriu aqui el codi

        System.out.println("Nom:        " + producte.nom);
        System.out.println("Descripcio: " + producte.descripcio);
        System.out.println("Preu:       " + producte.preu);
        System.out.println("Stock:      " + producte.stock);
    }
}
```

## Tests

### Test
```input
Corsair Vengeance RGB Pro
DDR4 3200 PC4-25600 16GB 2x8GB CL16
109
25
```
```output
Nom:        Corsair Vengeance RGB Pro
Descripcio: DDR4 3200 PC4-25600 16GB 2x8GB CL16
Preu:       109.0
Stock:      25
```

### Test
```input
Kingston HyperX Fury Black
16GB DDR4 2666Mhz PC-21300 (2x8GB) CL16
79.5
3
```
```output
Nom:        Kingston HyperX Fury Black
Descripcio: 16GB DDR4 2666Mhz PC-21300 (2x8GB) CL16
Preu:       79.5
Stock:      3
```

### Test private
```input
G.Skill Trident Z RGB
DDR4 3200 PC4-25600 16GB 2x8GB CL16
113.39
55
```
```output
Nom:        G.Skill Trident Z RGB
Descripcio: DDR4 3200 PC4-25600 16GB 2x8GB CL16
Preu:       113.39
Stock:      55
```
