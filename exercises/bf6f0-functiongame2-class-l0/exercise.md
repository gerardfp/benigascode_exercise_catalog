---
slug: bf6f0-functiongame2-class-l0
tags: [scanner, i/o]
---
# FunctionGame2

Crea els mètodes de la classe FunctionGame2

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

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        FunctionGame2 fg2 = new FunctionGame2();

        String functionName = scanner.next();

        switch (functionName) {
            case "function1":
                for (int i = 5; i-- > 0; ) {
                    int param = scanner.nextInt();
                    boolean returnValue = fg2.function1(param);
                    System.out.println(param + " -> " + returnValue);
                }
                break;
            case "function2":
                for (int i = 6; i-- > 0; ) {
                    float param = scanner.nextFloat();
                    boolean returnValue = fg2.function2(param);
                    System.out.println(param + " -> " + returnValue);
                }
                break;
            case "function3":
                for (int i = 4; i-- > 0; ) {
                    int param1 = scanner.nextInt();
                    String param2 = scanner.next();
                    String returnValue = fg2.function3(param1, param2);
                    System.out.println(param1 + "," + param2 + " -> " + returnValue);
                }
                break;
            case "function4":
                for (int i = 4; i-- > 0; ) {
                    int size = scanner.nextInt();
                    int[] param = new int[size];
                    for (int j = 0; j < size; j++) {
                        param[j] = scanner.nextInt();
                    }
                    int returnValue = fg2.function4(param);
                    System.out.println(Arrays.toString(param) + " -> " + returnValue);
                }
                break;
            case "function5":
                for (int i = 4; i-- > 0; ) {
                    int size = scanner.nextInt();
                    int[] param = new int[size];
                    for (int j = 0; j < size; j++) {
                        param[j] = scanner.nextInt();
                    }
                    int[] returnValue = fg2.function5(param);
                    System.out.println(Arrays.toString(param) + " -> " + Arrays.toString(returnValue));
                }
                break;
            case "function6":
                for (int i = 4; i-- > 0; ) {
                    int param1 = scanner.nextInt();
                    boolean param2 = scanner.nextBoolean();
                    String[] returnValue = fg2.function6(param1, param2);
                    System.out.println(param1 + "," + param2 + " -> " + Arrays.toString(returnValue));
                }
                break;
            case "function7":
                for (int i = 5; i-- > 0; ) {
                    int size = scanner.nextInt();
                    String[] param = new String[size];
                    for (int j = 0; j < size; j++) {
                        param[j] = scanner.next();
                    }
                    int returnValue = fg2.function7(param);
                    System.out.println(Arrays.toString(param) + " -> " + returnValue);
                }
                break;
            case "function8":
                for (int i = 9; i-- > 0; ) {
                    int param1 = scanner.nextInt();
                    int param2 = scanner.nextInt();
                    int param3 = scanner.nextInt();
                    int[] returnValue = fg2.function8(param1, param2, param3);
                    System.out.println(param1 + "," + param2 + "," + param3 + " -> " + Arrays.toString(returnValue));
                }
                break;
        }
    }
}
```

## Tests

### Test
```input
function1 1 2 3 5 10
```
```output
1 -> false
2 -> true
3 -> false
5 -> false
10 -> true
```

### Test
```input
function2 1.34 2.99 -3.2 0.00 10.1 -10.1
```
```output
1.34 -> true
2.99 -> true
-3.2 -> false
0.0 -> true
10.1 -> true
-10.1 -> false
```

### Test
```input
function3 2 hola 4 pa 5 ja 10 mi
```
```output
2,hola -> holahola
4,pa -> papapapa
5,ja -> jajajajaja
10,mi -> mimimimimimimimimimi
```

### Test
```input
function4 3 1 2 3   4 3 4 5 6  2 9 10  5 10 10 10 10 10
```
```output
[1, 2, 3] -> 6
[3, 4, 5, 6] -> 18
[9, 10] -> 19
[10, 10, 10, 10, 10] -> 50
```

### Test
```input
function5 3 1 2 3   4 4 5 6 7  3 10 20 30  5 -1 -2 4 9 7
```
```output
[1, 2, 3] -> [2, 4, 6]
[4, 5, 6, 7] -> [8, 10, 12, 14]
[10, 20, 30] -> [20, 40, 60]
[-1, -2, 4, 9, 7] -> [-2, -4, 8, 18, 14]
```

### Test
```input
function6  2 false   3 true   5 false   6 true
```
```output
2,false -> [falso, falso]
3,true -> [cierto, cierto, cierto]
5,false -> [falso, falso, falso, falso, falso]
6,true -> [cierto, cierto, cierto, cierto, cierto, cierto]
```

### Test
```input
function7   2 java javascript   3 java javascript java   5 swift dart python c# TypeScript   6 java php java java java C    10 c++ java python java haskell go rust kotlin perl bash
```
```output
[java, javascript] -> 1
[java, javascript, java] -> 2
[swift, dart, python, c#, TypeScript] -> 0
[java, php, java, java, java, C] -> 4
[c++, java, python, java, haskell, go, rust, kotlin, perl, bash] -> 2
```

### Test
```input
function8  1 2 3  4 6 5  8 7 9  21 31 11  61 41 51  91 81 71  10 10 11  11 10 10  12 12 12
```
```output
1,2,3 -> [1, 2, 3]
4,6,5 -> [4, 5, 6]
8,7,9 -> [7, 8, 9]
21,31,11 -> [11, 21, 31]
61,41,51 -> [41, 51, 61]
91,81,71 -> [71, 81, 91]
10,10,11 -> [10, 10, 11]
11,10,10 -> [10, 10, 11]
12,12,12 -> [12, 12, 12]
```
