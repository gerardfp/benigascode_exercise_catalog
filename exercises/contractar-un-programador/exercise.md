---
slug: contractar-un-programador
tags: [operadors]
---
# Contractar un programador

Una empresa necessita programadors Java i Python. En el procés de selecció de programadors l'empresa té en compte si es coneix el llenguatge i els anys d'experiència laboral amb el llenguatge.

L'empresa vol contractar:

a) programadors que coneguin Java i portin `1` any o més programant en Java

b) programadors que coneguin Python i portin `3` anys o més progamant en Python

Escriu un programa que a partir de les dades digui si passa el procés de selecció.

## Input

L'entrada consta de 4 dades.

- un boolea indicant si coneix Java
- un enter indicant els anys d'experiència en Java
- un boolea indicant si coneix Python
- un enter indicant els anys d'experiència en Python

## Output

`true` | `false`

## Plantillas

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
      
     
    }
}
```

## Tests

### Test
```input
true 1
false 0
```
```output
true
```

### Test
```input
false 0
true 3
```
```output
true
```

### Test
```input
true 0
true 2
```
```output
false
```

### Test
```input
true 3
true 2
```
```output
true
```

### Test
```input
false 1
false 1
```
```output
false
```
```explanation
Inexplicablement, aquest candidat té 1 any d'experiència en Java, però no coneix el llenguatge...
```

### Test private
```input
false 0
true 2
```
```output
false
```
