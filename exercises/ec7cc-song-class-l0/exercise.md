---
slug: ec7cc-song-class-l0
tags: [class, L0]
---
# Song

Crea l'objecte `song` i asigna-li els camps amb les dades de l'entrada.

## Input

-

## Output

-

## Plantillas

```java
import java.util.Scanner;


class Song {
    String name;
    String artist;
    float rating;
    boolean favorite;
}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // escriu aqui el codi

        System.out.print(song.favorite ? "<3 " : "   ");
        System.out.println(song.artist + " - " + song.name);
        for (int i = 0; i < (int) song.rating; i++) {
            System.out.print("*");
        }
    }
}
```

## Tests

### Test
```input
One love
Bob Marley
4.5
true
```
```output
<3 Bob Marley - One love
****
```

### Test
```input
Hey Joe
Jimmi Hendrix
4.8
true
```
```output
<3 Jimmi Hendrix - Hey Joe
****
```

### Test private
```input
Whole Lotta Love
Led Zeppelin
4.6
false
```
```output
   Led Zeppelin - Whole Lotta Love
****
```
