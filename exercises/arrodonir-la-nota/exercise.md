---
slug: arrodonir-la-nota
tags: [conversio]
---
# Arrodonir la nota

Al butlletí de notes no es poden posar notes amb decimals, així que el professor ha decidit arrodonir-les. Si els decimals estan per sota de 0.5 es trunca la nota (es lleven els decimals), però si són igual o majors que 0.5 aleshores s'arrodoneix cap amunt.

## Input

Una nota amb o sense decimals

## Output

enter

## Plantillas

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
      
      
    }
}
```

## Tests

### Test
```input
5.1
```
```output
5
```

### Test
```input
7.49
```
```output
7
```

### Test
```input
10
```
```output
10
```

### Test
```input
4.5
```
```output
5
```

### Test
```input
7.75
```
```output
8
```

### Test private
```input
6
```
```output
6
```
