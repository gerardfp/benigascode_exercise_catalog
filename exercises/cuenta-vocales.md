---
slug: cuenta-vocales
difficulty: 4.0
tags: [strings, loops, for-loop, counters]
---
# Cuenta vocales

Dada una frase (terminada con un salto de línea), cuenta el número de veces que aparece cada vocal.

## Input

Un texto terminado con un salto de línea.

## Output

En la primera linea la cantidad de `a`, en la siguiente linea la cantidad de `e`, etc.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    String line = sc.hasNextLine() ? sc.nextLine().toLowerCase() : "";
    int a = 0, e = 0, i = 0, o = 0, u = 0;
    for (int idx = 0; idx < line.length(); idx++) {
        char c = line.charAt(idx);
        switch (c) {
            case 'a' -> a++;
            case 'e' -> e++;
            case 'i' -> i++;
            case 'o' -> o++;
            case 'u' -> u++;
        }
    }
    IO.println(a);
    IO.println(e);
    IO.println(i);
    IO.println(o);
    IO.println(u);
}
```

## Tests

### Test
```input
hola mundo
```
```output
1
0
0
2
1
```

### Test
```input
aa ee ii oo uu
```
```output
2
2
2
2
2
```

### Test
```input
xxa xax axx
```
```output
3
0
0
0
0
```

### Test
```input
aa, EE, ii.
```
```output
2
2
2
0
0
```

### Test
```input
aA eE iI oO u
```
```output
2
2
2
2
1
```

### Test private
```input
aeiou
```
```output
1
1
1
1
1
```
