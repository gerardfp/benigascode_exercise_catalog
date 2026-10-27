---
slug: desglose-de-cantidades-en-monedas
difficulty: 4.0
tags: [operators, arithmetic, modulo, greedy]
---
# Desglossament en monedes

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 240">
  <title>Cinco monedas: 500, 100, 50, 5 y 1</title>
  <defs><linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fff0a6"/>      <stop offset="45%" stop-color="#e4b94f"/>      <stop offset="100%" stop-color="#b78325"/>    </linearGradient>    <linearGradient id="silver" x1="0" y1="0" x2="1" y2="1">      <stop offset="0%" stop-color="#ffffff"/>      <stop offset="50%" stop-color="#d9dee3"/>      <stop offset="100%" stop-color="#a6afb8"/>    </linearGradient>  </defs>
  <rect width="100%" height="100%" fill="#ffffff"/>
  <g font-family="Arial, Helvetica, sans-serif" text-anchor="middle" font-weight="700">
    <g transform="translate(110 120)">
      <circle r="76" fill="url(#gold)" stroke="#93671b" stroke-width="5"/>
      <circle r="64" fill="none" stroke="#fff0a6" stroke-width="3"/>
      <circle r="55" fill="none" stroke="#a77720" stroke-width="2" stroke-dasharray="3 6"/>
      <text y="13" font-size="42" fill="#684716">500</text>
    </g>
    <g transform="translate(305 120)">
      <circle r="76" fill="url(#silver)" stroke="#7d8790" stroke-width="5"/>
      <circle r="64" fill="none" stroke="#ffffff" stroke-width="3"/>
      <circle r="55" fill="none" stroke="#929ca5" stroke-width="2" stroke-dasharray="3 6"/>
      <text y="13" font-size="42" fill="#414a52">100</text>
    </g>
    <g transform="translate(500 120)">
      <circle r="76" fill="url(#gold)" stroke="#93671b" stroke-width="5"/>
      <circle r="64" fill="none" stroke="#fff0a6" stroke-width="3"/>
      <circle r="55" fill="none" stroke="#a77720" stroke-width="2" stroke-dasharray="3 6"/>
      <text y="13" font-size="42" fill="#684716">50</text>
    </g>
    <g transform="translate(695 120)">
      <circle r="76" fill="url(#silver)" stroke="#7d8790" stroke-width="5"/>
      <circle r="64" fill="none" stroke="#ffffff" stroke-width="3"/>
      <circle r="55" fill="none" stroke="#929ca5" stroke-width="2" stroke-dasharray="3 6"/>
      <text y="13" font-size="42" fill="#414a52">5</text>
    </g>
    <g transform="translate(890 120)">
      <circle r="76" fill="url(#gold)" stroke="#93671b" stroke-width="5"/>
      <circle r="64" fill="none" stroke="#fff0a6" stroke-width="3"/>
      <circle r="55" fill="none" stroke="#a77720" stroke-width="2" stroke-dasharray="3 6"/>
      <text y="13" font-size="42" fill="#684716">1</text>
    </g>
  </g>
</svg>

Calcula el desglossament d'una quantitat en monedes, de tal forma que es minimitze el número de monedes utilitzades en el desglossament.

Les monedes que es poden usar per al desglossament són: 500, 100, 50, 5, 1

## Input

Un número enter indicant la quantitat a desglossar

## Output

Imprimeix el número utlitzat de cada moneda utilitzat en el desglossament, ordenades per valor.

Si una moneda no s'utilitza en el desglossament, no s'ha d'imprimir.

Si solament s'utilitza 1 moneda en el desglossament, s'ha d'imprimir "moneda" en singular.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextInt()) return;
    int amount = sc.nextInt();
    int[] coins = {500, 100, 50, 5, 1};
    for (int coin : coins) {
        int count = amount / coin;
        amount %= coin;
        if (count == 1) {
            IO.println("1 moneda de " + coin);
        } else if (count > 1) {
            IO.println(count + " monedes de " + coin);
        }
    }
}
```

## Tests

### Test
```input
649
```
```output
1 moneda de 500
1 moneda de 100
9 monedes de 5
4 monedes de 1
```

### Test
```input
2026
```
```output
4 monedes de 500
5 monedes de 5
1 moneda de 1
```

### Test
```input
656
```
```output
1 moneda de 500
1 moneda de 100
1 moneda de 50
1 moneda de 5
1 moneda de 1
```

### Test private
```input
657
```
```output
1 moneda de 500
1 moneda de 100
1 moneda de 50
1 moneda de 5
2 monedes de 1
```
