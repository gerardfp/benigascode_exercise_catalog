---
slug: esquemes-extrems-maxim
difficulty: 3.0
tags: [arrays, loops, for-loop, operators, relational-operators, min-max]
---
# Extrems: valor màxim

Escriu un programa que llegeix una seqüència de $N$ nombres enters i troba el valor més gran (el màxim) de la seqüència.

## Entrada

A la primera línia hi ha el número $N$ ($N \ge 1$).

A continuació venen els $N$ nombres enters, cadascun en una línia.

## Salida

Imprimeix el valor màxim trobat.

## Plantillas

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();

    // Regla d'or: inicialitza max amb el primer element
    int max = nums[0];
    
    // TODO: Recorre a partir de l'índex 1 i actualitza max
    
    IO.println(max);
}
```

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();

    int max = nums[0];
    for (int i = 1; i < n; i++) {
        if (nums[i] > max) {
            max = nums[i];
        }
    }
    IO.println(max);
}
```

## Tests

### Test
```input
5
12
45
67
23
89
```
```output
89
```

### Test
```input
4
-10
-3
-50
-2
```
```output
-2
```

### Test
```input
1
100
```
```output
100
```

### Test
```input
4
7
7
7
7
```
```output
7
```
