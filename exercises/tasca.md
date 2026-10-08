---
slug: tasca
---
# Tasca

![image](assets/tasca-img0.png)

A la plataforma d'aprenentatge que estem desenvolupant, els alumnes han de poder realitzar trameses dels seus treballs. Aquestes trameses han de tenir una hora límit.
Als alumnes que realitzin la tramesa un cop superada aquesta hora límit, la plataforma els informarà del temps excedit.

Donades les hores de les trameses i l'hora límit, digues quan de temps s'ha excedit cada tramesa.

## Input

El primer número  indica la quantitat de trameses.

Per a cada tramesa s'indica: `hora minut segon`

Per últim s'indica l'hora límit: `hora minut segon`

Totes les hores són vàlides

## Output

S'imprimirà `ok` per a aquelles trameses que s'han fet dintre del temps límit.

Les trameses fora de temps s'escriurà: `S'ha excedit 0h 0m 0s` (canviant el `0` pel valor corresponent)

## Plantillas

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
      	
      	
    }
}
```

## Tests

### Test
```input
3
12 45 0
10 34 7
9 55 46

10 0 0
```
```output
S'ha excedit 2h 45m 0s
S'ha excedit 0h 34m 7s
ok
```

### Test
```input
6
11 0 0
10 1 0
10 0 1
9 0 0
9 59 0
9 59 59 

10 0 0
```
```output
S'ha excedit 1h 0m 0s
S'ha excedit 0h 1m 0s
S'ha excedit 0h 0m 1s
ok
ok
ok
```

### Test
```input
5
14 55 23
23 59 59
0 0 0
0 0 1
18 0 1

12 0 0
```
```output
S'ha excedit 2h 55m 23s
S'ha excedit 11h 59m 59s
ok
ok
S'ha excedit 6h 0m 1s
```

### Test
```input
2
23 59 59
0 0 0

23 59 59
```
```output
ok
ok
```

### Test
```input
4
10 16 5
10 20 5
11 15 25
13 15 25

10 15 30
```
```output
S'ha excedit 0h 0m 35s
S'ha excedit 0h 4m 35s
S'ha excedit 0h 59m 55s
S'ha excedit 2h 59m 55s
```
