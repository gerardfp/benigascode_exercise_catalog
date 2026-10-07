---
slug: f2eb6-players
tags: [class, L0]
---
# Players

Crea els objectes necessaris.

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


class Coords {
    int x, y;
}

class Player {
    String name;
    Coords position;
    int score;
}

class Game {
    int width;
    int height;
    Player player1;
    Player player2;
}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
      
      
      	// escriu aqui el codi
      
      
      	game.width = scanner.nextInt();
        game.height = scanner.nextInt();

        game.player1.name = scanner.next();
        game.player1.score = scanner.nextInt();
        game.player1.position.x = scanner.nextInt();
        game.player1.position.y = scanner.nextInt();

        game.player2.name = scanner.next();
        game.player2.score = scanner.nextInt();
        game.player2.position.x = scanner.nextInt();
        game.player2.position.y = scanner.nextInt();


        System.out.println("P1:" + game.player1.name + " #" + game.player1.score + " {"+game.player1.position.x+", "+game.player1.position.y+"}");
        System.out.println("P2:" + game.player2.name + " #" + game.player2.score + " {"+game.player2.position.x+", "+game.player2.position.y+"}");

    }
}
```

## Tests

### Test
```input
10 10
a 2300 9 5
b 5700 7 6
```
```output
P1:a #2300 {9, 5}
P2:b #5700 {7, 6}
```

### Test private
```input
20 20
gcd 17900 10 10
mcm 8000 14 3
```
```output
P1:gcd #17900 {10, 10}
P2:mcm #8000 {14, 3}
```
