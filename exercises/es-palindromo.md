---
slug: es-palindromo
difficulty: 4.0
tags: [strings, flags]
---
# Comprobador de Palíndromos

## Enunciado
Escribe un programa lea una línea de texto y determine si es un **palíndromo** (un texto que se lee igual de izquierda a derecha que de derecha a izquierda).

Para verificar si es palíndromo:
1. Se deben ignorar los espacios en blanco.
2. Se debe ignorar si las letras están en mayúsculas o minúsculas.

## Input
Una línea de texto

## Output
`SI` o `NO`

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextLine()) return;
    String line = sc.nextLine();
    String cleaned = line.replace(" ", "").toLowerCase();
    boolean isPal = true;
    int len = cleaned.length();
    for (int i = 0; i < len / 2; i++) {
        if (cleaned.charAt(i) != cleaned.charAt(len - 1 - i)) {
            isPal = false;
            break;
        }
    }
    IO.println(isPal ? "SI" : "NO");
}
```

## Tests

### Test
```input
radar
```
```output
SI
```

### Test
```input
java
```
```output
NO
```

### Test
```input
Anita lava la tina
```
```output
SI
```

### Test
```input
benigascode plataforma educativa
```
```output
NO
```
