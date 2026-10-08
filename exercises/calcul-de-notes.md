---
slug: calcul-de-notes
tags: [matemáticas, algorithms]
---
# Càlcul de notes

Donada una entrada de teclat corresponent a la marca numèrica d'un examen, el programa imprimirà la qualificació textual corresponent:

- Menys de 5: INSUFICIENT

- 5 a 6 (no inclòs): SUFICIENT

- 6 a 7 (no inclòs): BE

- 7 a 8.5 (no inclòs): NOTABLE

- 8.5 a 10 (no inclòs): EXCEL.LENT

- 10: MATRICULA

## Input

Un número flotant corresponent a la nota

## Output

{ INSUFICIENT | SUFICIENT | BE | NOTABLE | EXCEL.LENT | MATRICULA }

## Tests

### Test
```input
0
```
```output
INSUFICIENT
```

### Test
```input
4
```
```output
INSUFICIENT
```

### Test
```input
4.5
```
```output
INSUFICIENT
```

### Test
```input
4.999
```
```output
INSUFICIENT
```

### Test
```input
5
```
```output
SUFICIENT
```

### Test
```input
5.999
```
```output
SUFICIENT
```

### Test
```input
6
```
```output
BE
```

### Test
```input
6.999
```
```output
BE
```

### Test
```input
7
```
```output
NOTABLE
```

### Test
```input
8.499
```
```output
NOTABLE
```

### Test
```input
8.5
```
```output
EXCEL.LENT
```

### Test
```input
9.255
```
```output
EXCEL.LENT
```

### Test
```input
9.999
```
```output
EXCEL.LENT
```

### Test
```input
10
```
```output
MATRICULA
```
