---
slug: palindrom
tags: [strings, recursion, flags]
difficulty: 3
---
# Palíndrom

Donat un String, dir si és un palíndrom.

## Input

String

## Output

{ true | false }

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNext()) return;
    String s = sc.next();
    boolean pal = true;
    int i = 0, j = s.length() - 1;
    while (i < j) {
        if (s.charAt(i) != s.charAt(j)) {
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
a
```
```output
true
```

### Test
```input
a
```
```output
true
```

### Test
```input
aa
```
```output
true
```

### Test
```input
aba
```
```output
true
```

### Test
```input
abba
```
```output
true
```

### Test
```input
abcba
```
```output
true
```

### Test
```input
abcb
```
```output
false
```

### Test
```input
abcdcb
```
```output
false
```

### Test private
```input
abcdcbaa
```
```output
false
```
