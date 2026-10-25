---
slug: cercles-rgb
difficulty: 9.0
tags: [operators, math]
---
# Cercles RGB

RGB és un model de color additiu en el qual la llum vermella, verda i blava son mesclades per a reproduir colors. És el model que s'usa en pantalles, projectors, càmeres o scànners.

![image](assets/cercles-rgb-img0.png)

Fem un experiment emetent sobre una pared tres focus rodons -de diferents tamanys i posicions- de llum vermella, verda i blava.

¿Quants colors distints veurem?

## Input

La entrada consisteix en la definició dels 3 cercles RGB. 

Cada cercle es defineix per les coordinades del seu centre ($X$, $Y$)
i la longitud del seu radi $R$.

## Output

El nombre de colors distints que es veuran.

## Tests

### Test
```input
0 0 1
1 0 1
2 0 1
```
```output
5
```
#### Explanation
![image](assets/cercles-rgb-img1.png)

### Test
```input
0 0 1
1 0 1
2 0 1
```
```output
5
```
#### Explanation
![image](assets/cercles-rgb-img2.png)

### Test
```input
0 0 1
1 0 1
3 0 1
```
```output
4
```
#### Explanation
![image](assets/cercles-rgb-img3.png)

### Test
```input
0 0 1
2 0 1
4 0 1
```
```output
3
```
#### Explanation
![image](assets/cercles-rgb-img4.png)

### Test
```input
1 0 4
2 0 2
0 0 2
```
```output
4
```
#### Explanation
![image](assets/cercles-rgb-img5.png)

### Test
```input
1 0 2
3 0 1
0 0 1
```
```output
4
```
#### Explanation
![image](assets/cercles-rgb-img6.png)

### Test
```input
0 1 1
1 0 1
1 1 1
```
```output
7
```
#### Explanation
![image](assets/cercles-rgb-img7.png)

### Test
```input
0 0 4
4 0 3
4 0 2
```
```output
5
```
#### Explanation
![image](assets/cercles-rgb-img8.png)

### Test
```input
0 0 4
0 0 3
0 0 2
```
```output
3
```
#### Explanation
![image](assets/cercles-rgb-img9.png)

### Test
```input
0 0 4
2 0 3
2 0 1
```
```output
4
```
#### Explanation
![image](assets/cercles-rgb-img10.png)

### Test
```input
0 0 4
2 0 3
4 0 2
```
```output
6
```
#### Explanation
![image](assets/cercles-rgb-img11.png)

### Test
```input
0 0 4
6 0 4
3 0 2
```
```output
6
```
#### Explanation
![image](assets/cercles-rgb-img12.png)

### Test
```input
0 4 4
6 2 3
5 6 2
```
```output
6
```
#### Explanation
![image](assets/cercles-rgb-img13.png)

### Test private
```input
2 0 4
4 0 2
0 0 2
```
```output
3
```
