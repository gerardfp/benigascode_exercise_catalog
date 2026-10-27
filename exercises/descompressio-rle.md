---
slug: descompressio-rle
difficulty: 5.0
tags: [strings, loops]
---
# Descompressió RLE

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

Una cadena de `L` caracters comprimida en RLE

## Output

La cadena descomprimida

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNext()) {
        String s = sc.next();
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= '0' && c <= '9') {
                count = count * 10 + (c - '0');
            } else {
                for (int j = 0; j < count; j++) {
                    IO.print(c);
                }
                count = 0;
            }
        }
        IO.println();
    }
}
```

## Tests

### Test
```input
3B4N
```
```output
BBBNNNN
```

### Test
```input
3B4N
```
```output
BBBNNNN
```

### Test
```input
5B3N1B
```
```output
BBBBBNNNB
```

### Test
```input
1B5N1B
```
```output
BNNNNNB
```

### Test
```input
1A3B4A3N2C1A5D
```
```output
ABBBAAAANNNCCADDDDD
```

### Test
```input
8W7H7A9T
```
```output
WWWWWWWWHHHHHHHAAAAAAATTTTTTTTT
```

### Test private
```input
1J1A1V1A
```
```output
JAVA
```
