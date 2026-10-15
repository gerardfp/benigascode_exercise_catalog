---
slug: evaluate-expression
tags: [strings, recursion, math, parsing]
difficulty: 5
---
# Evaluate expression

Donat un String amb una expressió aritmètica de sumes i multiplicacions, avaluar el seu resultat.

## Input

Un string amb una expressió aritmètica de sumes i multiplicacions enteres.

## Output

El resultat de l'expressió

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNext()) return;
    String expr = sc.next();
    String[] terms = expr.split("\\+");
    int total = 0;
    for (int i = 0; i < terms.length; i++) {
        String[] factors = terms[i].split("\\*");
        int prod = 1;
        for (int j = 0; j < factors.length; j++) {
            prod *= Integer.parseInt(factors[j]);
        }
        total += prod;
    }
    IO.println(total);
}
```

## Tests

### Test
```input
1
```
```output
1
```

### Test
```input
2+2
```
```output
4
```

### Test
```input
2+2+2
```
```output
6
```

### Test
```input
2*2
```
```output
4
```

### Test
```input
2*2*2
```
```output
8
```

### Test
```input
2+3*4
```
```output
14
```

### Test
```input
2*3+4
```
```output
10
```

### Test
```input
2*3+4*5
```
```output
26
```

### Test
```input
2+3*4+5
```
```output
19
```

### Test
```input
2+10*1+1*100
```
```output
112
```

### Test private
```input
123*456+789*123+456*789
```
```output
512919
```
