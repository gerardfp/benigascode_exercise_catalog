---
slug: aprovar-el-modul
tags: [operadors, logics]
difficulty: 2
---
# Aprovar el mòdul

Per a aprovar el mòdul de programació, un alumne ha d'aprovar els 3 Trimestres.

Per a aprovar el T1, un alumne ha d'entregar com a mínim el 75% de les pràctiques i traure un com a mínim un 4 en l'examen. També pot aprovar aquesta Trimestre si entrega el 50% de les pràctiques i trau mínim un 5. I també aprova si trau més d'un 7 a l'examen (independentment de les practiques que hagi entregat).

Per a aprovar el T2, ha d'entregar com a mínim el 75% de les pràctiques i traure un com a mínim un 4 en l'examen. També pot aprovar si entrega totes les pràctiques o si entrega mínim el 50% de les pràctiques i trau com a mínim un 5 a l'examen.

Per a aprovar el T3, un alumne ha d'entregar totes les pràctiques i traure un com a mínim un 5 en l'examen.

## Input

La entrada consisteix en 9 nombres:

- Els tres primers nombres corresponen al T1: el nombre total de pràctiques, el nombre de pràctiques entregades i la nota de l'examen.
- Els tres següents nombres corresponen al T2: el nombre total de pràctiques, el nombre de pràctiques entregades i la nota de l'examen.
- Els tres últims nombres corresponen al T3: el nombre total de pràctiques, el nombre de pràctiques entregades i la nota de l'examen.

## Output

S'imprimirà `true` si l'alumne aprova el mòdul, o `false` si no l'aprova.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextDouble()) return;
    double t1 = Double.parseDouble(sc.next());
    double d1 = Double.parseDouble(sc.next());
    double e1 = Double.parseDouble(sc.next());
    double t2 = Double.parseDouble(sc.next());
    double d2 = Double.parseDouble(sc.next());
    double e2 = Double.parseDouble(sc.next());
    double t3 = Double.parseDouble(sc.next());
    double d3 = Double.parseDouble(sc.next());
    double e3 = Double.parseDouble(sc.next());

    boolean uf1 = (d1 >= 0.75 * t1 && e1 >= 4) || (d1 >= 0.50 * t1 && e1 >= 5) || (e1 > 7);
    boolean uf2 = (d2 >= 0.75 * t2 && e2 >= 4) || (d2 == t2) || (d2 >= 0.50 * t2 && e2 >= 5);
    boolean uf3 = (d3 == t3 && e3 >= 5);

    IO.println(uf1 && uf2 && uf3);
}
```

## Tests

### Test
```input
6 2 4
3 0 0
1 0 0
```
```output
false
```
#### Explanation
En la UF1 hi havia 6 pràctiques, se n'han entregat 2 i ha tret un 4 en l'examen.
No reuneix cap condició per aprovar la UF1, per tant no aprova el Mòdul.

### Test
```input
6 5 4
3 1 5
1 0 0
```
```output
false
```
#### Explanation
En la UF1 hi havia 6 pràctiques, n'ha entregat 5 i ha tret un 4 a l'examen. Per tant, aprova la UF1.
En la UF2 hi havia 3 pràctiques, n'ha entregat 1 i ha tret un 5 a l'examen. No aprova la UF2, ja que no ha entregat el 50% de les pràctiques. Per tant no aprova el Mòdul.

### Test
```input
6 0 8
3 2 5
1 0 10
```
```output
false
```
#### Explanation
En la UF1 no ha entregat cap pràctica però ha tret més d'un 7 a l'examen, per tant aprova la UF1.
En la UF2 ha entregat com a mínim el 50% de les pràctiques i ha tret com a mínim un 5 a l'examen, per tant aprova la UF2.
En la UF3 no ha entregat totes les pràctiques, així que tot i que té un 10 a l'examen, està suspés de la UF3. No aprova el mòdul.

### Test
```input
6 3 4
3 3 5
1 1 10
```
```output
false
```
#### Explanation
En la UF1 ha entregat el 50% de les pràctiques però no ha tret com a mínim un 5 a l'examen, per tant no aprova la UF1.
Tot i que la UF2 i la UF3 estan aprovades, no aprova el mòdul.

### Test
```input
6 3 5
3 3 10
1 1 10
```
```output
true
```
#### Explanation
En la UF1 ha entregat el 50% de les pràctiques i ha tret un 5 a l'examen, per tant l'aprova.
En les altres dos UF, ha entregat totes les pràctiques i ha aprovat l'examen, per tant les aprova.
Aprova el mòdul.

### Test
```input
10 5 5
3 3 0
1 1 5
```
```output
true
```

### Test private
```input
1 0 0
1 0 0
1 0 0
```
```output
false
```
