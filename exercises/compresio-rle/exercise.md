---
slug: compresio-rle
tags: [for]
---
# Compressió RLE

La codificació Run-length encoding (RLE) és una forma molt simple de compressió de dades en què seqüències de dades amb el mateix valor consecutiu són emmagatzemades com un únic valor més el seu recompte.

Per exemple, la cadena següent cadena de text:

```
BBBBNNNBBBBBNN
```

Es pot comprimir d'aquesta manera:

```
4B3N5B2N
```

S'interpreta com 4 bes, 3 enes, 5 bes, 2 enes.

## Input

Una cadena de `L` caràcters

## Output

La cadena comprimida

## Tests

### Test 10
```input
BN
```
```output
1B1N
```

### Test 10
```input
BBBNNNN
```
```output
3B4N
```

### Test 10
```input
BBBBBNNNB
```
```output
5B3N1B
```

### Test 10
```input
BNNNNNB
```
```output
1B5N1B
```

### Test 10
```input
ABBBAAAANNNCCADDDDD
```
```output
1A3B4A3N2C1A5D
```

### Test 10
```input
WWWWWWWWHHHHHHHAAAAAAATTTTTTTTTTTTTT
```
```output
8W7H7A14T
```

### Test private 10
```input
JAVA
```
```output
1J1A1V1A
```
