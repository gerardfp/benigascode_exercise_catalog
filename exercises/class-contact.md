---
slug: contact-class-l0
tags: [class]
difficulty: 5
---
# Contact

Assigna els valors dels camps a partir de les dades de l'entrada.

## Solutions

```java
class Direccion {
    String calle;
    String codPostal;
    String ciudad;
    String provincia;
}

class Contacto {
    String nombre;
    String apellidos;
    Direccion direccion;
}

void main() {
    Scanner scanner = new Scanner(System.in);

    Contacto contacto = new Contacto();
    contacto.direccion = new Direccion();

    contacto.nombre = scanner.nextLine();
    contacto.apellidos = scanner.nextLine();
    contacto.direccion.calle = scanner.nextLine();
    contacto.direccion.codPostal = scanner.nextLine();
    contacto.direccion.ciudad = scanner.nextLine();
    contacto.direccion.provincia = scanner.nextLine();

    IO.println(contacto.apellidos + ", " + contacto.nombre);
    IO.println(contacto.direccion.calle);
    IO.println(contacto.direccion.codPostal + " - " + contacto.direccion.ciudad);
    IO.println(contacto.direccion.provincia);
}
```

## Plantillas

```java
import java.util.Scanner;

class Direccion {
    String calle;
    String codPostal;
    String ciudad;
    String provincia;
}

class Contacto {
    String nombre;
    String apellidos;
    Direccion direccion;
}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Contacto contacto = new Contacto();
      
        contacto.direccion = new Direccion();

		// escriu aqui el codi

        System.out.println(contacto.apellidos + ", " + contacto.nombre);
        System.out.println(contacto.direccion.calle);
        System.out.println(contacto.direccion.codPostal + " - " + contacto.direccion.ciudad);
        System.out.println(contacto.direccion.provincia);
    }
}
```

## Tests

### Test
```input
Adrian
Droide Perez
C/Calleja, 2
09876
Barcelona
Barcelona
```
```output
Droide Perez, Adrian
C/Calleja, 2
09876 - Barcelona
Barcelona
```

### Test private
```input
Alba
Bosa Garcia
C/Callejon, 4, 3a
01234
Madrid
Madrid
```
```output
Bosa Garcia, Alba
C/Callejon, 4, 3a
01234 - Madrid
Madrid
```
