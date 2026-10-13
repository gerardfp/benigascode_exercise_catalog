---
slug: c2-l2-6-joc-de-pistes
---
# Joc de pistes

A les colònies de final de curs, una nit s'organitza un joc de pistes.

Es van deixant pistes que et porten a altres pistes fins arribar al premi final.

Farem un joc de pistes amb posicions d'un Array.

Per exemple:

```
String[] pistes = {"Ves a 2", "Ves a 4", "Ves a 1", "PREMI", "Ves a 3"}
```

Començant per pistes[0] seguiríem aquestes pistes:

"Ves a 2" -> "Ves a 1" -> "Ves a 4" -> "Ves a 3" -> "PREMI"

## Input

A la primera línia hi ha el nombre de pistes, la posició de la pista inicial, i un caràcter que serveix per a marcar la posició de les pistes.

A continuació venen les pistes, una en cada línia.

Dintre de cada pista, la posició de la següent pista està just a continuació del caràcter marcador.

La pista final té la paraula PREMI.

## Output

Es mostraran les pistes en l'ordre que s'han anat seguint fins arribar al premi.

## Tests

### Test
```input
5 0 #
Ves a #2
Ves a #4
Ves a #1
PREMI
Ves a #3
```
```output
Ves a #2
Ves a #1
Ves a #4
Ves a #3
PREMI
```

### Test
```input
5 0 #
Ves a #2
Ves a #4
Ves a #1
PREMI
Ves a #3
```
```output
Ves a #2
Ves a #1
Ves a #4
Ves a #3
PREMI
```

### Test
```input
5 0 {
A {2} trobaras el cami
Segueix buscant per {4}
Potser al {1} hi ha alguna cosa
PREMI
Prova al {3} a veure
```
```output
A {2} trobaras el cami
Potser al {1} hi ha alguna cosa
Segueix buscant per {4}
Prova al {3} a veure
PREMI
```

### Test
```input
4 2 $
Tebi $3
PREMI
Fred $0
Calent $1
```
```output
Fred $0
Tebi $3
Calent $1
PREMI
```

### Test private
```input
5 0 @
Aqui no @1
Aqui tampoc @2
No, no @3
Mmmmmm @4
PREMI
```
```output
Aqui no @1
Aqui tampoc @2
No, no @3
Mmmmmm @4
PREMI
```
