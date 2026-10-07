---
slug: precision-mecanografica
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
```explanation
Si en un texto de **100** caracteres se han cometido **10** errores y se ha tardado **60** segundos, el resultado de la prueba es:

Precisión: **90**%

Velocidad: **20** PPM
```

### Test
```input
10 3 60
```
```output
70
2
```
```explanation
Si en un texto de **10** caracteres se han cometido **3** errores y se ha tardado **60** segundos, el resultado de la prueba es:

Precisión: **70**%

Velocidad: **2** PPM
```

### Test
```input
60 0 10
```
```output
100
72
```
```explanation
Si en un texto de **60** caracteres se han cometido **0** errores y se ha tardado **10** segundos, el resultado de la prueba es:

Precisión: **100**%

Velocidad: **72** PPM
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

### Test private
```input
1 1 1
```
```output
0
12
```
