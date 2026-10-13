---
slug: c3-l0-5-compta-vocals
tags: [for]
---
# Filtra vocals

Donada una llista de lletres, imprimeix únicament les vocals que hi hagi.

## Input

L'entrada consta de dues parts:

- Primer s'indica la quantitat de lletres
- A continuació venen les lletres, en minúscules i separades per espais en blanc

## Output

S'imprimirà cada vocal en una línia

## Tests

### Test
```input
3
a b c
```
```output
a
```

### Test
```input
3
a b c
```
```output
a
```

### Test
```input
5
a b c d e
```
```output
a
e
```

### Test
```input
5
a x e x a
```
```output
a
e
a
```

### Test
```input
10
i j u k i l l o m a
```
```output
i
u
i
o
a
```

### Test
```input
20
a e t h v u i e a o c x u i a o e u l o
```
```output
a
e
u
i
e
a
o
u
i
a
o
e
u
o
```

### Test
```input
1
a
```
```output
a
```

### Test
```input
5
a e i o u
```
```output
a
e
i
o
u
```

### Test private
```input
5
x u v z i
```
```output
u
i
```
