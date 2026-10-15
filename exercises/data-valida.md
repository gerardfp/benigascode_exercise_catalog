---
slug: data-valida
tags: [conditionals, if-else, booleans, date-time]
difficulty: 2
---
# Data vàlida

Una data és vàlida si el número de dia està dintre dels dies del mes.

Cal tenir en compte que un any pot ser bixest. Un any és bixest si és divisible entre quatre i, o bé no és divisible entre 100 o és divisible entre 400.

## Input

Tres nombres corresponents a una data en format `dd/mm/yyyy`

## Output

`true` si la data és vàlida

`false` si no ho és

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int d = sc.nextInt();
    int m = sc.nextInt();
    int y = sc.nextInt();

    boolean leap = (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
    int maxDays = switch (m) {
        case 1, 3, 5, 7, 8, 10, 12 -> 31;
        case 4, 6, 9, 11 -> 30;
        case 2 -> leap ? 29 : 28;
        default -> 0;
    };

    boolean valid = d >= 1 && d <= maxDays;
    IO.println(valid);
}
```

## Tests

### Test
```input
1 10 2000
```
```output
true
```
#### Explanation
1 d'Octubre del 2000 és una data vàlida

### Test
```input
1 1 2000
```
```output
true
```
#### Explanation
32 d'Ocutbre del 2000 no és una data vàlida

### Test
```input
32 10 2000
```
```output
false
```
#### Explanation
31 d'Octubre del 2000 és una data vàlida

### Test
```input
31 10 2000
```
```output
true
```

### Test
```input
31 11 2000
```
```output
false
```
#### Explanation
El 2000 és bixest

### Test
```input
29 2 2000
```
```output
true
```
#### Explanation
El 1900 no és bixest

### Test
```input
29 2 1900
```
```output
false
```
#### Explanation
El 1904 és bixest

### Test
```input
29 2 1904
```
```output
true
```

### Test
```input
28 2 1994
```
```output
true
```

### Test
```input
29 2 2020
```
```output
true
```

### Test
```input
29 2 2100
```
```output
false
```

### Test
```input
31 8 2024
```
```output
true
```

### Test
```input
31 9 2024
```
```output
false
```

### Test
```input
30 6 2024
```
```output
true
```

### Test
```input
31 4 2024
```
```output
false
```

### Test private
```input
0 1 2020
```
```output
false
```
