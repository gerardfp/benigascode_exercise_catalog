---
slug: robot-simulator
---
# Robot simulator

Un robot pot moure's en una quadrícula en direcció , , , .

En un primer moment el robot es situa en la posició {,} de la quadrícula. Després, el robot rep una sèrie d'instruccions de moviment. El simulador ha d'indicar la posició final {,} en la que quedaria el robot després de realitzar els moviments.

Les instruccions de moviment són un String amb les direccions en les que s'ha de moure. Un punt indica el fi de les instruccions.
Per exemple:

```text
N N E E S E S W .
```

![image](1547568352-2ceaa63457-robot.png)

Posició final: {2,0}

Exemple 2:

```text
N E E N .
```

![image](1547570008-85507a4a19-robot1.png)

Posició final: {2,2}

## Input

Un String amb les instruccions `N`, `S`, `E`, `W`, `.`

## Output

Dos enters indicant la posició final separats per un salt de línia.
Primer la posició , i després la posició .

## Tests

### Test 12.5
```input
N N N .
```
```output
0
3
```

### Test 12.5
```input
N E E .
```
```output
2
1
```

### Test private 12.5
```input
N N S S .
```
```output
0
0
```

### Test private 12.5
```input
N E .
```
```output
1
1
```

### Test private 12.5
```input
S W N N E E .
```
```output
1
1
```

### Test private 12.5
```input
S N W W E N S E N N E S .
```
```output
1
1
```

### Test private 12.5
```input
S S W W W .
```
```output
-3
-2
```

### Test private 12.5
```input
N .
```
```output
0
1
```
