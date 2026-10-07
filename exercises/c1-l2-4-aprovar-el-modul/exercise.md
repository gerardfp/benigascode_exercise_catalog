---
slug: c1-l2-4-aprovar-el-modul
---
# Aprovar progrmació

Per a aprovar l'assignatura programació, un alumne ha d'aprovar els 3 Trimestres.

* Per a aprovar el T1, un alumne ha d'entregar com a mínim el 75% de les pràctiques i traure un com a mínim un 4 en l'examen. També pot aprovar el trimestre si entrega el 50% de les pràctiques i trau mínim un 5. I també aprova si trau més d'un 7 a l'examen (independentment de les practiques que haja entregat).

* Per a aprovar el T2, ha d'entregar com a mínim el 75% de les pràctiques i traure un com a mínim un 4 en l'examen. També pot aprovar si entrega totes les pràctiques o si entrega mínim el 50% de les pràctiques i trau com a mínim un 5 a l'examen.

* Per a aprovar el T3, un alumne ha d'entregar totes les pràctiques i traure un com a mínim un 5 en l'examen.

## Input

La entrada consisteix en 9 nombres.

Per a cada trimestre s'indica:

* El nombre de pràctiques que s'havien d'entregar
* El nombre de pràctiques que ha entregat
* La nota que ha tret a l'examen

## Output

S'imprimirà `true` si l'alumne aprova programació, o `false` si no l'aprova.

## Tests

### Test
```input
6 2 4
3 0 0
1 0 0
```
```output
false
```

### Test
```input
6 5 4
3 1 5
1 0 0
```
```output
false
```

### Test
```input
6 0 8
3 2 5
1 0 10
```
```output
false
```

### Test
```input
6 3 4
3 3 5
1 1 10
```
```output
false
```

### Test
```input
6 3 5
3 3 10
1 1 10
```
```output
true
```

### Test
```input
10 5 5
3 3 0
1 1 5
```
```output
true
```

### Test
```input
1 0 0
1 0 0
1 0 0
```
```output
false
```
