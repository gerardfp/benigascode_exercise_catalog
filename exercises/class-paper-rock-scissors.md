---
slug: d3da3-paper-rock-scissors-class-l0
tags: [class, L0]
difficulty: 5
---
# Paper, rock, scissors

Implementa les classes `Game` i `Player`

## Solutions

```java
class Player {
    int points;

    Player(int points) {
        this.points = points;
    }
}

class Game {
    Player player1;
    Player player2;

    Game(Player player1, Player player2) {
        this.player1 = player1;
        this.player2 = player2;
    }
}

void main() {
    Scanner scanner = new Scanner(System.in);

    Game game = new Game(new Player(0), new Player(0));

    int numRondas = scanner.nextInt();

    for (int i = 0; i < numRondas; i++) {
        String ronda = scanner.next();
        if (ronda.equals("@%") || ronda.equals("#@") || ronda.equals("%#")) {
            game.player1.points++;
        } else if (ronda.equals("%@") || ronda.equals("@#") || ronda.equals("#%")) {
            game.player2.points++;
        }
    }

    if (game.player1.points > game.player2.points) {
        IO.println("PLAYER 1 WINS");
    } else if (game.player2.points > game.player1.points) {
        IO.println("PLAYER 2 WINS");
    } else {
        IO.println("TIE");
    }
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
        Scanner scanner = new Scanner(System.in);

        Game game = new Game(new Player(0), new Player(0));

        int numRondas = scanner.nextInt();

        for (int i = 0; i < numRondas; i++) {
            String ronda = scanner.next();
            if(ronda.equals("@%") || ronda.equals("#@") || ronda.equals("%#")){
                game.player1.points++;
            } else if(ronda.equals("%@") || ronda.equals("@#") || ronda.equals("#%")){
                game.player2.points++;
            }
        }

        if(game.player1.points > game.player2.points){
            System.out.println("PLAYER 1 WINS");
        } else if(game.player2.points > game.player1.points){
            System.out.println("PLAYER 2 WINS");
        } else {
            System.out.println("TIE");
        }
    }
}
```

## Tests

### Test
```input
4 ## @# %# %@
```
```output
PLAYER 2 WINS
```

### Test
```input
6 #@ %@ %# #% %@ @%
```
```output
TIE
```

### Test private
```input
6 @% @% %# %# #% #@
```
```output
PLAYER 1 WINS
```
