---
slug: c1-l2-2-secret-handshake
---
# Secret Handshake

Hi ha 10 tipus de persones al món: *els que entenen el binari i els que no*.

Vosaltres i els vostres companys de cohort dels que "sabeu" quan es tracta d’un binari decidiu crear una "salutació" secreta.

```text
1 = fer l'ullet
10 = doble parpalleig
100 = tancar el ulls
1000 = saltar
```

## Input

La entrada consisteix en una seqüència de 4 bits, separats per espais.

4 bits

## Output

S'escriurà la seqüència d'events de la "salutació" secreta

## Tests

### Test 11.11
```input
1 0 0 0
```
```output
saltar
```

### Test 11.11
```input
1 0 0 0
```
```output
saltar
```

### Test private 11.11
```input
1 0 0 1
```
```output
tancar els ulls
fer l'ullet
```

### Test private 11.11
```input
1 0 1 0
```
```output
doble parpalleig
doble parpalleig
```

### Test private 11.11
```input
1 0 1 1
```
```output
doble parpalleig
fer l'ullet
fer l'ullet
```

### Test private 11.11
```input
1 1 0 0
```
```output
fer l'ullet
tancar els ulls
```

### Test private 11.11
```input
1 1 0 1
```
```output
fer l'ullet
doble parpalleig
fer l'ullet
```

### Test private 11.11
```input
1 1 1 0
```
```output
fer l'ullet
fer l'ullet
doble parpalleig
```

### Test private 11.12
```input
1 1 1 1
```
```output
fer l'ullet
fer l'ullet
fer l'ullet
fer l'ullet
```
