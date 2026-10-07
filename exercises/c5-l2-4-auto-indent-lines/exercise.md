---
slug: c5-l2-4-auto-indent-lines
---
# Auto-Indent Lines

Indentar -tabular, sagnar- és obligatori en Python. No obstant, és important fer-ho en tots els llenguatges, ja que ajuda a la comprensibilitat del codi.

Hi ha diferents estils d'indentació per als llenguatges que defineixen els blocs amb claus. La més comú és la K&R

- K&R

```
while (x == y) {
    something();
    somethingelse();
}
```

- Allman

```
while (x == y)
{
    something();
    somethingelse();
}
```

- GNU

```
while (x == y)
  {
    something ();
    somethingelse ();
  }
```

- Whitesmiths

```
while (x == y)
    {
    something();
    somethingelse();
    }
```

- Horstmann

```
while (x == y)
{   something();
    somethingelse();
}
```

- Pico

```
while (x == y)
{   something();
    somethingelse(); }
```

- Ratliff

```
while (x == y) {
    something();
    somethingelse();
    }
```

- Lisp

```
while (x == y)
  { something();
    somethingelse(); }
```

- Haskell

```
while (x == y)
  { something()
  ; somethingelse()
  ; 
  }
```

Amb els IDE tenim l'opció d'Auto-Indentar el codi. ¿Com ho fan?

## Input

La entrada és un codi escrit amb indentació K&R, però els espais d'indentació mal col·locats.
Tots els blocs del codi estan entre claus {}
El codi acaba amb la marca END.

## Output

S'escriurà el codi correctament indentat, estil K&R. El tamany d'indentació és 4 espais.

## Tests

### Test
```input
if(true){
   a=3;
      b=7;
}
END  
```
```output
if(true){
    a=3;
    b=7;
}
```

### Test
```input
if(true){
   a=3;
      b=7;
}

END
```
```output
if(true){
    a=3;
    b=7;
}
```

### Test
```input
   while(true){
   a=3;
  b=7;
}

END


```
```output
while(true){
    a=3;
    b=7;
}
```

### Test
```input
    if(true){
        a=10;
      } else {
    b=7;
  }

END
```
```output
if(true){
    a=10;
} else {
    b=7;
}
```

### Test
```input
   if(true){
   a=3;
      b=7;
 while(false){
 c=9;
    }
       }

END
```
```output
if(true){
    a=3;
    b=7;
    while(false){
        c=9;
    }
}
```

### Test
```input
 if(true){
        a=10;
    } else {
  b=7;
for(int i=0; i<10; i++){
  c=0;
  }  
     }

END
```
```output
if(true){
    a=10;
} else {
    b=7;
    for(int i=0; i<10; i++){
        c=0;
    }
}
```

### Test
```input
 if(true){
        a=10;
       } else {
       if(a==b){
          d=6;
   } else {
  b=7;
for(int i=0; i<10; i++){
  c=0;
  }
     }
}
END
```
```output
if(true){
    a=10;
} else {
    if(a==b){
        d=6;
    } else {
        b=7;
        for(int i=0; i<10; i++){
            c=0;
        }
    }
}
```

### Test
```input
while(!false){
    if(true){
        l--;
        sout();
        l++;
    } else if(false){
           sout();
           l++;
        } else if(true){
            l--;
            sout();
        } else {
            sout();
    }
}

END

```
```output
while(!false){
    if(true){
        l--;
        sout();
        l++;
    } else if(false){
        sout();
        l++;
    } else if(true){
        l--;
        sout();
    } else {
        sout();
    }
}
```

### Test private
```input
if(true){
a();
    if(true){
        a();
    } else if(true){
        if(true){
        a();    
    } else {
         if(true){
            a();    
            }
            a();
               }
          } else {
              a();
    if(true){
        a();
    }
     a();
    }
    a();
    } else {
        if(true){
            if(true){
                a();    
            }
            a();
} else {
    a();
    }
    a();
}

END
```
```output
if(true){
    a();
    if(true){
        a();
    } else if(true){
        if(true){
            a();
        } else {
            if(true){
                a();
            }
            a();
        }
    } else {
        a();
        if(true){
            a();
        }
        a();
    }
    a();
} else {
    if(true){
        if(true){
            a();
        }
        a();
    } else {
        a();
    }
    a();
}
```
