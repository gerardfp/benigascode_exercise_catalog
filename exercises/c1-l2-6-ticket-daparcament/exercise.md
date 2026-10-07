---
slug: c1-l2-6-ticket-daparcament
tags: [operadors]
---
# Ticket d'aparcament

![image](1556180294-d84162eb53-Untitleddrawing1.png)

Un ticket d'aparcament et permet aparcar durant un temps en funció dels diners que hi posis i de la tarifa.

Quan s'imprimeix el ticket, s'indica l'hora d'inici de l'aparcament, i l'hora de finalització (calculada a partir dels diners i de la tarifa).

## Input

- un nombre enter indica l'hora d'inici (hores, minuts i segons),
- un nombre float indica la quantitat de diners introduits,
- un nombre float indica la tarifa.

Els diners s'indiquen en Euros.

La tarifa s'indica en Minuts/Euros.

## Output

S'imprimirà l'hora de finalització en format H:M:S

## Tests

### Test
```input
0 0 0
0
0
```
```output
0:0:0
```
```explanation
L'hora d'inici és 0:0:0

La tarifa són 60 minuts per euro

S'ha introduit 1 euro

Per tant s'obté una hora d'aparcament
```

### Test
```input
0 0 0
60
1
```
```output
1:0:0
```
```explanation
L'hora d'inici és 10:0:0
La tarifa són 30 minuts per euro
S'ha introduit 1 euro

Per tant es tenen 30 minuts d'aparcament
```

### Test
```input
10 0 0
30
1
```
```output
10:30:0
```
```explanation
La tarifa és 1 minut per euro
S'ha introduit 0.5 euros

El temps d'aparcament són 30 segons
```

### Test
```input
10 15 0
1
0.5
```
```output
10:15:30
```
```explanation
La tarifa és 0.5 minuts per euro (30 segons per euro)
S'han introduït 0.5 euros
El temps són 15 segons
```

### Test
```input
16 0 0
0.5
0.5
```
```output
16:0:15
```

### Test
```input
16 45 0
30
1
```
```output
17:15:0
```

### Test
```input
16 30 45
0.5
1
```
```output
16:31:15
```

### Test
```input
16 30 45
1.5
40
```
```output
17:30:45
```

### Test
```input
8 30 45
30
20.75
```
```output
18:53:15
```

### Test private
```input
6 17 59
20.5
13.15
```
```output
10:47:33
```
