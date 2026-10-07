---
slug: c2-l3-1-permisos-unix
---
# Permisos UNIX

Els permisos de lecture, escritura i execució sobre fitxers en sistemes UNIX-like són gestionats en tres classes: usuari, grup i altres.

Els fitxers són propietat d'un usuari i d'un grup, i s'especifiquen permisos per a les tres classes: propietari del fitxer, els usuaris del grup propietari del fitxer i la resta d'usuaris.

![image](1557229688-38d8ac6b2b-permissions3.png)

Quan un usuari tracta d'accedir a un fitxer, els permisos efectius que té sobre el fitxer es determinen en base a la primera classe en la qual encaixi.

Donats els permisos, i l'usuari i grup propietaris d'un fitxer, calcula els permisos efectius que tindrà un usuari determinat sobre un fitxer.

## Input

A la primera línia venen els 9 permisos P, separats per espais en blanc, i l'usuari i grup propietaris.

A la segona línia ve l'usuari que tracta d'accedir al fitxer, i els 3 grups als que pertany.

P = { - | r | w | x }

L'usuari pertany sempre a 3 grups.

## Output

S'imprimiran els permisos efectius

## Tests

### Test 11.11
```input
r w x r - x r - - root root
alumne1 alumnes informatica dam
```
```output
r--
```

### Test 11.11
```input
r w x r - x r - - root root
alumne1 alumnes informatica dam
```
```output
r--
```

### Test private 11.11
```input
r w - r w - - - - root alumnes
alumne1 alumnes informatica asix
```
```output
rw-
```

### Test private 11.11
```input
r w x r - x r - - root root
alumne1 alumnes informatica dam
```
```output
r--
```

### Test private 11.11
```input
r w - r - - - - - alumne2 dam
alumne1 alumnes informatica asix
```
```output
---
```

### Test private 11.11
```input
r w x r w - r - - alumne3 asix
alumne2 alumnes informatica asix
```
```output
rw-
```

### Test private 11.11
```input
r w x r w - r - - alumne3 root
alumne3 root informatica asix
```
```output
rwx
```

### Test private 11.11
```input
r w x r w - r - - alumne3 root
alumne3 root informatica asix
```
```output
rwx
```

### Test private 11.12
```input
r w x r w x r - - root root
alumne3 root informatica asix
```
```output
rwx
```
