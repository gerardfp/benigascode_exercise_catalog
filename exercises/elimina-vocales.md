---
slug: elimina-vocales
difficulty: 3.0
tags: [strings, loops, filtering]
---
# Elimina vocales

Dada una frase, escribe la misma frase pero eliminando las vocales.

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
