---
slug: c1-l1-8-lliga-de-futbol
---
# Lliga de futbol

En la Lliga de futbol un equip rep 3 punts si guanya un partit, 1 punt si empata i 0 punts si perd.
L'equip A vol saber si està per davant a la classificació que l'equip B.

La classificació s'ordena segons els punts de cada equip, i en cas d'empat es mira la diferència entre els gols marcats i els gols rebuts.

## Input

Els primers 5 nombres son les dades de l'equip A.

Els següents 5 nombres les dades de l'equip B.

Las dades de cada equip són:

- El primer nombre  indica la quantitat de partits guanyats.

- El segon nombre  indica la quantitat de partitas empatats.

- El tercer nombre  indica la quantitat de partits perduts.

- El quart nombre  indica la quantitat de gols a favor.

- El cinquè nombre  indica la quantitat de gols en contra.

## Output

true - si l'equip A va per davant de l'equip B

false - si l'equip A va per darrere de l'equip B

## Tests

### Test 25
```input
1 0 0 0 0
0 0 0 0 0
```
```output
true
```

### Test 25
```input
3 0 0 6 0
0 1 2 0 8
```
```output
true
```

### Test private 25
```input
3 0 0 5 0
3 0 0 6 0
```
```output
false
```

### Test private 25
```input
5 0 10 20 2
0 15 0 25 8
```
```output
true
```
