---
slug: vocales-mayusculas
difficulty: 4.0
tags: [strings, loops]
---
# Vocales Mayúsculas

Dado un texto (con varios saltos de línea), cambia las vocales en minúscula a mayúscula.

## Input

Un texto con varios saltos de línea.
El texto termina con la palabra END (que no debe procesarse)

## Output

El mismo texto con las vocales en mayúscula.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNextLine()) {
        String line = sc.nextLine();
        if (line.equals("END")) {
            break;
        }
        String res = "";
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if (c == 'a') res += 'A';
            else if (c == 'e') res += 'E';
            else if (c == 'i') res += 'I';
            else if (c == 'o') res += 'O';
            else if (c == 'u') res += 'U';
            else res += c;
        }
        IO.println(res);
    }
}
```

## Tests

### Test
```input
hola mundo!
END
```
```output
hOlA mUndO!
```

### Test
```input
aae io uu
ae, iii.
OU
END
```
```output
AAE IO UU
AE, III.
OU
```

### Test
```input
lorem ipsum dolor sit amet,
consectetur adipiscing elit.
Aliquam ut iaculis enim,
sit amet tempor massa.
END
```
```output
lOrEm IpsUm dOlOr sIt AmEt,
cOnsEctEtUr AdIpIscIng ElIt.
AlIqUAm Ut IAcUlIs EnIm,
sIt AmEt tEmpOr mAssA.
```

### Test private
```input
a
END
```
```output
A
```
