---
slug: data-de-part
difficulty: 2.0
tags: [conditionals, operators, relational-operators]
---
# Data de caducitat

Estem desenvolupant una aplicació per a dispositius mòbils que ajudi al consumidor a escollir els productes que compra al supermercat. L'usuari escaneja amb la càmera l'etiqueta d'un producte i l'aplicació li dona informació d'aquest producte.

Una de les opcions de l'aplicació és advertir a l'usuari dels productes que han superat la data de caducitat.

## Input

La entrada consta de 6 nombres corresponents a la data de caducitat i la data actual en format `dd/mm/yyyy`.

## Output

S'imprimirà `true` si el producte està caducat, o `false` si no ho està.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int d1 = sc.nextInt();
    int m1 = sc.nextInt();
    int y1 = sc.nextInt();
    int d2 = sc.nextInt();
    int m2 = sc.nextInt();
    int y2 = sc.nextInt();

    int expiry = y1 * 10000 + m1 * 100 + d1;
    int current = y2 * 10000 + m2 * 100 + d2;

    IO.println(current > expiry);
}
```

## Tests

### Test
```input
 1 1 2020
 1 1 2020
```
```output
false
```
#### Explanation
Caduca a l'endemà

### Test
```input
1 1 2030
1 1 2020
```
```output
false
```
#### Explanation
La data de caducitat 1/1/2030 és major que la data actual 1/1/2020

### Test
```input
1 2 2020
1 1 2020
```
```output
false
```

### Test
```input
2 1 2020
1 1 2020
```
```output
false
```

### Test
```input
1 1 2020
2 1 2020
```
```output
true
```

### Test
```input
1 1 2020
1 2 2020
```
```output
true
```

### Test
```input
1 1 2020
1 1 2030
```
```output
true
```

### Test
```input
2 2 2020
1 1 2030
```
```output
true
```

### Test private
```input
1 1 2030
2 2 2020
```
```output
false
```
