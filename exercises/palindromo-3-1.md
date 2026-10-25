---
slug: palindromo-3-1
difficulty: 3.0
tags: [strings, flags, two-pointers]
---
# Palíndrom

Donada una frase, digues si és un palíndrom 

No s'han de comptar els espais en blanc, ni els caracters de puntuació:

```
. , ' ! ? -
```

Tampoc s'han de tenir en compte les majúscules i minúscules.

## Input

Una línia amb un String.

## Output

`true` | `false`

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextLine()) return;
    String line = sc.nextLine().toLowerCase();
    
    int i = 0;
    int j = line.length() - 1;
    boolean pal = true;
    while (i < j) {
        char ci = line.charAt(i);
        if (ci == ' ' || ci == '.' || ci == ',' || ci == '\'' || ci == '!' || ci == '?' || ci == '-') {
            i++;
            continue;
        }
        char cj = line.charAt(j);
        if (cj == ' ' || cj == '.' || cj == ',' || cj == '\'' || cj == '!' || cj == '?' || cj == '-') {
            j--;
            continue;
        }
        if (ci != cj) {
            pal = false;
            break;
        }
        i++;
        j--;
    }
    IO.println(pal);
}
```

## Tests

### Test
```input
hola mon!
```
```output
false
```

### Test
```input
luz azul
```
```output
true
```

### Test
```input
a ti no, bonita.
```
```output
true
```

### Test
```input
amor a roma
```
```output
true
```

### Test
```input
Ella te da detalles
```
```output
false
```

### Test
```input
ala
```
```output
true
```

### Test
```input
anul-la la lluna
```
```output
true
```

### Test
```input
Catala, a l'atac
```
```output
true
```

### Test
```input
A una nena nua llepa-li la pell, llepa-li la pell a una nena nua.
```
```output
true
```

### Test
```input
Apa! Cal a la capa?
```
```output
true
```

### Test
```input
mnb
```
```output
false
```

### Test
```input
.lkl.
```
```output
true
```

### Test
```input
opo!
```
```output
true
```

### Test private
```input
ala!
```
```output
true
```
