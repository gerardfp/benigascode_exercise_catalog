---
slug: maxima-puntuacio
difficulty: 4.0
tags: [strings, loops, while-loop, min-max]
---
# Màxima puntuació

En molts jocs guanya qui ha fet més punts al final de la partida.

Esbrina qui és el guanyador a partir de les puntuacions finals de 6 jugadors.

## Input

L'entrada consta de 6 noms amb 6 puntuacions.

## Output

El nom i la puntuació del guanyador

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    String maxName = "";
    int maxScore = Integer.MIN_VALUE;
    for (int i = 0; i < 6 && sc.hasNext(); i++) {
        String name = sc.next();
        int score = sc.nextInt();
        if (score > maxScore) {
            maxScore = score;
            maxName = name;
        }
    }
    IO.println(maxName + " " + maxScore);
}
```

## Tests

### Test
```input
Larry 100
Ken 101
Philip 105
Niklaus 110
Rasmus 99
Chris 70
```
```output
Niklaus 110
```

### Test
```input
Bjarne 80
Guido  77
Dennis 99
Yukihiro 89
Alan 90
James 100
```
```output
James 100
```

### Test
```input
Grace 105
Kathleen 99
Brendan 96
Anders 101
Roberto 87
Xavier 70
```
```output
Grace 105
```

### Test private
```input
Grace 105
Kathleen 99
Brendan 96
Anders 101
Roberto 115
Xavier 70
```
```output
Roberto 115
```
