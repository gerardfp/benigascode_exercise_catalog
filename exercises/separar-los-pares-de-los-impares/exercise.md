---
slug: separar-los-pares-de-los-impares
tags: [condicionales, control-de-flujo]
---
# Separar els parells dels imparells

![image](1574079187-6bb595c935-Untitleddrawing3.png)

Donada una seqüència de números, s'ha de separar en base a dos criteris:

Segons la **posició**:

Se separarà la seqüència original en dues seqüències:

- En una els que ocupen una posició parell,

- En l'altra els que ocupen una posició imparell.

Segons el **valor**:

Se separarà la seqüència original en dues seqüències:

- En una els números parells,

- En l'altra els imparells.

## Input

El primer nombre  indica el tamany de la seqüència. A continuació ve la seqüència.

## Output

S'imprimirán 4 seqüències, entre les dues primeres i les dues últimes s'imprimirà un salt de línia extra.

Les dues primeres seqüències són la separació per posició (posició parell/imparell).

Les dues últimes són la separació per valor (valor parell/imparell).

## Tests

### Test 14.29
```input
3    
1 2 3
```
```output
1 3
2

2
1 3
```

### Test 14.29
```input
5    
5 4 8 6 7
```
```output
5 8 7
4 6

4 8 6
5 7
```

### Test private 14.29
```input
2   
6 3
```
```output
6
3

6
3
```

### Test private 14.29
```input
10    
3 6 34 6 2 4 6 23 45 4
```
```output
3 34 2 6 45
6 6 4 23 4

6 34 6 2 4 6 4
3 23 45
```

### Test private 14.29
```input
5   
2 3 4 5 6
```
```output
2 4 6
3 5

2 4 6
3 5
```

### Test private 14.29
```input
2  
1 2
```
```output
1
2

2
1
```

### Test private 14.26
```input
20
3 5 4 2 6 7 8 0 1 5 3 4 5 6 3 7 8 1 0 4
```
```output
3 4 6 8 1 3 5 3 8 0 
5 2 7 0 5 4 6 7 1 4 

4 2 6 8 0 4 6 8 0 4 
3 5 7 1 5 3 5 3 7 1 
```
