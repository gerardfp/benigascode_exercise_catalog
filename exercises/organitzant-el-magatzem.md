---
slug: organitzant-el-magatzem
difficulty: 5.0
tags: [arrays, loops, sorting]
---
# Organitzant el magatzem

Una empresa de logística té desitja revisar la política de col·locació de productes al magatzem.
Actualment la política és colocar els productes que van arribant el més al fons i a l'esquerra possible:

![image](assets/organitzant-el-magatzem-img0.png)

Aquesta política però, no és l'òptima, ja que els productes s'haurien pogut col·locar d'aquesta altra forma:

![image](assets/organitzant-el-magatzem-img1.png)

L'empresa desitja realitzar algunes simulacions per a detectar quan ocorren aquests problemes i poder aplicar estratègies diferents.

## Input

L'entrada consta en primer lloc del tamany del magatzem (MxN).
A continuació venen els productes que s'han d'emmagatzemar.
Primer ve el nombre de productes que venen a continuació. 
Per a cada producte s'indica el nombre de línies de la seva figura, i a continuació ve la figura.

## Output

S'imprimirà la distribució final en que queda el magatzem. Els espais buits del magatzem s'indiquen amb un punt.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int R = sc.nextInt();
    int C = sc.nextInt();
    int numP = sc.nextInt();
    sc.nextLine();

    char[][] grid = new char[R][C];
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            grid[r][c] = '.';
        }
    }

    for (int p = 0; p < numP; p++) {
        String line = sc.nextLine();
        while (line.trim().length() == 0) {
            line = sc.nextLine();
        }
        int h = Integer.parseInt(line.trim());
        String[] shape = new String[h];
        for (int i = 0; i < h; i++) {
            shape[i] = sc.nextLine();
        }

        boolean placed = false;
        for (int r = 0; r <= R - h; r++) {
            for (int c = 0; c < C; c++) {
                boolean fits = true;
                for (int i = 0; i < h; i++) {
                    for (int j = 0; j < shape[i].length(); j++) {
                        if (shape[i].charAt(j) != ' ') {
                            if (c + j >= C || grid[r + i][c + j] != '.') {
                                fits = false;
                                break;
                            }
                        }
                    }
                    if (!fits) break;
                }
                if (fits) {
                    for (int i = 0; i < h; i++) {
                        for (int j = 0; j < shape[i].length(); j++) {
                            if (shape[i].charAt(j) != ' ') {
                                grid[r + i][c + j] = shape[i].charAt(j);
                            }
                        }
                    }
                    placed = true;
                    break;
                }
            }
            if (placed) break;
        }
    }

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            IO.print(grid[r][c]);
        }
        IO.println();
    }
}
```

## Tests

### Test
```input
4 4
4
3
a
a
a
3
b
bb
bb
2
cc
 c
2
d
dd
```
```output
abcc
abbc
abb.
....
```

### Test
```input
4 4
4
3
a
a
a
3
b
bb
bb
2
cc
 c
2
d
dd
```
```output
abcc
abbc
abb.
....
```
#### Explanation
![image](assets/organitzant-el-magatzem-img2.png)

### Test
```input
3 3
2
3
pp
p
pp
3
 x
xx
 x
```
```output
ppx
pxx
ppx
```
#### Explanation
![image](assets/organitzant-el-magatzem-img3.png)

### Test
```input
3 4
3
2
oooo
oooo
2
xx
xx
1
mmmmm
```
```output
oooo
oooo
....
```
#### Explanation
![image](assets/organitzant-el-magatzem-img4.png)

### Test
```input
8 8
8
5
eeeee
ee
eeee
ee
eeeee
3
ooo
o o
ooo
1
a
4
i
i
i
i
2
u u
uuu
3
x x
 x
x x
3
y   y
 y y
  y
2
zz
zz
```
```output
eeeeeooo
eea..o.o
eeee.ooo
ee...izz
eeeeeizz
u.uy.i.y
uuu.yiy.
.....y..
```

### Test
```input
3 6
8
2
 ss
ss
2
w w w
wwwww
2
ttt
 t
2
l
ll
2
v v
 v
2
u u
uuu
2
 j
jj
2
zz
 zz
```
```output
.ssttt
sslvtv
..llv.
```

### Test private
```input
5 10
10
1
iiii
2
 t
ttt
3
s
ss
 s
2
  l
lll
2
oo
oo
3
 j
 j
jj
2
zz
 zz
4
i
i
i
i
3
l
l
ll
3
t
tt
t
```
```output
iiiit.s.oo
..ltttssoo
llljzz.sl.
...j.zz.l.
..jj....ll
```
