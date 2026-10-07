---
slug: c3-l2-3-l33t
---
# l33t

El l33t no té regles, però un algoritme sí. Posem aquestes:

- Es substitueixen aquestes lletres:

```text
A: 4
B: 8
E: 3
G: 6
I: !
L: 1
M: /\/\
O: 0
S: 5
T: 7
U: |_|
V: \\//
W: \/\/
Z: 2
```

- La resta de lletres s'escriuen alternant minúscules i majúscules

- S'eliminen els punts i les comes

## Input

Un text amb  linies.
El text acaba amb una línia amb la paraula .

## Output

El text en llengua l33t

## Tests

### Test
```input
Hello world
END
```
```output
h3110 \/\/0R1d
```

### Test
```input
Hello leet
END
```
```output
h3110 1337
```

### Test
```input
goodbye world
END
```
```output
600d8Y3 \/\/0r1D
```

### Test
```input
all your base are belong to us
END
```
```output
411 y0|_|R 8453 4r3 8310N6 70 |_|5
```

### Test
```input
Lorem ipsum 
dolor sit amet, 
consectetur adipiscing elit.
END
```
```output
10r3/\/\ !P5|_|/\/\ 
d010R 5!7 4/\/\37 
c0N53c737|_|R 4d!P!5c!N6 31!7
```

### Test
```input
This isn't even, 
my final form.
END
```
```output
7h!5 !5N'7 3\\//3N 
/\/\y F!n41 F0r/\/\
```

### Test
```input
If the Tao is great, then the operating system is great. 
If the operating system is great, then the compiler is great. 
If the compiler is great, then the application is great. 
The user is pleased, and there is harmony in the world.
END
```
```output
!f 7H3 740 !5 6r347 7H3n 7H3 0p3R47!n6 5Y573/\/\ !5 6r347 
!F 7h3 0P3r47!N6 5y573/\/\ !5 6R347 7h3N 7h3 C0/\/\p!13R !5 6r347 
!F 7h3 C0/\/\p!13R !5 6r347 7H3n 7H3 4pP1!c47!0N !5 6r347 
7H3 |_|53r !5 P13453d 4Nd 7H3r3 !5 H4r/\/\0Ny !N 7h3 \/\/0R1d
```

### Test
```input
It's over 9000!
END
```
```output
!7'5 0\\//3R 9000!
```
