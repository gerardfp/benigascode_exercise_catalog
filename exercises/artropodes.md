---
slug: artropodes
tags: [operadors, aritmetics]
difficulty: 1
---
# Artròpodes

En la classe de Naturals estan estudiant els artròpodes. Són animals invertebrats dotats d'un esquelet extern i apèndixs articulats. Es divideixen en insectes, aràcnids, crustacis i miriàpodes. El nombre de potes en aquests animals és molt variable:

- Els insectes tenen 6 potes
- Els aràcnids tenen 8 potes
- Els crustacis tenen 10 potes
- Els miriàpodes tenen 2 o 4 potes per cada segment del seu cos

![image](assets/c1-l1-12-artropodes-img0.png)

Un dia la professora va demanar als alumnes que portessin artròpodes a classe i els va posar un problema de matemàtiques: calcular el nombre de pates de tots els animals que havien portat.

## Input

El primer nombre $I$ indica el nombre d'insectes.

El segon nombre $A$ indica el nombre d'aràcnids.

El tercer nombre $C$ indica el nombre de crustacis.

El quart nombre $M1$ indica el nombre de miriàpodes de 2 potes i el cinquè el nombre $S1$ el nombre de segments que tenen.

El sisè nombre $M2$ indica el nombre de miriàpodes de 4 potes i el setè nombre $S2$ el nombre de segments que tenen.

## Output

Un nombre indicant la quantitat total de potes.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int insects = sc.nextInt();
    int arachnids = sc.nextInt();
    int crustaceans = sc.nextInt();
    int m1 = sc.nextInt();
    int s1 = sc.nextInt();
    int m2 = sc.nextInt();
    int s2 = sc.nextInt();

    int total = insects * 6 + arachnids * 8 + crustaceans * 10 + m1 * s1 * 2 + m2 * s2 * 4;
    IO.println(total);
}
```

## Tests

### Test
```input
1
0
0
0 10
0 10
```
```output
6
```
#### Explanation
Només hi ha un insecte, per tant 6 potes

### Test
```input
1
0
0
0 10
0 10
```
```output
6
```
#### Explanation
Només hi ha un aràcnid, per tant 8 potes

### Test
```input
0
1 
0
0 5
0 5
```
```output
8
```
#### Explanation
Només hi ha 2 crustacis, per tant 20 potes

### Test
```input
0
0
2
0 12
0 14
```
```output
20
```
#### Explanation
Hi ha un miriàpode de 10 segments (2 potes per segment), per tant 20 potes

### Test
```input
0
0
0
1 10
0 12
```
```output
20
```
#### Explanation
Hi ha un miriàpode (de 4 potes per segment) amb 10 segments, per tant 40 potes

### Test
```input
0
0
0
0 8
1 10
```
```output
40
```

### Test
```input
1
1
1
1 10
1 10
```
```output
84
```

### Test private
```input
7
11
5
3 10
2 12
```
```output
336
```
