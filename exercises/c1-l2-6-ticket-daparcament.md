---
slug: c1-l2-6-ticket-daparcament
tags: [operadors]
---
# Ticket d'aparcament

![image](assets/c1-l2-6-ticket-daparcament-img0.png)

Un ticket d'aparcament et permet aparcar durant un temps en funció dels diners que poses i de la tarifa.

Quan s'imprimix el ticket, s'indica l'hora d'inici de l'aparcament, i l'hora de finalització (calculada a partir dels diners i de la tarifa).

## Input

- Tres enters indiquen l'hora d'inici (hores, minuts i segons),

- Un decimal indica la quantitat de diners introduits,

- Un decimal indica la tarifa (Minuts/Euros)

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

### Test
```input
0 0 0
60
1
```
```output
1:0:0
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

### Test
```input
10 15 0
1
0.5
```
```output
10:15:30
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

### Test
```input
6 17 59
20.5
13.15
```
```output
10:47:33
```
