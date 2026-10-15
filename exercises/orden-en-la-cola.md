---
slug: orden-en-la-cola
tags: [arrays, esquemes]
difficulty: 3
---
# Orden en la cola

![image](assets/aafec-orden-en-la-cola-img0.png)

Para entrar en un sitio hay que coger un ticket con un número y esperar en la cola.
Hay gente que se cansa de esperar y abandona la cola. Y hay otros que tratan de colarse…

Cuando a uno le toca entrar y tiene un número mayor del que tocaría, **la única forma de saber si realmente se ha colado es ver si de los que van por detrás de él en la cola hay alguien que tiene un número más bajo**.

Se desea hacer un programa que diga, por cada persona que hay en la cola, por delante de cuántas personas se han colado.

## Input

El primer numero $N$ indica la cantidad de gente que hay en la cola.

A continuación vienen los $N$ números de ticket de cada persona.

## Output

Se imprimirá (en orden de aparición en la cola) el número de ticket de las personas que se hayan colado, y por delante de cuántas personas se ha colado. Con el siguiente formato:

```
La persona con el ticket T se ha colado por delante de X personas.
```

Si no se ha colado nadie se escribirá `COLA EN ORDEN`.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int n = sc.nextInt();
    int[] a = new int[n];
    for (int i = 0; i < n; i++) {
        a[i] = sc.nextInt();
    }
    boolean colado = false;
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[i]) {
                count++;
            }
        }
        if (count > 0) {
            colado = true;
            IO.println("La persona con el ticket " + a[i] + " se ha colado por delante de " + count + " personas.");
        }
    }
    if (!colado) {
        IO.println("COLA EN ORDEN");
    }
}
```

## Tests

### Test
```input
5
1 4 3 2 5
```
```output
La persona con el ticket 4 se ha colado por delante de 2 personas.
La persona con el ticket 3 se ha colado por delante de 1 personas.
```

### Test
```input
10
1 2 5 6 3 4 10 14 13 12
```
```output
La persona con el ticket 5 se ha colado por delante de 2 personas.
La persona con el ticket 6 se ha colado por delante de 2 personas.
La persona con el ticket 14 se ha colado por delante de 2 personas.
La persona con el ticket 13 se ha colado por delante de 1 personas.
```

### Test
```input
6
23 2 7 5 24 25
```
```output
La persona con el ticket 23 se ha colado por delante de 3 personas.
La persona con el ticket 7 se ha colado por delante de 1 personas.
```

### Test
```input
4
23 25 24 5
```
```output
La persona con el ticket 23 se ha colado por delante de 1 personas.
La persona con el ticket 25 se ha colado por delante de 2 personas.
La persona con el ticket 24 se ha colado por delante de 1 personas.
```

### Test
```input
5
7 12 13 17 23
```
```output
COLA EN ORDEN
```

### Test private
```input
7
1 5 8 27 33 36 41
```
```output
COLA EN ORDEN
```
