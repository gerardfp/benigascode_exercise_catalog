---
slug: c1-l1-7-temps-de-descarrega
tags: [operadors]
---
# Temps de descàrrega

![image](c1-l1-7-temps-de-descarrega-img0.png)

S'està realitzant un programa per a gestionar descàrregues d'arxius.
Aquest programa ha de mostrar a l'usuari el temps estimat que trigarà la descàrrega, en funció de la velocitat i el tamany de l'arxiu.

## Input

El primer nombre  indica la velocitat de descàrrega (en KB per segon).

El segon nombre  indica el tamany de l'arxiu (en MB).

> Cal tenir en compte que 1MB = 1024 KB

## Output

Els segons que trigarà la descàrrega (sense decimals).

## Tests

### Test
```input
1 1
```
```output
1024
```

### Test
```input
1 2
```
```output
2048
```

### Test
```input
1024 1
```
```output
1
```

### Test
```input
512 10
```
```output
20
```

### Test
```input
4096 1024
```
```output
256
```
