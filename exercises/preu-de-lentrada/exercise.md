---
slug: preu-de-lentrada
tags: [if]
---
# Preu de l'entrada

![image](1569595180-4a4864113f-ws9pryrtwvt7uqgpzdbo.png)
Un web de venta de tickets per a espectacles calcula el preu d'una entrada a partir d'una sèrie de dades:

- **L'edat de la persona**: si la persona és menor de 6 anys, l'entrada és gratuita. Si és menor de 18 anys, se li aplica un descompte del 10%. I si la persona té 65 anys o més se li aplica un descompte del 15%.
- **El dia de la setmana**: si l'entrada és per al dimecres (dia de l'espectador) se li aplica un 25% de descompte. En canvi si és per a dissabte o diumenge, el preu s'apuja un 5%.
- **Cupó de descompte**: si el comprador té un cupó de descompte, se li aplica un 30% de descompte.

El descompte per edat i cupó són mútuament exclusius. És a dir, si s'aplica el tíquet descompte no es pot aplicar el descompte per edat.

## Input

L'entrada consta de 4 dades.

- La primera dada P és un nombre flotant que indica el preu base del ticket.
- La segona dada E és un enter que indica l'edat del comprador.
- La tercera dada D és un enter que indica el dia de la setmana (1=dilluns, 2=dimarts, 3=dimecres, ...)
- L'ultima dada C és un booleà que indica si el comprador té cupó.

## Output

S'imprimirà el preu final de l'entrada amb 2 xifres decimals.

## Tests

### Test
```input
10 25 1 false
```
```output
10.00
```
```explanation
Preu base=10

Edad=25. No se li aplica descompte

Dia=Dilluns. No se li aplica descompte

Cupó=false. No se li aplica descompte
```

### Test
```input
10 25 1 false
```
```output
10.00
```
```explanation
Al ser menor de 6 anys, el tícket és gratuït
```

### Test
```input
10 3 1 false
```
```output
0.00
```
```explanation
Al ser major de 65 anys, se li aplica un 15% de descompte.
```

### Test
```input
10 70 4 false
```
```output
8.50
```
```explanation
Se li aplica un 25% per ser Dimecres, i un 30% pel cupó de descompte.
```

### Test
```input
10 25 3 true
```
```output
4.50
```
```explanation
Se li aplica el 30% pel cupó de descompte, però no el 10% (menor 18 anys).
```

### Test
```input
10 13 4 true
```
```output
7.00
```
```explanation
Se li aplica el 10% per ser menor de 18 anys.
```

### Test
```input
10 13 2 false
```
```output
9.00
```
```explanation
S'incrementa el preu un 5% per ser dissabte.
```

### Test
```input
10 25 6 false
```
```output
10.50
```
```explanation
S'incrementa el preu un 5% per ser diumenge.
```

### Test
```input
10 25 7 false
```
```output
10.50
```
```explanation
Descompte del 10% per ser menor de 18, i increment del 5% per ser dissabte.
```

### Test
```input
10 12 6 false
```
```output
9.50
```
```explanation
Descompte per del 30% per cupó. No se li aplica el de edad. Increment del 5% per diumenge.
```

### Test
```input
10 12 7 true
```
```output
7.50
```
```explanation
Descompte del 15% per tenir 65 anys i del 25% per ser dimecres.
```

### Test
```input
10 65 3 false
```
```output
6.00
```

### Test private
```input
10 65 3 true
```
```output
4.50
```
