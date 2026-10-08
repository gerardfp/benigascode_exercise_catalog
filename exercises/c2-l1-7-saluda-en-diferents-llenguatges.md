---
slug: c2-l1-7-saluda-en-diferents-llenguatges
tags: [condicionales, control-de-flujo]
---
# Saluda en diferents idiomes

Fes un programa que faci una salutació en un d'aquests idiomes:

- French: Bonjour

- Spanish: Hola

- Russian: Zdravstvuyte

- Chinese: Nin hao

- Japanese: Konnichiwa

- German: Guten Tag

- Portuguese: Ola

- Arabic: Asalaam alaikum

- Hindi: Namaste

- Romanian: Buna ziua

Si el programa no reconeix l'idioma, demana educadament: "*No conec el teu idioma, com es diu hola?*". Aleshores fes una salutació en aquest idioma.

## Input

Un idioma.

Si el idioma no és reconegut pel programa, aleshores s'indica la salutació en aquest idioma.

## Output

S'imprimirà la salutació en l'idioma especificat.

Si l'idioma no és un de la llista, s'imprimirà la frase `No conec el teu idioma, com es diu hola?`, i aleshores s'imprimirà la salutació rebuda.

## Plantillas

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
      
        /*
        "French" "Bonjour"
        "Spanish" "Hola"
        "Russian" "Zdravstvuyte"
        "Chinese" "Nin hao"
        "Japanese" "Konnichiwa"
        "German" "Guten Tag"
        "Portuguese" "Ola"
        "Arabic" "Asalaam alaikum"
        "Hindi" "Namaste"
        "Romanian" "Buna ziua"
        */
    }
}
```

## Tests

### Test
```input
French
```
```output
Bonjour
```

### Test
```input
French
```
```output
Bonjour
```

### Test
```input
Spanish
```
```output
Hola
```

### Test
```input
Russian
```
```output
Zdravstvuyte
```

### Test
```input
Zulu
Sawubona
```
```output
No conec el teu idioma, com es diu hola?
Sawubona
```

### Test
```input
Chinese
```
```output
Nin hao
```

### Test
```input
Italian
Salve
```
```output
No conec el teu idioma, com es diu hola?
Salve
```

### Test
```input
Japanese
```
```output
Konnichiwa
```

### Test
```input
Swahili
Hujambo
```
```output
No conec el teu idioma, com es diu hola?
Hujambo
```

### Test
```input
German
```
```output
Guten Tag
```

### Test
```input
Portuguese
```
```output
Ola
```

### Test
```input
Korean
Anyoung haseyo
```
```output
No conec el teu idioma, com es diu hola?
Anyoung haseyo
```

### Test
```input
Arabic
```
```output
Asalaam alaikum
```

### Test
```input
Hindi
```
```output
Namaste
```

### Test
```input
Romanian
```
```output
Buna ziua
```
