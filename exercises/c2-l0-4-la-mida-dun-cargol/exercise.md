---
slug: c2-l0-4-la-mida-dun-cargol
---
# La mida d'un cargol

![image](1576672258-b20fcd32e4-cargol.jpg)
Crea un programa que a partir de la mida d'un cargol, mostri el text corresponent a la mida, segons la taula següent:

- D’1 cm (inclòs) a 3 cm (no inclòs): petit

- De 3 cm (inclòs) a 5 cm (no inclòs): mitjà

- De 5 cm (inclòs) a 8 cm (no inclòs): gran

- De 8 cm (inclòs) a 10 cm (inclòs): molt gran

- Qualsevol altre valor indica que la mida del cargol és incorrecta.

## Input

La mida del cargol en centímetres (int).

## Output

{ petit | mitja | gran | molt gran | mida incorrecta }

## Tests

### Test 7.14
```input
1
```
```output
petit
```

### Test 7.14
```input
2
```
```output
petit
```

### Test private 7.14
```input
3
```
```output
mitja
```

### Test private 7.14
```input
4
```
```output
mitja
```

### Test private 7.14
```input
5
```
```output
gran
```

### Test private 7.14
```input
6
```
```output
gran
```

### Test private 7.14
```input
7
```
```output
gran
```

### Test private 7.14
```input
8
```
```output
molt gran
```

### Test private 7.14
```input
9
```
```output
molt gran
```

### Test private 7.14
```input
10
```
```output
molt gran
```

### Test private 7.14
```input
11
```
```output
mida incorrecta
```

### Test private 7.14
```input
12
```
```output
mida incorrecta
```

### Test private 7.14
```input
13
```
```output
mida incorrecta
```

### Test private 7.18
```input
14
```
```output
mida incorrecta
```
