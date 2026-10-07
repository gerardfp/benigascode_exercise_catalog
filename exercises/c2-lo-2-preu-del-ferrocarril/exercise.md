---
slug: c2-lo-2-preu-del-ferrocarril
---
# Preu del ferrocarril

Escriu un programa que determini el preu d'un bolet d'anada i tornada en ferrocarril, donada la distància a recòrrer i la quantitat en dies en el destí, sabent que:

- Si l'estada és de més de 7 dies i la distància és més de 800km, el bolet té un descompte del 30%.

- El preu per quilòmetre és de 0.35 euros.

## Input

La distància  a del viatge (float).

La quantitat  de dies en el destí (int).

## Output

El preu del bolet.

## Tests

### Test 10
```input
100.0 1
```
```output
35.0
```

### Test 10
```input
200.0 1
```
```output
70.0
```

### Test private 10
```input
900.0 1
```
```output
315.0
```

### Test private 10
```input
100.0 10
```
```output
35.0
```

### Test private 10
```input
900.0 10
```
```output
220.5
```

### Test private 10
```input
800.0 7
```
```output
280.0
```

### Test private 10
```input
801.0 7
```
```output
280.35
```

### Test private 10
```input
800.0 8
```
```output
280.0
```

### Test private 10
```input
801.0 8
```
```output
196.245
```

### Test private 10
```input
234.5 1
```
```output
82.075
```
