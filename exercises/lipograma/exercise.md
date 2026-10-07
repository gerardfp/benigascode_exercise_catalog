---
slug: lipograma
---
# Lipograma

Donat un text i una lletra, dir si el text **omet** aquesta lletra.

## Input

En primer lloc va el text, en vàries línies, i acabat amb .

A continuació ve el caràcter.

## Output

true | false

## Tests

### Test
```input
Hello world!
END
e
```
```output
false
```

### Test
```input
Hello World!
END
a
```
```output
true
```

### Test
```input
Hello World!
END
u
```
```output
true
```

### Test
```input
Lorem ipsum 
dolor sit amet, 
consectetur adipiscing elit
END
x
```
```output
true
```

### Test
```input
a
END
a
```
```output
false
```

### Test
```input
Lorem ipsum 
dolor sit amet, 
consectetur adipiscing
END
g
```
```output
false
```

### Test
```input
aaaa
END
a
```
```output
false
```

### Test
```input
aaaa
END
e
```
```output
true
```
