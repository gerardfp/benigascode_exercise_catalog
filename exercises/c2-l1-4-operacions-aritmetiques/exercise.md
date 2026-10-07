---
slug: c2-l1-4-operacions-aritmetiques
tags: [scanner, i/o]
---
# Expressions aritmètiques

Implementa un intèrpret d'expressions aritmètiques.

Els operadors que ha d'implementar són:

```text
+    Addició
-    Subtracció
*    Multiplicació
/    Divisió
%    Residu
```

## Input

La entrada consisteix en el primer operand , l'operador , i el segon operand , separats per espais en blanc.

-100 <=  <= 100

-100 <=  <= 100

 i  són nombres decimals.

## Output

El resultat de la operació (float), o els missatges `Error: division by zero` i `Error: operation not permitted` en el seu cas.

## Tests

### Test 11.11
```input
1 + 1
```
```output
2.0
```

### Test 11.11
```input
1 + 1
```
```output
2.0
```

### Test private 11.11
```input
1 - 1
```
```output
0.0
```

### Test private 11.11
```input
100 * 100
```
```output
10000.0
```

### Test private 11.11
```input
5 / 10
```
```output
0.5
```

### Test private 11.11
```input
10 % 0.5
```
```output
0.0
```

### Test private 11.11
```input
10 / 0
```
```output
Error: division by zero
```

### Test private 11.11
```input
7 & 3
```
```output
Error: operation not permitted
```

### Test private 11.12
```input
27 % 0
```
```output
Error: division by zero
```
