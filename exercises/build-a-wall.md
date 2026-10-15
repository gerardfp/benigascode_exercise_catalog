---
slug: build-a-wall
tags: [loops]
difficulty: 4
---
# Another brick in the wall

L'any 1978, el mític grup Pink Floyd va publicar el seu 11è disc: The Wall.
A les seves actuacions, Pink FLoyd, sempre utilitzaven efectes visuals per acompanyar la seva psicodèlica música rock. Per al tour de The Wall, un enorme mur es construïa a l'escenari entre la banda i el públic.

![image](assets/c3-l4-1-build-a-wall-img0.jpg)

En aquesta ocasió la banda ens demana una aplicació que generi un mur ASCII-ART per a projectar a l'escenari.

## Input

L'entrada consisteix en 4 nombres: amplada del maó, alçada del maó, nombre de maons per línia, nombre de línies de maons.

## Output

S'imprimirà un mur de les dimensions especificades.
El mur ha de començar amb un maó complet.

Exemple de mur 8-1-3-3:

```
----------------------------
|        |        |        |
----------------------------
    |        |        |
----------------------------
|        |        |        |
----------------------------
```

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int w = sc.nextInt();
    int brickH = sc.nextInt();
    int n = sc.nextInt();
    int l = sc.nextInt();

    String dashes = "";
    for (int i = 0; i < 1 + n * (w + 1); i++) {
        dashes += "-";
    }

    String spacesW = "";
    for (int i = 0; i < w; i++) {
        spacesW += " ";
    }

    String spacesHalfW = "";
    for (int i = 0; i < w / 2; i++) {
        spacesHalfW += " ";
    }

    String normalRow = "|";
    for (int i = 0; i < n; i++) {
        normalRow += spacesW + "|";
    }

    String offsetRow = spacesHalfW + "|";
    for (int i = 0; i < n - 1; i++) {
        offsetRow += spacesW + "|";
    }

    IO.println(dashes);
    for (int row = 0; row < l; row++) {
        String content = (row % 2 == 0) ? normalRow : offsetRow;
        for (int h = 0; h < brickH; h++) {
            IO.println(content);
        }
        IO.println(dashes);
    }
}
```

## Tests

### Test
```input
8 1 3 3
```
```output
----------------------------
|        |        |        |
----------------------------
    |        |        |
----------------------------
|        |        |        |
----------------------------
```

### Test
```input
8 1 4 3
```
```output
-------------------------------------
|        |        |        |        |
-------------------------------------
    |        |        |        |
-------------------------------------
|        |        |        |        |
-------------------------------------
```

### Test
```input
6 1 5 4
```
```output
------------------------------------
|      |      |      |      |      |
------------------------------------
   |      |      |      |      |
------------------------------------
|      |      |      |      |      |
------------------------------------
   |      |      |      |      |
------------------------------------
```

### Test
```input
6 2 4 3
```
```output
-----------------------------
|      |      |      |      |
|      |      |      |      |
-----------------------------
   |      |      |      |
   |      |      |      |
-----------------------------
|      |      |      |      |
|      |      |      |      |
-----------------------------
```

### Test
```input
6 3 4 2
```
```output
-----------------------------
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |
-----------------------------
   |      |      |      |
   |      |      |      |
   |      |      |      |
-----------------------------
```

### Test private
```input
8 1 6 10
```
```output
-------------------------------------------------------
|        |        |        |        |        |        |
-------------------------------------------------------
    |        |        |        |        |        |
-------------------------------------------------------
|        |        |        |        |        |        |
-------------------------------------------------------
    |        |        |        |        |        |
-------------------------------------------------------
|        |        |        |        |        |        |
-------------------------------------------------------
    |        |        |        |        |        |
-------------------------------------------------------
|        |        |        |        |        |        |
-------------------------------------------------------
    |        |        |        |        |        |
-------------------------------------------------------
|        |        |        |        |        |        |
-------------------------------------------------------
    |        |        |        |        |        |
-------------------------------------------------------
```
