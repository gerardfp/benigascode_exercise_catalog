---
slug: dad4d-libro-class-l0
tags: [class, L0]
---
# Libro

Crea les classes `Libro` i `Autor`

## Input

-

## Output

-

## Plantillas

```java
import java.util.Scanner;

// escriu el codi aqui



public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Libro libro = new Libro();
      
        libro.autor = new Autor();

        libro.titulo = scanner.nextLine();
        libro.ISBN = scanner.nextLine();
        libro.rating = scanner.nextFloat();
        scanner.nextLine();
        libro.autor.nombre = scanner.nextLine();
        libro.autor.rating = scanner.nextFloat();

        System.out.println(libro.ISBN);
        System.out.println(libro.titulo);
        System.out.println(new String(new char[(int)libro.rating]).replace("\0","*"));
        System.out.println(libro.autor.nombre);
        System.out.println(new String(new char[(int)libro.autor.rating]).replace("\0","*"));

    }
}
```

## Tests

### Test
```input
C Programming Language
978-0131103627
4.5
Dennis M. Ritchie
5
```
```output
978-0131103627
C Programming Language
****
Dennis M. Ritchie
*****
```

### Test
```input
Expert C Programming: Deep C Secrets
978-0131774292
4.7
Peter van der Linden
5
```
```output
978-0131774292
Expert C Programming: Deep C Secrets
****
Peter van der Linden
*****
```

### Test private
```input
C: A Reference Manual
978-0130895929
5
Samuel P. Harbison
5
```
```output
978-0130895929
C: A Reference Manual
*****
Samuel P. Harbison
*****
```
