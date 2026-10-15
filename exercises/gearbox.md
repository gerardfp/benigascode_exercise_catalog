---
slug: gearbox
tags: [class]
difficulty: 3
---
# GearBox

Implementa els mètodes GearBox.gearUp() i GearBox.gearDown()

- gearUp() incrementa la 'gear' en 1. Quan s'arriba a límit 'numGears', no s'ha d'incrementar
- gearDown() decrementa la 'gear' en 1. Quan s'arriba a '-1' (marxa enrere), no s'ha de decrementar

## Input

-

## Output

-

## Solutions

```java
class GearBox {
    int gear;
    int numGears;

    void gearUp() {
        if (gear < numGears) {
            gear++;
        }
    }

    void gearDown() {
        if (gear > -1) {
            gear--;
        }
    }

    void show() {
        IO.print("Current gear: ");
        switch (gear) {
            case -1 -> IO.println("R");
            case 0 -> IO.println("N");
            default -> IO.println(gear);
        }
    }
}

void main() {
    Scanner scanner = new Scanner(System.in);
    GearBox gearBox = new GearBox();
    gearBox.numGears = scanner.nextInt();
    scanner.nextLine();

    String action;
    while (!(action = scanner.nextLine()).equals("__END__")) {
        switch (action) {
            case "UP" -> gearBox.gearUp();
            case "DOWN" -> gearBox.gearDown();
        }
        gearBox.show();
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

class GearBox {
    int gear;
    int numGears;

    void show(){
        System.out.print("Current gear: ");

        switch (gear){
            case -1:
                System.out.println("R");
                break;
            case 0:
                System.out.println("N");
                break;
            default:
                System.out.println(gear);
        }
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

	    GearBox gearBox = new GearBox();
        gearBox.numGears = scanner.nextInt();
        scanner.nextLine();

        String action;
        while(!(action = scanner.nextLine()).equals("__END__")){
            switch (action){
                case "UP":
                    gearBox.gearUp();
                    break;
                case "DOWN":
                    gearBox.gearDown();
                    break;
            }
            gearBox.show();
        }
    }
}
```

## Tests

### Test
```input
5
UP
UP
UP
DOWN
DOWN
__END__
```
```output
Current gear: 1
Current gear: 2
Current gear: 3
Current gear: 2
Current gear: 1
```

### Test
```input
6
UP
UP
DOWN
DOWN
DOWN
__END__
```
```output
Current gear: 1
Current gear: 2
Current gear: 1
Current gear: N
Current gear: R
```

### Test
```input
6
UP
UP
DOWN
DOWN
DOWN
__END__
```
```output
Current gear: 1
Current gear: 2
Current gear: 1
Current gear: N
Current gear: R
```

### Test
```input
5
UP
UP
UP
UP
UP
UP
__END__
```
```output
Current gear: 1
Current gear: 2
Current gear: 3
Current gear: 4
Current gear: 5
Current gear: 5
```

### Test private
```input
5
UP
UP
UP
UP
UP
UP
DOWN
DOWN
DOWN
DOWN
DOWN
DOWN
DOWN
DOWN
__END__
```
```output
Current gear: 1
Current gear: 2
Current gear: 3
Current gear: 4
Current gear: 5
Current gear: 5
Current gear: 4
Current gear: 3
Current gear: 2
Current gear: 1
Current gear: N
Current gear: R
Current gear: R
Current gear: R
```
