---
slug: c3-l0-6-code-analyzer
---
# Code analyzer

Donat un codi font en llenguatge Java, compta la quantitat de classes que hi ha definides.

## Input

L'entrada és un codi font en vàries línies.

La paraula  sempre va separada per espais en blanc de la resta del codi.

El codi acaba amb la paraula

## Output

S'imprimirà la quantitat de classes definides.

## Tests

### Test 12.5
```input
class A { int x; } END
```
```output
1
```

### Test 12.5
```input
class A { 
   int x; 
} 

END
```
```output
1
```

### Test private 12.5
```input
class Mktr {}

class Pkjy {}

END
```
```output
2
```

### Test private 12.5
```input
class Mktr {
   class Trws {}
}

class Pkjy {}

END
```
```output
3
```

### Test private 12.5
```input
class Mktr {}

abstract class Pkjy extends Mktr{
   int i;
   
   void xcvb();
}

END
```
```output
2
```

### Test private 12.5
```input
class Mktr {}

abstract class Pkjy extends Mktr{
   int i;

   void xcvb();

   class Swqz { class Ynvc {} }
}

END
```
```output
4
```

### Test private 12.5
```input
class A { class B {}}
END
```
```output
2
```

### Test private 12.5
```input
int i = 0;
END
```
```output
0
```
