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

### Test 6.67
```input
French
```
```output
Bonjour
```

### Test 6.67
```input
French
```
```output
Bonjour
```

### Test private 6.67
```input
Spanish
```
```output
Hola
```

### Test private 6.67
```input
Russian
```
```output
Zdravstvuyte
```

### Test private 6.67
```input
Zulu
Sawubona
```
```output
No conec el teu idioma, com es diu hola?
Sawubona
```

### Test private 6.67
```input
Chinese
```
```output
Nin hao
```

### Test private 6.67
```input
Italian
Salve
```
```output
No conec el teu idioma, com es diu hola?
Salve
```

### Test private 6.67
```input
Japanese
```
```output
Konnichiwa
```

### Test private 6.67
```input
Swahili
Hujambo
```
```output
No conec el teu idioma, com es diu hola?
Hujambo
```

### Test private 6.67
```input
German
```
```output
Guten Tag
```

### Test private 6.67
```input
Portuguese
```
```output
Ola
```

### Test private 6.67
```input
Korean
Anyoung haseyo
```
```output
No conec el teu idioma, com es diu hola?
Anyoung haseyo
```

### Test private 6.67
```input
Arabic
```
```output
Asalaam alaikum
```

### Test private 6.67
```input
Hindi
```
```output
Namaste
```

### Test private 6.62
```input
Romanian
```
```output
Buna ziua
```
