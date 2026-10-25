---
slug: distancia-hamming
difficulty: 3.0
tags: [strings, loops, for-loop, counters]
---
# Distància Hamming

Donats dos Strings, calcula la seva distància Hamming.

La distància Hamming entre dos Strings de la mateixa longitud és la quantitat de posicions en les quals els caracters són diferents.

Exemple:

```
Hola mon
Hala man
```

La distància Hamming entre "Hola mon" i "Hala man" és 2, ja que en les posicions 1 i 6 els caracters són diferents.

## Input

Dos Strings, cadascun en una línia.

## Output

La distància Hamming entre els dos Strings, **si són d'igual longitud**.

Si són de distinta longitud s'imprimirá -1.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextLine()) return;
    String s1 = sc.nextLine();
    if (!sc.hasNextLine()) return;
    String s2 = sc.nextLine();
    if (s1.length() != s2.length()) {
        IO.println(-1);
    } else {
        int dist = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                dist++;
            }
        }
        IO.println(dist);
    }
}
```

## Tests

### Test
```input
Hola mon
Hala man
```
```output
2
```

### Test
```input
i hate java
i love java
```
```output
3
```

### Test
```input
CAGGTACAGT
AAGGTACTTA
```
```output
4
```

### Test
```input
1011010
1000010
```
```output
2
```

### Test
```input
hola
hol
```
```output
-1
```

### Test
```input
CGATTGACGATCAT
CGATGCTGACTAT
```
```output
-1
```

### Test
```input
hola
hola
```
```output
0
```

### Test
```input
h
k
```
```output
1
```

### Test
```input
a
a
```
```output
0
```

### Test
```input
is this a string?
is this a  string?
```
```output
-1
```

### Test
```input
aa
aa
```
```output
0
```

### Test
```input
aa
a
```
```output
-1
```

### Test private
```input
aa
ab
```
```output
1
```
