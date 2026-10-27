---
slug: esquemes-cerca-lineal-posicio
difficulty: 2.0
tags: [arrays, loops, for-loop, search]
---
# Cerca lineal: primera posició d'un valor

Donada una seqüència de $N$ nombres enters i un valor objectiu $X$, troba l'índex (posició base 0) de la primera aparició de $X$ a la seqüència. Si el valor $X$ no es troba a la seqüència, imprimeix `-1`.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen els $N$ nombres enters de la seqüència.

A l'última línia hi ha el valor $X$ a cercar.

## Salida

Imprimeix l'índex de la primera aparició de $X$, o `-1` si no existeix.

## Plantillas

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
    int x = sc.nextInt();

    int pos = -1;
    // TODO: Cerca lineal del primer índex de x i atura't en trobar-lo (break)

    IO.println(pos);
}
```

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
    int x = sc.nextInt();

    int pos = -1;
    for (int i = 0; i < n; i++) {
        if (nums[i] == x) {
            pos = i;
            break;
        }
    }
    IO.println(pos);
}
```

## Tests

### Test
```input
5
10
20
30
20
40
20
```
```output
1
```

### Test
```input
4
1
2
3
4
99
```
```output
-1
```

### Test
```input
3
5
6
7
5
```
```output
0
```

### Test
```input
1
8
8
```
```output
0
```
