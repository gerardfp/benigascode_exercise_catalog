---
slug: c1-l3-5-data-de-part
tags: [condicionales, control-de-flujo]
---
# Data de caducitat

Estem desenvolupant una aplicació per a dispositius mòbils que ajudi al consumidor a escollir els productes que compra al supermercat. L'usuari escaneja amb la càmera l'etiqueta d'un producte i l'aplicació li dona informació d'aquest producte.

Una de les opcions de l'aplicació és advertir a l'usuari dels productes que han superat la data de caducitat.

## Input

La entrada consta de 6 nombres corresponents a la data de caducitat i la data actual en format dd/mm/yyyy.

## Output

S'imprimirà  si el producte està caducat, o  si no ho està.

## Tests

### Test 11.11
```input
 1 1 2020
 1 1 2020
```
```output
false
```

### Test 11.11
```input
1 1 2030
1 1 2020
```
```output
false
```

### Test private 11.11
```input
1 2 2020
1 1 2020
```
```output
false
```

### Test private 11.11
```input
2 1 2020
1 1 2020
```
```output
false
```

### Test private 11.11
```input
1 1 2020
2 1 2020
```
```output
true
```

### Test private 11.11
```input
1 1 2020
1 2 2020
```
```output
true
```

### Test private 11.11
```input
1 1 2020
1 1 2030
```
```output
true
```

### Test private 11.11
```input
2 2 2020
1 1 2030
```
```output
true
```

### Test private 11.12
```input
1 1 2030
2 2 2020
```
```output
false
```
