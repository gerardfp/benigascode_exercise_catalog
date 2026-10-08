---
slug: carta-formal
tags: [control-de-flujo, loops]
---
# Carta formal

Desitjem enviar una carta formal als nostres clients, i volem generar de forma automàtica l'encapçalament per a cada client.

A la nostra base de dades de client tenim els camps: tractament, nom, cognom1 i cognom2.

Fes un programa que generi aquest encapçalament amb el format que s'observa a **Sample Output**

## Input

L'entrada consta de 4 línies:

```text
`tractament
nom
cognom1
cognom2
`
```

## Output

-

## Plantillas

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
      	Scanner scanner = new Scanner(System.in);
      
      
    }
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

### Test
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
