---
slug: contractar-un-xef
tags: [scanner]
---
# Contractar un xef

Imagina que ets el cap de personal d'un restaurant i has de contractar un xef. Per fer-ho has de recollir algunes dades preliminars dels candidats.

Tens un formulari per a recollir les següents dades dels candidats: nom, edat, nivell d'estudis, anys d'experiència, i tipus de cuina.

El teu programa ha de llegir totes les paraules (o números) de les cinc línies de l'entrada i imprimir: "El formulari de `{nom}` s'ha completat. Et contactarem
si necessitem un xef de cuina `{tipus cuina}`."

## Input

L'entrada consta de 5 línies:

- A la primera línia hi ha el nom (String)
- A la segona línia hi ha l'edat (int)
- A la tercera línia hi ha el nivell d'estudis (String)
- A la quarta línia hi ha els anys (int)
- A la cinquena línia hi ha el tipus de cuina (String)

## Output

-

## Plantillas

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
      
    }
}
```

## Tests

### Test
```input
Joan
33
secundaria
4
tradicional
```
```output
El formulari de Joan s'ha completat. Et contactarem si necessitem un xef de cuina tradicional.
```

### Test
```input
Miquel
24
universitari
2
fussio
```
```output
El formulari de Miquel s'ha completat. Et contactarem si necessitem un xef de cuina fussio.
```

### Test
```input
Maria Elena
34
universitari
10
vanguardista
```
```output
El formulari de Maria Elena s'ha completat. Et contactarem si necessitem un xef de cuina vanguardista.
```

### Test private
```input
Josep Antoni
20
sense estudis
3
nouvelle cuisine
```
```output
El formulari de Josep Antoni s'ha completat. Et contactarem si necessitem un xef de cuina nouvelle cuisine.
```
