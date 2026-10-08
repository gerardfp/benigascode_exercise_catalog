---
slug: metro-circular
---
# Metro circular

![image](assets/metro-circular-img0.png)

Estamos desarrollando un app para planificar rutas en metro. Ya la tenemos casi lista, pero hay algunas líneas que son circulares y nos traen de cabeza.

En estas líneas de metro circulares hay trenes dando vueltas en los dos sentidos. Así que si un pasajero quiere ir de una estación A a otra estación B, puede viajar en cualquiera de los dos sentidos. Claro está que en un sentido el viaje puede ser más corto que en el otro.

Nuestra app, debe informar cuál es la ruta más corta entre las estaciones de origen y destino seleccionadas por el usuario, informando del tiempo total de viaje y de todas las paradas intermedias.

## Input

El primer número  indica la cantidad de estaciones.

A continuación vienen los  nombres de cada estación (una palabra)

A continuación vienen los  tiempos de trayecto entre estaciones (en segundos):
El primer tiempo corresponde al tiempo de viaje entre la primera y la segunda estación, y así sucesivamente, de forma que el último tiempo corresponde al tiempo entre la última y la primera. Los tiempos de viajes entre las estaciones son los mismos en ambos sentidos.

Por último vienen los nombres de las estaciones de origen y destino.

Se garantiza que los tiempos de viaje en ambos sentidos entre origen y destino son distintos.

## Output

Se imprimirán los nombres de las estaciones de la ruta más corta, cada una en una nueva línea.

Al final se imprimirá el tiempo total de viaje (en segundos).

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
7
A   B   C   D   E   F   G
100 300 200 100 400 100 200

B E
```
```output
B
C
D
E
600
```

### Test
```input
5
A   B   C   D   E
100 300 400 200 500

A D
```
```output
A
E
D
700
```

### Test
```input
4
A   B   C   D
100 100 100 100

A D
```
```output
A
D
100
```

### Test
```input
4
A   B   C   D
100 100 100 400

A D
```
```output
A
B
C
D
300
```

### Test
```input
7
A   B   C   D   E   F   G
100 300 200 100 400 100 200

E B
```
```output
E
D
C
B
600
```

### Test
```input
5
A   B   C   D   E
100 300 400 200 500

D A
```
```output
D
E
A
700
```

### Test
```input
4
A   B   C   D
100 100 100 100

D A
```
```output
D
A
100
```

### Test
```input
4
A   B   C   D
100 100 100 400

D A
```
```output
D
C
B
A
300
```

### Test
```input
10
Laguna Carpetana Oporto Usera Legazpi Arganzuela Pacifico Conde Baranda ODonell
300    400       350    220   550     430        290      190   400     100

Carpetana Pacifico
```
```output
Carpetana
Laguna
ODonell
Baranda
Conde
Pacifico
1280
```

### Test
```input
10
Laguna Carpetana Oporto Usera Legazpi Arganzuela Pacifico Conde Baranda ODonell
300    400       350    220   550     430        290      190   400     100

Pacifico Carpetana 
```
```output
Pacifico
Conde
Baranda
ODonell
Laguna
Carpetana
1280
```

### Test
```input
10
Laguna Carpetana Oporto Usera Legazpi Arganzuela Pacifico Conde Baranda ODonell
300    400       350    220   550     430        290      190   400     100

Arganzuela ODonell
```
```output
Arganzuela
Pacifico
Conde
Baranda
ODonell
1310
```

### Test
```input
10
Laguna Carpetana Oporto Usera Legazpi Arganzuela Pacifico Conde Baranda ODonell
300    400       350    220   550     430        290      190   400     100

ODonell Arganzuela
```
```output
ODonell
Baranda
Conde
Pacifico
Arganzuela
1310
```
