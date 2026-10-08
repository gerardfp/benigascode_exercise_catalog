---
slug: precision-mecanografica
tags: [scanner, i/o]
---
# Precisión mecanográfica

En unas pruebas de mecanografía se pide teclear un texto y se mide la precisión y la velocidad:

- La PRECISIÓN se mide en **Porcentaje** entre el número de caracteres del texto y el número de errores cometidos.

- La VELOCIDAD se mide en **Palabras Por Minuto** (se considera que **una palabra son 5 caracteres -sin importar si son letras, signos o espacios-**).

Dados los datos de una prueba, determina la precisión y la velocidad.

Los datos de una prueba consisten en el número de caracteres del texto, el número de errores cometidos y el tiempo empleado **(en segundos)**.

## Input

La entrada consta de tres números:

L: número de caracteres del texto

E: número de errores cometidos

T: tiempo empleado (en segundos)

1 <= L <= 1000

0 <= E <= L

1 <= T <= 1000

## Output

Se debe imprimir la Precisión (porcentaje de aciertos) y la Velocidad (palabras por minuto), cada uno en una línea, y sin decimales.

## Tests

### Test
```input
100 10 60
```
```output
90
20
```

### Test
```input
10 3 60
```
```output
70
2
```

### Test
```input
60 0 10
```
```output
100
72
```

### Test
```input
300 37 65
```
```output
87
55
```

### Test
```input
789 7 165
```
```output
99
57
```

### Test
```input
60 60 6
```
```output
0
120
```

### Test
```input
1 1 1
```
```output
0
12
```
