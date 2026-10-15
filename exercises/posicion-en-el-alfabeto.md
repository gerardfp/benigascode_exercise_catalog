---
slug: posicion-en-el-alfabeto
tags: [strings, loops]
difficulty: 2
---
# Posició a l'alfabet

Donat un text, indica la posició que ocupa cada lletra del text a l'alfabet.

## Input

String

## Output

La posició de cada lletra en una línia diferent.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNextLine()) {
        String line = sc.nextLine().toLowerCase();
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if (c >= 'a' && c <= 'z') {
                IO.println(c - 'a');
            }
        }
    }
}
```

## Tests

### Test
```input
hola
```
```output
7
14
11
0
```

### Test
```input
mon
```
```output
12
14
13
```

### Test
```input
java
```
```output
9
0
21
0
```

### Test
```input
ace
```
```output
0
2
4
```

### Test
```input
tochararray
```
```output
19
14
2
7
0
17
0
17
17
0
24
```

### Test private
```input
jived fox nymph grabs quick waltz
```
```output
9
8
21
4
3
5
14
23
13
24
12
15
7
6
17
0
1
18
16
20
8
2
10
22
0
11
19
25
```
