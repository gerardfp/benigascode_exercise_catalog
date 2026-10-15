---
slug: notes-analytics
tags: [if]
difficulty: 2
---
# Avaluació final

Un Institut on s'estudia FP d'Informàtica necessita un programa per a agilitzar les avaluacions. El programa ha de calcular si un alumne aprova una Unitat Formativa a partir dels següents elements:

- Pràctiques entregades.
- Notes dels 3 exàmens parcials.
- Nota de l'examen final.
- Faltes de assistència.

Els requisits per a aprovar la UF són:
a)
Haver entregar al menys els 75% de pràctiques. 
No faltar a més del 20% de les horas de la UF.
Aprovar tots els exàmens parcials.
b)
També es pot aprovar simplement aprovant l'examen final, sempre i quant no s'hagi faltat a més del 20% de les hores de la UF.

## Input

En la primera línia el nombre de practiques totals (T) i el nombre de pràctiques entregades (E)
En la segona línia les notes dels 3 exàmens parcials (P1, P2, P3).
En la tercera línia la nota de l'examen final (EF).
En la quarta línia el nombre total d'hores de la UF (TH) i les hores de faltes d'assistència (FA).

## Output

Aprova | Suspen

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    double t = sc.nextDouble();
    double e = sc.nextDouble();
    double p1 = sc.nextDouble();
    double p2 = sc.nextDouble();
    double p3 = sc.nextDouble();
    double ef = sc.nextDouble();
    double th = sc.nextDouble();
    double fa = sc.nextDouble();

    boolean attendanceOk = fa < th * 0.2;
    boolean practicesOk = (e / t) >= 0.75;
    boolean partialsOk = p1 >= 5 && p2 >= 5 && p3 >= 5;
    boolean finalOk = ef >= 5;

    if (attendanceOk && ((practicesOk && partialsOk) || finalOk)) {
        IO.println("Aprova");
    } else {
        IO.println("Suspen");
    }
}
```

## Tests

### Test
```input
10 5
6 5 0
7
85 14
```
```output
Aprova
```

### Test
```input
10 10
10 10 10
10
85 70
```
```output
Suspen
```

### Test
```input
5 4
5 5 5
3
85 0
```
```output
Aprova
```

### Test
```input
5 3
5 5 5
4
85 5
```
```output
Suspen
```

### Test
```input
5 3
4 9 9
0
85 70
```
```output
Suspen
```

### Test
```input
5 5
5 5 4
4
85 0
```
```output
Suspen
```

### Test
```input
5 5
10 10 10
10
85 17
```
```output
Suspen
```

### Test private
```input
5 5
10 10 10
10
85 18
```
```output
Suspen
```
