---
slug: elimina-vocales
tags: [strings, loops, filtering, string-manipulation]
difficulty: 3
---
# Elimina vocales

Dada una frase (terminada con un salto de linea), escribe la misma frase pero eliminando las vocales.

## Input

Una frase terminada con un salto de linea '\n'

## Output

La frase sin las vocales.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNextLine()) {
        String s = sc.nextLine();
        String res = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                continue;
            }
            res += c;
        }
        IO.println(res);
    }
}
```

## Tests

### Test
```input
hola mundo!
```
```output
hl mnd!
```

### Test
```input
lalalA
```
```output
lll
```

### Test
```input
xa, XA, xE, xI, xO, xu
```
```output
x, X, x, x, x, x
```

### Test
```input
xAaAxeEe
```
```output
xx
```

### Test private
```input
la
```
```output
l
```
