---
slug: c4-l2-4-balanceig-de-carrega
---
# Balanceig de càrrega

El balanceig de càrrega consisteix en la distribució de la feina a realitzar entre diferents recursos com ordinadors, clústers, línies de xarxa, unitats centrals de processament o dispositius de disc.

En aquest problema tractarem el balanceig de càrrega de dispositius de disc en funció de l'espai disponible.

Quan s'ha d'emmagatzemar un bloc de dades, el balancejador de càrrega escull el disc amb més espai disponible per a emmagaztemar-les:

![image](1559057293-33da2565fb-diskbalancer.png)

## Input

En primer lloc trobem el nombre de discs <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.924ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 828.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M287 628Q287 635 230 637Q207 637 200 638T193 647Q193 655 197 667T204 682Q206 683 403 683Q570 682 590 682T630 676Q702 659 752 597T803 431Q803 275 696 151T444 3L430 1L236 0H125H72Q48 0 41 2T33 11Q33 13 36 25Q40 41 44 43T67 46Q94 46 127 49Q141 52 146 61Q149 65 218 339T287 628ZM703 469Q703 507 692 537T666 584T629 613T590 629T555 636Q553 636 541 636T512 636T479 637H436Q392 637 386 627Q384 623 313 339T242 52Q242 48 253 48T330 47Q335 47 349 47T373 46Q499 46 581 128Q617 164 640 212T683 339T703 469Z"></path></g></svg></span>.

A continuació ve l'espai ocupat a cada disc.

Seguidament ve un seqüència amb els tamanys dels blocs de dades que s'han d'emmagatzemar. La seqüència finalitza amb un 0.

## Output

S'imprimirà l'espai ocupat en cada disc un cop s'han emmagatzemat tots els blocs.

## Tests

### Test
```input
2
0 0
2 3 6 1 5 2   0
```
```output
10 9
```
```explanation
Disposem de dos discs, la ocupació inicial dels quals és:
```

### Test
```input
2
0 0
2 3 6 1 5 2   0
```
```output
10 9
```
```explanation
Inicialment tenim aquesta ocupació dels discs:
```

### Test
```input
3
1 4 5
1 2 3 4 5  0
```
```output
7 8 10
```

### Test
```input
5
3 0 1 6 10
10  4  1  5  3  1  2  4  8  9     0
```
```output
17 10 12 18 10
```

### Test
```input
6
10 0 10 10 30 40
16  54  40  36  16  57  20  52  36  29  24  26  16  20  35     0
```
```output
90 92 99 117 87 92
```

### Test private
```input
8
100 0 110 70 20 35 45 90
38  65  16  88  20  49  94  81  32  56  13  47  32  52  86  81  75  58  71  59  24  31  88  75  90  13  76  42  97  103  93  87  47  102  35  11  107  55  17  16  105  10  18  94  73  96  67  17  47  102     0
```
```output
407 423 425 435 411 485 420 415
```
