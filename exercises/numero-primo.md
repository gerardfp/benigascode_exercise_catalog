---
slug: numero-primo
tags: [loops, for-loop, math, flags]
difficulty: 3
---
# Determinar si un número es primo

## Enunciado
Un número entero mayor que 1 es **primo** si únicamente es divisible de manera exacta entre 1 y entre sí mismo. Los números menores o iguales a 1 no se consideran primos.

Escribe un programa en Java que lea un número entero `N` desde la entrada estándar.

- Si `N` es primo, imprime:
  `PRIMO`
- En caso contrario, imprime:
  `NO_PRIMO`

## Formato de entrada
Un único número entero `N` leído desde la entrada estándar.

## Formato de salida
La palabra `PRIMO` o `NO_PRIMO` en una única línea.

## Ejemplo 1
Entrada:
```text
7
```
Salida:
```text
PRIMO
```

## Ejemplo 2
Entrada:
```text
12
```
Salida:
```text
NO_PRIMO
```

## Ejemplo 3
Entrada:
```text
1
```
Salida:
```text
NO_PRIMO
```

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    if (n <= 1) {
        IO.println("NO_PRIMO");
        return;
    }
    boolean isPrime = true;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime) {
        IO.println("PRIMO");
    } else {
        IO.println("NO_PRIMO");
    }
}
```

## Tests

### Test
```input
7
```
```output
PRIMO
```

### Test
```input
12
```
```output
NO_PRIMO
```

### Test
```input
1
```
```output
NO_PRIMO
```

### Test
```input
997
```
```output
PRIMO
```
