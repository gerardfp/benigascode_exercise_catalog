---
slug: ordenar-numeros
tags: [arrays, esquemes]
difficulty: 4
---
# Ordenar lista de enteros ascendente

## Enunciado
Escribe un programa en Java que lea una cantidad `N` de números enteros y a continuación los `N` valores correspondientes.

El programa debe ordenar los números de menor a mayor y mostrarlos en una sola línea, separados por un espacio en blanco.

Si `N <= 0`, el programa debe imprimir únicamente:
`VACIO`

## Formato de entrada
El primer entero `N` indica la cantidad de números a procesar. Seguidamente, se encuentran los `N` números enteros separados por espacios o saltos de línea.

## Formato de salida
Una única línea con los números ordenados de menor a mayor separados por espacios, o la palabra `VACIO`.

## Ejemplo 1
Entrada:
```text
5 10 3 8 1 6
```
Salida:
```text
1 3 6 8 10
```

## Ejemplo 2
Entrada:
```text
3 4 2 4
```
Salida:
```text
2 4 4
```

## Ejemplo 3
Entrada:
```text
0
```
Salida:
```text
VACIO
```

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int n = sc.nextInt();
    if (n <= 0) {
        IO.println("VACIO");
        return;
    }
    int[] a = new int[n];
    for (int i = 0; i < n; i++) {
        a[i] = sc.nextInt();
    }
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (i > 0) IO.print(" ");
        IO.print(a[i]);
    }
    IO.println();
}
```

## Tests

### Test
```input
5 10 3 8 1 6
```
```output
1 3 6 8 10
```

### Test
```input
3 4 2 4
```
```output
2 4 4
```

### Test
```input
0
```
```output
VACIO
```

### Test
```input
6 100 -5 20 0 50 -10
```
```output
-10 -5 0 20 50 100
```
