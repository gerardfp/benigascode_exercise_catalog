---
slug: c3-l2-7-descompressio-rle
tags: [scanner, i/o]
---
# Descompressió RLE

La codificació Run-length encoding (RLE) és una forma molt simple de compressió de dades en què seqüències de dades amb el mateix valor consecutiu són emmagatzemades com un únic valor més el seu recompte.

Per exemple, la cadena següent cadena de text:

```text
BBBBNNNBBBBBNN
```

Es pot comprimir d'aquesta manera:

```text
4B3N5B2N
```

S'interpreta com 4 bes, 3 enes, 5 bes, 2 enes.

## Input

Una cadena de L caracters comprimida en RLE

No hi ha cap recompte superior a 9

## Output

La cadena descomprimida

## Tests

### Test 14.29
```input
3B4N
```
```output
BBBNNNN
```

### Test 14.29
```input
3B4N
```
```output
BBBNNNN
```

### Test private 14.29
```input
5B3N1B
```
```output
BBBBBNNNB
```

### Test private 14.29
```input
1B5N1B
```
```output
BNNNNNB
```

### Test private 14.29
```input
1A3B4A3N2C1A5D
```
```output
ABBBAAAANNNCCADDDDD
```

### Test private 14.29
```input
8W7H7A9T
```
```output
WWWWWWWWHHHHHHHAAAAAAATTTTTTTTT
```

### Test private 14.26
```input
1J1A1V1A
```
```output
JAVA
```
