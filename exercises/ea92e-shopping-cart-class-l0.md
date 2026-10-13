---
slug: ea92e-shopping-cart-class-l0
tags: [class, L0]
---
# Shopping Cart

Crea les classes necessàries.

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


// escriu el codi aqui

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        ShoppingCart shoppingCart = new ShoppingCart();

        int nProducts = scanner.nextInt();
        scanner.nextLine();

        shoppingCart.products = new Product[nProducts];

        for (int i = 0; i < nProducts; i++) {
            shoppingCart.products[i] = new Product();
            shoppingCart.products[i].name = scanner.nextLine();
            shoppingCart.products[i].price = scanner.nextFloat();
            scanner.nextLine();
        }

        System.out.println("ShoppingCart");
        for (int i = 0; i < nProducts; i++) {
            System.out.format("%40s  %6.2f%n", shoppingCart.products[i].name, shoppingCart.products[i].price);
        }
    }
}
```

## Tests

### Test
```input
4
FREKVENS Altavoz, 10x20 cm
59
SYMFONISK Altavoz wifi, 31x10x15 cm
105.9
ENEBY Altavoz Bluetooth, 20x20 cm
49.99
ENEBY Altavoz Bluetooth, 30x30 cm
89.99
```
```output
ShoppingCart
              FREKVENS Altavoz, 10x20 cm   59.00
     SYMFONISK Altavoz wifi, 31x10x15 cm  105.90
       ENEBY Altavoz Bluetooth, 20x20 cm   49.99
       ENEBY Altavoz Bluetooth, 30x30 cm   89.99
```

### Test private
```input
2
LILLHULT MiniUSB cable, 0.4 m
2.25
LILLHULT USB tipo C cable, 1.5 m
4.45
```
```output
ShoppingCart
           LILLHULT MiniUSB cable, 0.4 m    2.25
        LILLHULT USB tipo C cable, 1.5 m    4.45
```
