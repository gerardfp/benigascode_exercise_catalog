---
slug: aac7e-functiongame-class-l0
tags: [scanner, i/o]
---
# FunctionGame

Implementa els mètodes (funcions) de la classe FunctionGame

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

class FunctionGame {
  
  // escriu el codi aqui

}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        FunctionGame functionGame = new FunctionGame();

        String functionName = scanner.next();

        if("function1".equals(functionName)){
            for (int i = 5; i-->0;) {
                int param = scanner.nextInt();
                int returnValue = functionGame.function1(param);
                System.out.println(param + " -> " + returnValue);
            }
        } else if("function2".equals(functionName)){
            for (int i = 5; i-->0;) {
                int param = scanner.nextInt();
                int returnValue = functionGame.function2(param);
                System.out.println(param + " -> " + returnValue);
            }
        } else if("function3".equals(functionName)){
            for (int i = 5; i-->0;) {
                int param = scanner.nextInt();
                int returnValue = functionGame.function3(param);
                System.out.println(param + " -> " + returnValue);
            }
        } else if("function4".equals(functionName)){
            for (int i = 5; i-->0;) {
                int param = scanner.nextInt();
                int returnValue = functionGame.function4(param);
                System.out.println(param + " -> " + returnValue);
            }
        } else if("function5".equals(functionName)){
            for (int i = 5; i-->0;) {
                int param = scanner.nextInt();
                int returnValue = functionGame.function5(param);
                System.out.println(param + " -> " + returnValue);
            }
        }  else if("function6".equals(functionName)){
            for (int i = 5; i-->0;) {
                int param1 = scanner.nextInt();
                int param2 = scanner.nextInt();
                int returnValue = functionGame.function6(param1, param2);
                System.out.println(param1 + "," + param2 + " -> " + returnValue);
            }
        } else if("function7".equals(functionName)){
            for (int i = 7; i-->0;) {
                int param1 = scanner.nextInt();
                int param2 = scanner.nextInt();
                int returnValue = functionGame.function7(param1, param2);
                System.out.println(param1 + "," + param2 + " -> " + returnValue);
            }
        } else if("function8".equals(functionName)){
            for (int i = 7; i-->0;) {
                int param1 = scanner.nextInt();
                int param2 = scanner.nextInt();
                int param3 = scanner.nextInt();
                int returnValue = functionGame.function8(param1, param2, param3);
                System.out.println(param1 + "," + param2 + "," + param3 + " -> " + returnValue);
            }
        }
    }
}
```

## Tests

### Test 12.5
```input
function1 1 2 3 5 10
```
```output
1 -> 2
2 -> 3
3 -> 4
5 -> 6
10 -> 11
```

### Test 12.5
```input
function2 1 2 3 5 10
```
```output
1 -> -2
2 -> -1
3 -> 0
5 -> 2
10 -> 7
```

### Test private 12.5
```input
function3 1 2 3 5 10
```
```output
1 -> 10
2 -> 20
3 -> 30
5 -> 50
10 -> 100
```

### Test private 12.5
```input
function4 1 2 3 5 10
```
```output
1 -> 1
2 -> 3
3 -> 5
5 -> 9
10 -> 19
```

### Test private 12.5
```input
function5 1 2 3 5 10
```
```output
1 -> 6
2 -> 6
3 -> 6
5 -> 6
10 -> 6
```

### Test private 12.5
```input
function6 1 1 2 2 3 4 5 9 10 11
```
```output
1,1 -> 2
2,2 -> 4
3,4 -> 7
5,9 -> 14
10,11 -> 21
```

### Test private 12.5
```input
function7 1 2 3 4 7 5 8 5 11 8 5 5 3 3
```
```output
1,2 -> 2
3,4 -> 4
7,5 -> 7
8,5 -> 8
11,8 -> 11
5,5 -> 5
3,3 -> 3
```

### Test private 12.5
```input
function8 1 2 3  5 4 6  9 8 7  9 7 7  8 8 9  7 9 7   10 10 10
```
```output
1,2,3 -> 1
5,4,6 -> 4
9,8,7 -> 7
9,7,7 -> 7
8,8,9 -> 8
7,9,7 -> 7
10,10,10 -> 10
```
