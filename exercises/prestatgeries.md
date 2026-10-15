---
slug: prestatgeries
tags: [operators, booleans, relational-operators]
difficulty: 1
---
# Llibres i prestatgeries

Per a endreçar els seus llibres, Miquel ha comprat unes prestatgeries.
Cada prestatgeria té un nombre de prestatges, i a cada prestatge hi caben una quantitat de llibres determinada.
En Miquel vol saber si ha comprat suficients prestatges.

## Input

El primer nombre $P$ indica la quanitat de prestatgeries.

El segon nombre $G$ indica el nombre de prestatges que té cada prestatgeria.

El tercer nombre $L$ indica el nombre de llibres que hi caben a cada prestatgeria.

L'últim nombre $N$ indica la quantitat de llibres que té en Miquel.

## Output

`true` | `false`

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int p = sc.nextInt();
    int g = sc.nextInt();
    int l = sc.nextInt();
    int n = sc.nextInt();

    IO.println(p * g * l >= n);
}
```

## Tests

### Test
```input
1 1 1 1
```
```output
true
```
#### Explanation
1 prestatgeria X 1 prestatge X 1 llibre = 1 llibre de capacitat

La quantitat de llibres és 1, per tant sí que caben.

### Test
```input
2 4 10 60
```
```output
true
```
#### Explanation
2 prestatgeries X 4 prestatges X 10 llibres = 80 llibres de capacitat

La quantitat de llibres és 60, per tant sí que caben

### Test
```input
10 3 5 200
```
```output
false
```
#### Explanation
10 prestatgeries X 3 prestatges X 5 llibres = 150 llibres de capacitat

La quantitat de llibres és 200, per tant no caben tots.

### Test private
```input
1 5 10 50
```
```output
true
```
