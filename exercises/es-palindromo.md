---
slug: es-palindromo
tags: [strings]
difficulty: 5
---
# Comprobador de Palíndromos

## Enunciado
Escribe un programa en Java que lea una línea de texto desde la entrada estándar y determine si es un **palíndromo** (un texto que se lee igual de izquierda a derecha que de derecha a izquierda).

Para verificar si es palíndromo:
1. Debes ignorar los espacios en blanco.
2. Debes ignorar si las letras están en mayúsculas o minúsculas (caso insensible).

Si el texto resultante es un palíndromo, el programa debe imprimir:
`SI`

En caso contrario, debe imprimir:
`NO`

## Formato de entrada
Una sola línea de texto leída desde la entrada estándar (`System.in`).

## Formato de salida
La cadena `SI` o `NO` en una única línea.

## Ejemplo 1
Entrada:
```text
radar
```
Salida:
```text
SI
```

## Ejemplo 2
Entrada:
```text
Anita lava la tina
```
Salida:
```text
SI
```

## Ejemplo 3
Entrada:
```text
java
```
Salida:
```text
NO
```

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
