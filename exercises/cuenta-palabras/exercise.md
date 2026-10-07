---
slug: cuenta-palabras
---
# Cuenta palabras

Dado un texto, cuenta el número de palabras que contiene.

## Input

Un string con varios saltos de línea.
El texto termina con la palabra END (que no debe procesarse)

1 <= L <= 100

## Output

Un entero indicando el número de palabras

## Tests

### Test 20
```input
hola mundo!
END
```
```output
2
```

### Test 20
```input
hola, que tal.
END
```
```output
3
```

### Test private 20
```input
Lorem ipsum dolor sit amet,
consectetur adipiscing elit.
END
```
```output
8
```

### Test private 20
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

### Test private 20
```input
hola
END
```
```output
1
```
