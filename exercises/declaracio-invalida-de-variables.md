---
slug: declaracio-invalida-de-variables
difficulty: 1.0
tags: [variables, types]
---
# Declaració invàlida de variables

Donades dues variables `a` i `b` amb declaracions invàlides, afegeix el tipus correcte.

## Plantillas

```java
void main() {
    a = 512343;
    b = 3431231;
      
    IO.println(a + b);
}
```

## Solutions

```java
void main() {
    int a = 512343;
    int b = 3431231;

    IO.println(a + b);
}
```

## Tests

### Test
```input
```
```output
3943574
```
