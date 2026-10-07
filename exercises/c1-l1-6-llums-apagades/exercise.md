---
slug: c1-l1-6-llums-apagades
tags: [operadors, logics]
---
# Llums apagats

S'està realitzant una aplicació per a controlar els llums d'una casa.
L'aplicació ha de mostrar si tots els llums de la casa estan apagats.
En total hi ha 4 llums.

## Input

La entrada consta de 4 valors booleans que indiquen si cadascun dels llums està encés o apagat.

`true` => encés

`false` => apagat

## Output

S'ha d'imprimir `true` si tots els llums estan apagats, i `false` si hi ha algún llum encés.

## Tests

### Test
```input
false false false false
```
```output
true
```
```explanation
Tots els llums estan apagats
```

### Test
```input
false false false false
```
```output
true
```
```explanation
El primer llum està encés
```

### Test
```input
true false false false
```
```output
false
```
```explanation
L'últim llum està encés
```

### Test private
```input
false false false true
```
```output
false
```
