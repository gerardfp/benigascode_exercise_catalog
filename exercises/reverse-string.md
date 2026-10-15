---
slug: reverse-string
tags: [strings, loops, for-loop, string-manipulation, reverse]
difficulty: 2
---
# Reverse String

Donat un string, inverteix-lo

## Input

String

## Output

L'string amb els caracters en ordre invers.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    String rev = "";
    for (int i = s.length() - 1; i >= 0; i--) {
        rev += s.charAt(i);
    }
    IO.println(rev);
}
```

## Tests

### Test
```input
hola
```
```output
aloh
```

### Test
```input
hola
```
```output
aloh
```

### Test
```input
hola mon!
```
```output
!nom aloh
```

### Test
```input
java
```
```output
avaj
```

### Test
```input
toCharArray()
```
```output
)(yarrArahCot
```

### Test
```input
i love programming very much
```
```output
hcum yrev gnimmargorp evol i
```

### Test
```input
pipiripip
```
```output
pipiripip
```

### Test
```input
.si ti ,sey ?gnirts desrever gnol yrev a siht si
```
```output
is this a very long reversed string? yes, it is.
```

### Test private
```input
abcd
```
```output
dcba
```
