---
slug: compresio-rle
difficulty: 4.0
tags: [strings, loops]
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

Una cadena de L caràcters

## Output

La cadena comprimida

## Tests

### Test
```input
BN
```
```output
1B1N
```

### Test
```input
BBBNNNN
```
```output
3B4N
```

### Test
```input
BBBBBNNNB
```
```output
5B3N1B
```

### Test
```input
BNNNNNB
```
```output
1B5N1B
```

### Test
```input
ABBBAAAANNNCCADDDDD
```
```output
1A3B4A3N2C1A5D
```

### Test
```input
WWWWWWWWHHHHHHHAAAAAAATTTTTTTTTTTTTT
```
```output
8W7H7A14T
```

### Test private
```input
JAVA
```
```output
1J1A1V1A
```
