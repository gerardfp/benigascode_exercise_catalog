---
slug: a2e8f-usuari-class-l0
tags: [class, L0]
---
# Usuari

Utilitza el mètode constructor de la clase User per a crear i inicialitzar els objectes necessaris.

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


class User {
    int id;
    String username;
    String displayName;
    String email;

    User(int id, String username, String displayName, String email) {
        this.id = id;
        this.username = username;
        this.displayName = displayName;
        this.email = email;
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

		// escriu el codi aqui

        String format = "%6d | %-8s | %-16s | %-18s %n";
        System.out.format(format, user1.id, user1.username, user1.displayName, user1.email);
        System.out.format(format, user2.id, user2.username, user2.displayName, user2.email);
        System.out.format(format, user3.id, user3.username, user3.displayName, user3.email);
    }
}
```

## Tests

### Test
```input
```
```output
  1001 | acasas   | Armando Casas    | acasas@mail.com    
  1002 | equito   | Esteban Quito    | equito@mail.com    
  1003 | centes   | Cindy Entes      | centes@mail.com  
```
