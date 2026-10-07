---
slug: c2-l3-1-contenidors
---
# Contenidors

Els contenidors són entorns d'execució aïllats que només tenen accés als recursos (cpu, memòria, sistema d'arxius, xarxa, etc.) que li són assignats.

Existeixen moltes solucions de software que permeten el maneig de contenidors (crear, iniciar, parar, eliminar...).

Una forma habitual de gestionar els contenidors és a través de comandaments. Per exemple, el comandament START inicia un contenidor, i STOP l'atura. És clar, que un contenidor ha d'estar un estat adequat per a poder enviar-li un comandament. Per exemple, no es pot aturar un contenidor que no estigui en execució.

El següent diagrama ilustra els estats en els que pot estar un contenidor, i els comandaments que es poden executar sobre ell, canviant el seu estat.

![image](1557270926-18375a3fbe-statemachine1.png)

Es requereix crear un programa per a gestionar els estats d'un contenidor a través de comandaments.

## Input

La entrada consisteix en un estat i un comandament.

Un contenidor que encara no existeix s'indica amb l'estat '_'

estat = { _ | CREATED | RUNNING | PAUSED | STOPPED }

comandament = { CREATE | START | PAUSE | UNPAUSE | STOP | RM }

## Output

S'indicarà l'estat en que ha de quedar el contenidor si el comandament es pot realitzar.
Si no es pot realitzar, s'indicarà amb el missatge d'error "Invalid command  for state "

## Tests

### Test 3.23
```input
_  CREATE
```
```output
CREATED
```

### Test 3.23
```input
_  CREATE
```
```output
CREATED
```

### Test private 3.23
```input
_  START
```
```output
Invalid command START for state _
```

### Test private 3.23
```input
_  PAUSE
```
```output
Invalid command PAUSE for state _
```

### Test private 3.23
```input
_  UNPAUSE
```
```output
Invalid command UNPAUSE for state _
```

### Test private 3.23
```input
_  STOP
```
```output
Invalid command STOP for state _
```

### Test private 3.23
```input
_  RM
```
```output
Invalid command RM for state _
```

### Test private 3.23
```input
CREATED  CREATE
```
```output
Invalid command CREATE for state CREATED
```

### Test private 3.23
```input
CREATED  START
```
```output
RUNNING
```

### Test private 3.23
```input
CREATED  PAUSE
```
```output
Invalid command PAUSE for state CREATED
```

### Test private 3.23
```input
CREATED  UNPAUSE
```
```output
Invalid command UNPAUSE for state CREATED
```

### Test private 3.23
```input
CREATED  STOP
```
```output
Invalid command STOP for state CREATED
```

### Test private 3.23
```input
CREATED  RM
```
```output
DELETED
```

### Test private 3.23
```input
RUNNING  CREATE
```
```output
Invalid command CREATE for state RUNNING
```

### Test private 3.23
```input
RUNNING  START
```
```output
Invalid command START for state RUNNING
```

### Test private 3.23
```input
RUNNING  PAUSE
```
```output
PAUSED
```

### Test private 3.23
```input
RUNNING  UNPAUSE
```
```output
Invalid command UNPAUSE for state RUNNING
```

### Test private 3.23
```input
RUNNING  STOP
```
```output
STOPPED
```

### Test private 3.23
```input
RUNNING  RM
```
```output
Invalid command RM for state RUNNING
```

### Test private 3.23
```input
PAUSED  CREATE
```
```output
Invalid command CREATE for state PAUSED
```

### Test private 3.23
```input
PAUSED  START
```
```output
Invalid command START for state PAUSED
```

### Test private 3.23
```input
PAUSED  PAUSE
```
```output
Invalid command PAUSE for state PAUSED
```

### Test private 3.23
```input
PAUSED  UNPAUSE
```
```output
RUNNING
```

### Test private 3.23
```input
PAUSED  STOP
```
```output
Invalid command STOP for state PAUSED
```

### Test private 3.23
```input
PAUSED  RM
```
```output
Invalid command RM for state PAUSED
```

### Test private 3.23
```input
STOPPED  CREATE
```
```output
Invalid command CREATE for state STOPPED
```

### Test private 3.23
```input
STOPPED  START
```
```output
RUNNING
```

### Test private 3.23
```input
STOPPED  PAUSE
```
```output
Invalid command PAUSE for state STOPPED
```

### Test private 3.23
```input
STOPPED  UNPAUSE
```
```output
Invalid command UNPAUSE for state STOPPED
```

### Test private 3.23
```input
STOPPED  STOP
```
```output
Invalid command STOP for state STOPPED
```

### Test private 3.1
```input
STOPPED  RM
```
```output
DELETED
```
