---
slug: cuenta-palabras
difficulty: 5
---
# Cuenta palabras

Dado un texto, cuenta el número de palabras que contiene.

## Input

Un string con varios saltos de línea.
El texto termina con la palabra END (que no debe procesarse)

## Output

Un entero indicando el número de palabras

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int count = 0;
    while (sc.hasNext()) {
        String word = sc.next();
        if (word.equals("END")) {
            break;
        }
        count++;
    }
    IO.println(count);
}
```

## Tests

### Test
```input
hola mundo!
END
```
```output
2
```

### Test
```input
hola, que tal.
END
```
```output
3
```

### Test
```input
Lorem ipsum dolor sit amet,
consectetur adipiscing elit.
END
```
```output
8
```

### Test
```input
Lorem ipsum
dolor sit amet,
consectetur adipiscing
elit.
END
```
```output
8
```

### Test private
```input
hola
END
```
```output
1
```
