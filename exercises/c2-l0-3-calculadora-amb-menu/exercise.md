---
slug: c2-l0-3-calculadora-amb-menu
tags: [matemáticas, algorithms]
---
# Calculadora amb menú

Realitza un programa que soliciti dos nombres i mostri per pantalla el següent menú:

```text
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
```

L'usuari escullirà una opció i el programa finalitzarà mostrant el resultat per pantalla.

## Input

L'entrada consta de 3 nombres:

- Els dos primers  i  son els operands.

- El tercer nombre  és l'opció del menú seleccionada

Totes les operacions són enteres i no hi ha cap divisor que sigui 0.

## Output

S'imprimirà el resultat de l'operació

## Tests

### Test
```input
1 1     1
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2
```

### Test
```input
1 1     1
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2
```

### Test
```input
1 1     2
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
0
```

### Test
```input
1 1     3
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
1
```

### Test
```input
1 1     4
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
1
```

### Test
```input
2 2     1
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
4
```

### Test
```input
2 3     2
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
-1
```

### Test
```input
2 5     3
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
10
```

### Test
```input
10 5     4
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2
```

### Test
```input
3456 678     3
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2343168
```
