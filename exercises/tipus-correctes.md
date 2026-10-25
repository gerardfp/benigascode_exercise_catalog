---
slug: tipus-correctes
difficulty: 1.0
tags: [variables, types]
---
# Tipus correctes

Completa el següent programa afegint els tipus correctes a cada variable.

## Input

-

## Output

-

## Plantillas

```java
public class Main {

    public static void main(String[] args) {
    	y = 2020;
      	m = "Abril";
      	t = 37.5f;
      	s = false;
      	c = ';';
      
      	System.out.println(y);
      	System.out.println(m);
      	System.out.println(t);
      	System.out.println(s);
      	System.out.println(c);
    }
}
```

## Solutions

```java
void main() {
    int y = 2020;
    String m = "Abril";
    double t = 37.5;
    boolean s = false;
    char c = ';';

    IO.println(y);
    IO.println(m);
    IO.println(t);
    IO.println(s);
    IO.println(c);
}
```

## Tests

### Test
```input
```
```output
2020
Abril
37.5
false
;
```
