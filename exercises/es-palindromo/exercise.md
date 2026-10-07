---
slug: es-palindromo
tags: [strings]
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
