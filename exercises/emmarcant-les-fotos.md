---
slug: emmarcant-les-fotos
tags: [conditionals, if-else, math, geometry]
difficulty: 3
---
# Emmarcant les fotos

En Joan té un munt de fotos per a emmarcar, i vol comprar els marcs.

Els marcs han de ser suficientment grans com per a que hi càpiga la foto i a més a més ha de tenir la mateixa proporció per a que quedi bé.

La definició del rectangle d'una foto i d'un marc es pot fer amb les coordenades dels seus punts superior-dreta i inferior-esquerra:

![image](assets/c1-l2-1-emmarcant-les-fotos-img0.png)

## Input

La entrada consta de la definició del rectangle de la **foto** i del rectangle del **marc**.

Per a cada rectangle s'indiquen les coordenades (x, y) dels seus cantons superior-dreta i inferior-esquerra.

## Output

S'imprimirà "true" si el marc és adequat per a la foto, i "false" si no ho és.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int fx1 = sc.nextInt();
    int fy1 = sc.nextInt();
    int fx2 = sc.nextInt();
    int fy2 = sc.nextInt();

    int mx1 = sc.nextInt();
    int my1 = sc.nextInt();
    int mx2 = sc.nextInt();
    int my2 = sc.nextInt();

    int fw = Math.abs(fx1 - fx2);
    int fh = Math.abs(fy1 - fy2);
    int mw = Math.abs(mx1 - mx2);
    int mh = Math.abs(my1 - my2);

    int pMin = Math.min(fw, fh);
    int pMax = Math.max(fw, fh);
    int mMin = Math.min(mw, mh);
    int mMax = Math.max(mw, mh);

    boolean fits = mMin >= pMin && mMax >= pMax;
    boolean sameRatio = (pMin * mMax) == (pMax * mMin);

    IO.println(fits && sameRatio);
}
```

## Tests

### Test
```input
1 1  0 0
1 1  0 0 
```
```output
true
```
#### Explanation
La foto i el marc són iguals, per tant si que hi cap i sí que té la mateixa proporció.

### Test
```input
1 1 0 0
1 1 0 0
```
```output
true
```
#### Explanation
El marc és més gran que la foto i la proporció és la mateixa

![image](assets/c1-l2-1-emmarcant-les-fotos-img1.png)

### Test
```input
1 1 0 0
2 2 0 0
```
```output
true
```
#### Explanation
El marc és més gran que la foto, però la proporció no és la mateixa

![image](assets/c1-l2-1-emmarcant-les-fotos-img2.png)

### Test
```input
1 1 0 0
3 2 0 0
```
```output
false
```
#### Explanation
La foto i el marc tenen el mateix tamany i la proporció és la mateixa

![image](assets/c1-l2-1-emmarcant-les-fotos-img3.png)

### Test
```input
1 2  0 0
4 2  2 1
```
```output
true
```
#### Explanation
El marc i la foto tenen el mateix tamany i la proporció és la mateixa

![image](assets/c1-l2-1-emmarcant-les-fotos-img4.png)

### Test
```input
1 1  -1 0
4 3  3 1
```
```output
true
```
#### Explanation
Tenen la mateixa proporció, però el marc és més petit que la foto:

![image](assets/c1-l2-1-emmarcant-les-fotos-img5.png)

### Test
```input
1 2  -1 0
4 2  3 1
```
```output
false
```

### Test
```input
4 -2  -1 1
3 2  1 1
```
```output
false
```

### Test private
```input
4 3  0 1
8 6  0 1
```
```output
false
```
