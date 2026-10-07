---
slug: e2ac7-rebajas-class-l0
tags: [class, L0]
---
# Rebaixes

-

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

class Producto {
    String descripcion;
    float precio;

    Producto(String descripcion, float precio) {
        this.descripcion = descripcion;
        this.precio = precio;
    }

    public String toString() {
        // escriu el codi aqui
    }
}

class Descuento {
    float valor;

    Descuento(float valor) {
        this.valor = valor;
    }

  	// escriu el codi aqui
}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.US);

        Producto producto = new Producto(scanner.next(), scanner.nextFloat());

        System.out.println(producto);

        Descuento descuento = new Descuento(scanner.nextFloat());

        descuento.aplicar(producto);

        System.out.println(producto);
    }
}
```

## Tests

### Test
```input
producto1 10
15
```
```output
Producto{descripcion='producto1', precio=10.0}
Producto{descripcion='producto1', precio=8.5}
```

### Test
```input
productoX 100
25
```
```output
Producto{descripcion='productoX', precio=100.0}
Producto{descripcion='productoX', precio=75.0}
```

### Test private
```input
productoV 4.5
1.5
```
```output
Producto{descripcion='productoV', precio=4.5}
Producto{descripcion='productoV', precio=4.4325}
```
