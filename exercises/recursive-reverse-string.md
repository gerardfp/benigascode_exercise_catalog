---
slug: recursive-reverse-string
tags: [strings, recursion, string-manipulation]
difficulty: 3
---
# Reverse String

Donat un String, invirteix-lo (implementant un algorisme recursiu)

## Input

Una línia de text

## Output

El text amb l'ordre dels caracters invertit.

## Solutions

```java
String reverse(String s) {
    if (s.length() <= 1) {
        return s;
    }
    return reverse(s.substring(1)) + s.charAt(0);
}

void main() {
    Scanner sc = new Scanner(System.in);
    if (sc.hasNextLine()) {
        String line = sc.nextLine();
        IO.println(reverse(line));
    }
}
```

## Tests

### Test
```input
a
```
```output
a
```

### Test
```input
abcde
```
```output
edcba
```

### Test
```input
ab c d efgh
```
```output
hgfe d c ba
```

### Test private
```input
cgctagcttagctaacg
```
```output
gcaatcgattcgatcgc
```
