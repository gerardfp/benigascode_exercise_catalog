---
slug: enquesta-frameworks
tags: [strings, conditionals, if-else, scanner]
difficulty: 2
---
# Enquesta frameworks

En les enquestes poden haver preguntes condicionades. Són preguntes que només es fan si s'ha donat una determinada resposta en una pregunta anterior.

En una enquesta sobre *frameworks* es pregunta als participants si en coneixen algun, i en cas afirmatiu se'ls pregunta quin. 

```
Benvingut a l'enquesta.
Coneixes algun framework?
> no
Gracies per contestar
```

```
Benvingut a l'enquesta.
Coneixes algun framework?
> si
Quin?
> react
S'ha registrat la resposta: react
Gracies per contestar
```

## Input

L'entrada té dues opcions:

- un únic `no`
- un `si` i una nova línia de text

## Output

S'imprimirà l'enquesta en el format apuntat als casos de prova

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextLine()) return;
    String ans = sc.nextLine().trim();
    IO.println("Benvingut a l'enquesta.");
    IO.println("Coneixes algun framework?");
    if (ans.equalsIgnoreCase("si")) {
        IO.println("Quin?");
        if (sc.hasNextLine()) {
            String framework = sc.nextLine();
            IO.println("S'ha registrat la resposta: " + framework);
        }
    }
    IO.println("Gracies per contestar");
}
```

## Plantillas

```java
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
      
      
    }
}
```

## Tests

### Test
```input
no
```
```output
Benvingut a l'enquesta.
Coneixes algun framework?
Gracies per contestar
```

### Test
```input
si
vue.js
```
```output
Benvingut a l'enquesta.
Coneixes algun framework?
Quin?
S'ha registrat la resposta: vue.js
Gracies per contestar
```

### Test
```input
si
svelte
```
```output
Benvingut a l'enquesta.
Coneixes algun framework?
Quin?
S'ha registrat la resposta: svelte
Gracies per contestar
```

### Test private
```input
si
Spring
```
```output
Benvingut a l'enquesta.
Coneixes algun framework?
Quin?
S'ha registrat la resposta: Spring
Gracies per contestar
```
