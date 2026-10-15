---
slug: pangrama
tags: [strings, loops, for-loop, flags, boolean-array]
difficulty: 4
---
# Pangrama

Donat un text, dir si utilitza **totes** les lletres de l'alfabet.

Alfabet:

```
abcdefghijklmnopqrstuvwxyz
```

## Input

Un text en una sola línia

## Output

true | false

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextLine()) return;
    String text = sc.nextLine().toLowerCase();
    boolean[] seen = new boolean[26];
    for (int i = 0; i < text.length(); i++) {
        char ch = text.charAt(i);
        if (ch >= 'a' && ch <= 'z') {
            seen[ch - 'a'] = true;
        }
    }
    boolean allSeen = true;
    for (int i = 0; i < 26; i++) {
        if (!seen[i]) {
            allSeen = false;
            break;
        }
    }
    IO.println(allSeen);
}
```

## Tests

### Test
```input
the quick brown fox jumps over the lazy dog
```
```output
true
```

### Test
```input
grumpy wizards make toxic brew for the evil queen and jack
```
```output
true
```

### Test
```input
jackdaws love my big sphinx of quartz
```
```output
true
```

### Test
```input
hello world of java programming
```
```output
false
```

### Test private
```input
hello
```
```output
false
```
