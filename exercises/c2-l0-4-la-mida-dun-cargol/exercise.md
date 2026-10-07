---
slug: c2-l0-4-la-mida-dun-cargol
tags: [if]
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

### Test
```input
1
```
```output
petit
```

### Test
```input
2
```
```output
petit
```

### Test
```input
3
```
```output
mitja
```

### Test
```input
4
```
```output
mitja
```

### Test
```input
5
```
```output
gran
```

### Test
```input
6
```
```output
gran
```

### Test
```input
7
```
```output
gran
```

### Test
```input
8
```
```output
molt gran
```

### Test
```input
9
```
```output
molt gran
```

### Test
```input
10
```
```output
molt gran
```

### Test
```input
11
```
```output
mida incorrecta
```

### Test
```input
12
```
```output
mida incorrecta
```

### Test
```input
13
```
```output
mida incorrecta
```

### Test private
```input
14
```
```output
mida incorrecta
```
