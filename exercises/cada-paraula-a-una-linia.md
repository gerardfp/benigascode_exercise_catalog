---
slug: cada-paraula-a-una-linia
tags: [strings, scanner, io]
difficulty: 1
---
# Cada paraula a una línia

Escriu un programa que llegeixi cinc paraules de l'entrada estàndard i imprimeixi cada paraula en una nova línia. Les paraules han d'estar en el mateix ordre.

## Input

Cinc paraules, separades per espais en blanc o salts de línia.

## Output

Cada paraula en una nova línia.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    for (int i = 0; i < 5; i++) {
        IO.println(sc.next());
    }
}
```

## Tests

### Test
```input
Java te
8 tipus primitius
```
```output
Java
te
8
tipus
primitius
```

### Test
```input
Java te 5
operadors
aritmetics
```
```output
Java
te
5
operadors
aritmetics
```

### Test
```input
gat gos
vaca
porc gall
```
```output
gat
gos
vaca
porc
gall
```

### Test
```input
a b c d e
```
```output
a
b
c
d
e
```

### Test private
```input
q w d r t
```
```output
q
w
d
r
t
```
