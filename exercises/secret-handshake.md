---
slug: secret-handshake
difficulty: 4.0
tags: [conditionals, if-else, operators, bitwise]
---
# Secret Handshake

Hi ha 10 tipus de persones al món: *els que entenen el binari i els que no*.

Vosaltres i els vostres companys de cohort dels que "sabeu" quan es tracta d’un binari decidiu crear una "salutació" secreta.

```
1 = fer l'ullet
10 = doble parpalleig
100 = tancar el ulls
1000 = saltar
```

## Input

La entrada consisteix en una seqüència de 4 bits, separats per espais.

## Output

S'escriurà la seqüència d'events de la "salutació" secreta

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    String s = "";
    for (int i = 0; i < 4; i++) {
        s += sc.next();
    }
    int i = 0;
    while (i < s.length()) {
        if (s.charAt(i) == '1') {
            int j = i + 1;
            while (j < s.length() && s.charAt(j) == '0') {
                j++;
            }
            int zeros = j - i - 1;
            if (zeros == 0) {
                IO.println("fer l'ullet");
            } else if (zeros == 1) {
                IO.println("doble parpalleig");
            } else if (zeros == 2) {
                IO.println("tancar els ulls");
            } else if (zeros == 3) {
                IO.println("saltar");
            }
            i = j;
        } else {
            i++;
        }
    }
}
```

## Tests

### Test
```input
1 0 0 0
```
```output
saltar
```

### Test
```input
1 0 0 0
```
```output
saltar
```

### Test
```input
1 0 0 1
```
```output
tancar els ulls
fer l'ullet
```

### Test
```input
1 0 1 0
```
```output
doble parpalleig
doble parpalleig
```

### Test
```input
1 0 1 1
```
```output
doble parpalleig
fer l'ullet
fer l'ullet
```

### Test
```input
1 1 0 0
```
```output
fer l'ullet
tancar els ulls
```

### Test
```input
1 1 0 1
```
```output
fer l'ullet
doble parpalleig
fer l'ullet
```

### Test
```input
1 1 1 0
```
```output
fer l'ullet
fer l'ullet
doble parpalleig
```

### Test private
```input
1 1 1 1
```
```output
fer l'ullet
fer l'ullet
fer l'ullet
fer l'ullet
```
