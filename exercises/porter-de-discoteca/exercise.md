---
slug: porter-de-discoteca
---
# Porter de discoteca

Algunes discoteques tenen unes normes d'accés extranyes. Aquesta en concret té les següents:

- Si ets menor d'edad no pots entrar

- Els homes no poden portar arracades

- S'ha d'anar ben vestit

- Els que tenen la tarjeta VIP poden entrar, sense tenir en compte aquestes normes.

Es desitja implementar un sistema de control d'accés automàtic a la discoteca que autoritzi l'accès en base a aquestes regles. (*Un sistema basat en el reconeixement d'imatges i NFC proporciona les dades d'entrada*).

## Input

L'entrada consta de 5 dades:

- Un nombre enter indica l'edat

- El sexe s'indica amb {home|dona}

- Un booleà indica si porta arracades

- Un booleà indica si va ben vestit

- Un booleà indica si té tarjeta VIP

No hi ha

## Output

S'imprimirà "ENTRA" si el sistema autoritza l'accés i "NO ENTRA" en cas contrari.

## Tests

### Test 2.04
```input
17 home true true true
```
```output
ENTRA
```

### Test 2.04
```input
17 home true true true
```
```output
ENTRA
```

### Test private 2.04
```input
17 home true true false
```
```output
NO ENTRA
```

### Test private 2.04
```input
17 home true false true
```
```output
ENTRA
```

### Test private 2.04
```input
17 home true false false
```
```output
NO ENTRA
```

### Test private 2.04
```input
17 home false true true
```
```output
ENTRA
```

### Test private 2.04
```input
17 home false true false
```
```output
NO ENTRA
```

### Test private 2.04
```input
17 home false false true
```
```output
ENTRA
```

### Test private 2.04
```input
17 home false false false
```
```output
NO ENTRA
```

### Test private 2.04
```input
17 dona true true true
```
```output
ENTRA
```

### Test private 2.04
```input
17 dona true true false
```
```output
NO ENTRA
```

### Test private 2.04
```input
17 dona true false true
```
```output
ENTRA
```

### Test private 2.04
```input
17 dona true false false
```
```output
NO ENTRA
```

### Test private 2.04
```input
17 dona false true true
```
```output
ENTRA
```

### Test private 2.04
```input
17 dona false true false
```
```output
NO ENTRA
```

### Test private 2.04
```input
17 dona false false true
```
```output
ENTRA
```

### Test private 2.04
```input
17 dona false false false
```
```output
NO ENTRA
```

### Test private 2.04
```input
18 home true true true
```
```output
ENTRA
```

### Test private 2.04
```input
18 home true true false
```
```output
NO ENTRA
```

### Test private 2.04
```input
18 home true false true
```
```output
ENTRA
```

### Test private 2.04
```input
18 home true false false
```
```output
NO ENTRA
```

### Test private 2.04
```input
18 home false true true
```
```output
ENTRA
```

### Test private 2.04
```input
18 home false true false
```
```output
ENTRA
```

### Test private 2.04
```input
18 home false false true
```
```output
ENTRA
```

### Test private 2.04
```input
18 home false false false
```
```output
NO ENTRA
```

### Test private 2.04
```input
18 dona true true true
```
```output
ENTRA
```

### Test private 2.04
```input
18 dona true true false
```
```output
ENTRA
```

### Test private 2.04
```input
18 dona true false true
```
```output
ENTRA
```

### Test private 2.04
```input
18 dona true false false
```
```output
NO ENTRA
```

### Test private 2.04
```input
18 dona false true true
```
```output
ENTRA
```

### Test private 2.04
```input
18 dona false true false
```
```output
ENTRA
```

### Test private 2.04
```input
18 dona false false true
```
```output
ENTRA
```

### Test private 2.04
```input
18 dona false false false
```
```output
NO ENTRA
```

### Test private 2.04
```input
19 home true true true
```
```output
ENTRA
```

### Test private 2.04
```input
19 home true true false
```
```output
NO ENTRA
```

### Test private 2.04
```input
19 home true false true
```
```output
ENTRA
```

### Test private 2.04
```input
19 home true false false
```
```output
NO ENTRA
```

### Test private 2.04
```input
19 home false true true
```
```output
ENTRA
```

### Test private 2.04
```input
19 home false true false
```
```output
ENTRA
```

### Test private 2.04
```input
19 home false false true
```
```output
ENTRA
```

### Test private 2.04
```input
19 home false false false
```
```output
NO ENTRA
```

### Test private 2.04
```input
19 dona true true true
```
```output
ENTRA
```

### Test private 2.04
```input
19 dona true true false
```
```output
ENTRA
```

### Test private 2.04
```input
19 dona true false true
```
```output
ENTRA
```

### Test private 2.04
```input
19 dona true false false
```
```output
NO ENTRA
```

### Test private 2.04
```input
19 dona false true true
```
```output
ENTRA
```

### Test private 2.04
```input
19 dona false true false
```
```output
ENTRA
```

### Test private 2.04
```input
19 dona false false true
```
```output
ENTRA
```

### Test private 2.08
```input
19 dona false false false
```
```output
NO ENTRA
```
