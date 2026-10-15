---
slug: calculadora-amb-menu
tags: [if, switch]
difficulty: 2
---
# Calculadora amb menú

Realitza un programa que soliciti dos nombres i mostri per pantalla el següent menú:

```
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
```

L'usuari escullirà una opció i el programa finalitzarà mostrant el resultat per pantalla.

## Input

L'entrada consta de 3 nombres:

- Els dos primers, $N1$ i $N2$, són els operands.
- El tercer nombre $OP$ és l'opció del menú seleccionada

## Output

S'imprimirà el resultat de l'operació

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    int op = sc.nextInt();

    IO.println("MENU:");
    IO.println("1.-SUMAR");
    IO.println("2.-RESTAR");
    IO.println("3.-MULTIPLICAR");
    IO.println("4.-DIVIDIR");
    IO.println("Esculli una opcio:");

    int res = switch (op) {
        case 1 -> a + b;
        case 2 -> a - b;
        case 3 -> a * b;
        case 4 -> a / b;
        default -> 0;
    };
    IO.println(res);
}
```

## Tests

### Test
```input
1 1     1
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2
```

### Test
```input
1 1     1
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2
```

### Test
```input
1 1     2
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
0
```

### Test
```input
1 1     3
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
1
```

### Test
```input
1 1     4
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
1
```

### Test
```input
2 2     1
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
4
```

### Test
```input
2 3     2
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
-1
```

### Test
```input
2 5     3
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
10
```

### Test
```input
10 5     4
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2
```

### Test private
```input
3456 678     3
```
```output
MENU:
1.-SUMAR
2.-RESTAR
3.-MULTIPLICAR
4.-DIVIDIR
Esculli una opcio:
2343168
```
