---
slug: vocales-mayusculas
---
# Vocales Mayúsculas

Dado un texto (con varios saltos de línea), cambia las vocales en minúscula a mayúscula.

## Input

Un texto con varios saltos de línea.
El texto termina con la palabra END (que no debe procesarse)

1 <= L <= 100

## Output

El mismo texto con las vocales en mayúscula.

## Tests

### Test 25
```input
hola mundo!
END
```
```output
hOlA mUndO!
```

### Test 25
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

### Test private 25
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

### Test private 25
```input
a
END
```
```output
A
```
