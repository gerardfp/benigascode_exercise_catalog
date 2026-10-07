---
slug: informe-de-vendes
tags: [arrays]
---
# Informe de vendes

![image](1612521147-606fe603b9-informeventas.png)

Es requereix desenvolupar una aplicació que realitzi un informe de vendes.

A partir del volum de vendes de cada mes, l'informe ha d'incloure:

- El creixement mensual: consisteix en restar a les vendes de cada mes les vendes del mes anterior.
- Les vendes acumulades: es tracta de sumar a les vendes de cada mes les vendes de tots els mesos anteriors.

## Input

El primer número <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica la quantitat de mesos.

A continuació, el volum de vendes de cada mes.

## Output

S'imprimiràn, en format Array, el creixement i les vendes acumulades, cadascun en una línia.

*Es permet utilitzar el mètode `Arrays.toString()` per a imprimir els resultats*

## Plantillas

```java
import java.util.Arrays;
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
5
10 20 50 70 120
```
```output
[10, 10, 30, 20, 50]
[10, 30, 80, 150, 270]
```
```explanation
[10, 20-10, 50-20, 70-50, 120-70]

[10, 20+10, 50+20+10, 70+50+20+10, 120+70+50+20+10]
```

### Test
```input
3
100 150 250
```
```output
[100, 50, 100]
[100, 250, 500]
```
```explanation
[100, 150-100, 250-150]

[100, 150+100, 250+150+100]
```

### Test
```input
4
1 3 6 10
```
```output
[1, 2, 3, 4]
[1, 4, 10, 20]
```
```explanation
[1, 3-1, 6-3, 10-6]

[1, 3+1, 6+3+1, 10+6+3+1]
```

### Test
```input
1
1000
```
```output
[1000]
[1000]
```

### Test
```input
2
1000 1000
```
```output
[1000, 0]
[1000, 2000]
```

### Test private
```input
10
5 4 3 6 4 8 7 4 1 2
```
```output
[5, -1, -1, 3, -2, 4, -1, -3, -3, 1]
[5, 9, 12, 18, 22, 30, 37, 41, 42, 44]
```
