---
slug: inicialitzar-array
tags: [arrays, types, loops, for-loop]
difficulty: 2
---
# Inicialitzar array

Incialitza l'array d'enters anomenat `numbers` amb cinc elements `12, 17, 8, 101, 33`.

Utilitza la plantilla proporcionada.

## Input

-

## Output

-

## Solutions

```java
void main() {
    int[] numbers = {12, 17, 8, 101, 33};
    for (int i = 0; i < numbers.length; i++) {
        IO.println(numbers[i]);
    }
}
```

## Plantillas

```java
public class Main {

    public static void main(String[] args) {
        
      	// inicialitza l'array numbers
      	int[] numbers  
          
      	for (int i = 0; i < numbers.length; i++) {
         	System.out.println(numbers[i]); 
        }
    }
}
```

## Tests

### Test
```input
```
```output
12
17
8
101
33
```
