---
slug: fibonacci-n
difficulty: 4.0
tags: [loops, for-loop, math]
---
# Término N de Fibonacci

# Término N de la Sucesión de Fibonacci

## Enunciado
La sucesión de **Fibonacci** es una secuencia de números donde cada término se obtiene sumando los dos anteriores:
- $F(0) = 0$
- $F(1) = 1$
- $F(N) = F(N-1) + F(N-2)$ para $N >= 2$

Escribe un programa en Java que lea un número entero `N` desde la entrada estándar y calcule el valor de $F(N)$.

- Si $N < 0$, el programa debe imprimir: `ERROR`
- Si $N >= 0$, el programa debe imprimir el número $F(N)$ correspondiente.

## Formato de entrada
Un número entero `N`.

## Formato de salida
El valor de $F(N)$ o la palabra `ERROR` en una única línea.

## Ejemplo 1
Entrada:
```text
6
```
Salida:
```text
8
```

## Ejemplo 2
Entrada:
```text
0
```
Salida:
```text
0
```

## Ejemplo 3
Entrada:
```text
-3
```
Salida:
```text
ERROR
```

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int n = sc.nextInt();
    if (n < 0) {
        IO.println("ERROR");
    } else if (n == 0) {
        IO.println(0);
    } else if (n == 1) {
        IO.println(1);
    } else {
        int a = 0;
        int b = 1;
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        IO.println(b);
    }
}
```

## Tests

### Test
```input
6
```
```output
8
```

### Test
```input
0
```
```output
0
```

### Test
```input
-3
```
```output
ERROR
```

### Test
```input
15
```
```output
610
```
