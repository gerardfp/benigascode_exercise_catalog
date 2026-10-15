---
slug: new-array
tags: [arrays]
difficulty: 5
---
# New array

Inicialitza l'array de `floats` de tamany 100, amb el valor `0.0f` a tots els elements.

Després asigna els els valors següents a les posicions indicades:

```
posició | valor
---------+-------
 primera | 31.0f
  segona | 56.0f
 vintena | 12.0f
  ultima | 79.0f
---------+-------
```

## Input

-

## Output

-

## Solutions

```java
void main() {
    float[] arrayFloats = new float[100];
    arrayFloats[0] = 31.0f;
    arrayFloats[1] = 56.0f;
    arrayFloats[19] = 12.0f;
    arrayFloats[arrayFloats.length - 1] = 79.0f;

    for (int i = 0; i < arrayFloats.length; i++) {
        IO.print(arrayFloats[i] + " ");
    }
}
```

## Plantillas

```java
public class Main {

    public static void main(String[] args) {
      
      	// inicialitza l'array
      	arrayFloats
          
        // assigna els elements indicats
          
      	for (int i = 0; i < arrayFloats.length; i++) {
         	System.out.print(arrayFloats[i] + " "); 
        }
    }
}
```

## Tests

### Test
```input
```
```output
31.0 56.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 12.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 79.0 
```
