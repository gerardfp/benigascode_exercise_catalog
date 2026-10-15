---
slug: carta-formal
tags: [scanner]
difficulty: 5
---
# Carta formal

Desitjem enviar una carta formal als nostres clients, i volem generar de forma automàtica l'encapçalament per a cada client. 

A la nostra base de dades de client tenim els camps: tractament, nom, cognom1 i cognom2.

Fes un programa que generi aquest encapçalament amb el format que s'observa a **Sample Output**

## Input

L'entrada consta de 4 línies:

```
tractament
nom
cognom1
cognom2
```

## Output

-

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    String tractament = sc.nextLine();
    String nom = sc.nextLine();
    String cognom1 = sc.nextLine();
    String cognom2 = sc.nextLine();

    IO.println(tractament + " " + cognom1 + " " + cognom2 + ", " + nom);
    IO.println();
    IO.println("El principal objectiu de la present carta...");
}
```

## Tests

### Test
```input
Senyor
Antoni
Perez
Sales
```
```output
Senyor Perez Sales, Antoni

El principal objectiu de la present carta...
```

### Test
```input
Excelentissima senyora
Maria Antonia
de la Fuente
Rodriguez
```
```output
Excelentissima senyora de la Fuente Rodriguez, Maria Antonia

El principal objectiu de la present carta...
```

### Test private
```input
Sra.
Juana
Garcia
Romero
```
```output
Sra. Garcia Romero, Juana

El principal objectiu de la present carta...
```
