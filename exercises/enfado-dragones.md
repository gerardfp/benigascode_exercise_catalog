---
slug: enfado-dragones
difficulty: 2.0
tags: [loops, while-loop, conditionals]
---
# El enfado de los dragones

En el reino de Dragonia, los dragones tienen muy mal genio. Un dragón puede estar tranquilo, enfadado o furioso dependiendo de cuántas monedas de oro le hayan robado.

Para cada dragón debes indicar su estado:

Si le han robado menos de 10 monedas, está tranquilo.

Si le han robado entre 10 y 50 monedas (ambos incluidos), está enfadado.

Si le han robado más de 50 monedas, está furioso.

El programa debe leer primero el número de dragones y, después, la cantidad de monedas robadas a cada uno. Para cada dragón, debe mostrar su estado.

## Entrada

La primera línea contiene un número entero `N`, que indica el número de dragones.

Las siguientes `N` líneas contienen un número entero `M`, que indica cuántas monedas de oro le han robado a cada dragón.

## Salida

Para cada dragón, imprime una línea con su estado:

tranquilo si le han robado menos de 10 monedas.

enfadado si le han robado entre 10 y 50 monedas.

furioso si le han robado más de 50 monedas.

## Plantillas

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // Escribe aquí tu solución
    }
}
```

## Tests

### Test
```input
5
3
10
25
50
51
```
```output
tranquilo
enfadado
enfadado
enfadado
furioso
```

### Test
```input
3
0
1
9
```
```output
tranquilo
tranquilo
tranquilo
```

### Test private
```input
4
10
11
49
50
```
```output
enfadado
enfadado
enfadado
enfadado
```

### Test private
```input
4
51
100
999
1000
```
```output
furioso
furioso
furioso
furioso
```

### Test private
```input
1
0
```
```output
tranquilo
```

### Test private
```input
100
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
```
```output
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
enfadado
```
