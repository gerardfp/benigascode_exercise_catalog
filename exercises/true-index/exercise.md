---
slug: true-index
---
# True index

Crea un array de 100 booleans, i estableix els elements en els índexs indicats a `true`.

## Input

Una sèrie de números enters que representen l'índex dels elements que han de ser `true`. La sèrie acaba amb un `-1`.

## Output

-

## Plantillas

```java
import java.util.Scanner;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
      	Scanner scanner= new Scanner(System.in);

      	// crea l'array de 100 booleans
      
      
        int index = scanner.nextInt();
        while(index != -1){
          	// assigna el valor 'true' a l'element de l'array en la posicio 'index'
			
          
            index = scanner.nextInt();
        }

        System.out.println(Arrays.toString(array));
    }
}
```

## Tests

### Test 20
```input
0 1 2 3 4   -1
```
```output
[true, true, true, true, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]
```

### Test 20
```input
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49   -1
```
```output
[false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]
```

### Test private 20
```input
90 91 92 93 94 95 96 97 98 99   -1
```
```output
[false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, true, true, true, true, true, true, true, true, true]
```

### Test private 20
```input
-1
```
```output
[false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]
```

### Test private 20
```input
45 78 93 23 4 55 61  -1
```
```output
[false, false, false, false, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, false, false, false, false, false, false, false, false, false, true, false, false, false, false, false, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, false, false, false, false, false, false]
```
