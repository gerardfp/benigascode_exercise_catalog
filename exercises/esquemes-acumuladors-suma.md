---
slug: esquemes-acumuladors-suma
difficulty: 3.0
tags: [arrays, loops, for-loop, operators, arithmetic, accumulators]
---
# Acumuladors: suma total

Escriu un programa que llegeix una seqüència de nombres enters i calcula la suma total acumulada de tots els seus elements.

## Entrada

A la primera línia hi ha el número $N$, que indica la quantitat de nombres.

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix la suma de tots els elements de la seqüència.

## Plantillas

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    
    int suma = 0;
    // TODO: Llegeix els n nombres i acumula la suma
    
    IO.println(suma);
}
```

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int suma = 0;
    for (int i = 0; i < n; i++) {
        suma += sc.nextInt();
    }
    IO.println(suma);
}
```

## Tests

### Test
```input
4
10
20
30
40
```
```output
100
```

### Test
```input
3
-5
15
-10
```
```output
0
```

### Test
```input
1
42
```
```output
42
```

### Test
```input
5
1
2
3
4
5
```
```output
15
```
