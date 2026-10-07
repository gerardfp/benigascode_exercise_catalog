---
slug: inventari
---
# Inventari

![image](1612523128-71db09dc8d-ab1c9693af1c85815c500ef79c575eab.png)

En un magatzem és important portar el control de les entrades i sortides de mercaderies i mantenir l'inventari amb la màxima precisió.

Quan hi ha una sortida de mercaderies, s'ha de disminuir l'inventari d'aquestes mercaderies. I quan es produeix una entrada, l'inventari s'ha d'augmentar.

Lògicament, l'inventari d'un producte no pot ser inferior a zero. Així que quan arriba una ordre de sortida, si la quantitat demandada d'una mercaderia és superior a l'stock, només es servirà la quantitat disponible al magatzem.

El magatzem també té una capacitat total límit, així que quan arriba una ordre d'entrada, només s'acceptarà la quantitat de mercaderies sense superar aquest límit. *Suposem que aquest límit es refereix a la quantitat de mercaderies, i no al seu tamany, forma o pes.*

## Input

L'entrada consisteix en primer lloc en la situació actual del magatzem:

- El primer enter  és la capacitat màxima del magatzem

- El segon nombre  indica la quantitat de productes

- A continuació ve una sèrie amb els  codis de productes (una paraula)

- A continuació ve una sèrie amb els  stocks de cada producte (un enter)

En segon lloc, venen les ordres d'entrada/sortida:

- El primer nombre  indica la quantitat d'ordres

- A continuació venen les  ordres, cadascuna en una línia, i per a cada ordre s'indica:

El codi del producte

- La quantitat (positiva per a les ordres d'entrada i negativa per a les de sortida)

## Output

S'imprimirà l'stock final de cada mercaderia, separats per espais en blanc, després de realitzar totes les ordres.

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
100
3
ABC MNO XYZ
25  30  15

4
ABC 10
MNO -20
ABC 5
XYZ -10
```
```output
40 10 5
```

### Test
```input
50
5
ABC IJK MNO RST XYZ
10  10  10  10  10

3
ABC 10
MNO -10
ABC 10
```
```output
20 10 0 10 10
```

### Test
```input
20
2
ABC MNO
10  5

1
ABC 30
```
```output
15 5
```

### Test
```input
20
2
ABC MNO
10  20

2
ABC -20
MNO -30
```
```output
0 0
```
