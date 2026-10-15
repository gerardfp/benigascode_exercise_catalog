---
slug: black-friday
tags: [loops]
difficulty: 4
---
# Black Friday

Arriba el Black Friday i s'han d'apujar els preus!

Escriu un programa que apuji el preu dels productes un tant per cent determinat.

## Input

L'entrada consisteix en vàries sèries de productes.

Per a cada sèrie s'indica el número de productes $N$, i el tant per cent $T$ que s'han d'apujar els seus preus.

A continuació venen els productes de la sèrie. Per a cada producte s'indica el seu codi $C$ i preu $P$.

- $N$: enter
- $T$: decimal
- $C$: paraula
- $P$: decimal

<p>L'entrada acaba amb dos zeros.</p>

## Output

S'imprimirà cada producte en una nova línia: el codi i el preu apujat (decimal).

**Suggerència per a la solució**

En aquest problema cadrà fer dos bucles niats (un dintre de l'altre). L'exterior es repetirà fins trobar dos zeros a l'entrada. L'interior es repetirà tantes vegades com productes hi hagi en la sèrie.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    while (sc.hasNext()) {
        int n = sc.nextInt();
        float t = sc.nextFloat();
        if (n == 0 && t == 0) break;
        for (int i = 0; i < n; i++) {
            String code = sc.next();
            float p = sc.nextFloat();
            float newP = p + p * t / 100;
            IO.println(code + " " + newP);
        }
    }
}
```

## Tests

### Test
```input
2 5
HW_Hled2 100
KLM_403G 10

3 10
yCat9000 1000
SK8_Plus 500
TK_CPANA 100

0 0
```
```output
HW_Hled2 105.0
KLM_403G 10.5
yCat9000 1100.0
SK8_Plus 550.0
TK_CPANA 110.0
```
#### Explanation
Els primers 2 productes s'apujen un 5%

Els següents 3 productes s'apujen un 10%

### Test
```input
2 15
UE_Boom_2 59
Ezviz_C3T 34.99

3 10
Beko_BSSA2 181.35
HP_M404dn 161.60
Epson_EH_TW610 599

0 0
```
```output
UE_Boom_2 67.85
Ezviz_C3T 40.238503
Beko_BSSA2 199.485
HP_M404dn 177.76001
Epson_EH_TW610 658.9
```
#### Explanation
Els primers 2 productes s'apujen un 15%

Els següents 3 productes s'apujen un 10%

### Test
```input
5 3.33
Mi_TV_4S 349
Mi_Band_4 19
Nest_Mini2 19
IdeaPad_3 649
A51_5G 289

3 7
Cyclone_V10 399
iPhone_11 584
TV_QLED_65 1299

2 13
HW_T530 149
MediaPad_M5 175

0 0
```
```output
Mi_TV_4S 360.6217
Mi_Band_4 19.6327
Nest_Mini2 19.6327
IdeaPad_3 670.6117
A51_5G 298.6237
Cyclone_V10 426.93
iPhone_11 624.88
TV_QLED_65 1389.93
HW_T530 168.37
MediaPad_M5 197.75
```
#### Explanation
Els primers 5 productes s'apujen un 3,33%

Els següents 3 productes s'apujen un 7%

Els següents 2 productes s'apujen un 13%

### Test
```input
2 5
HW_Hled2 100
KLM_403G 10

3 10
yCat9000 1000
SK8_Plus 500
TK_CPANA 100

2 15
UE_Boom_2 59
Ezviz_C3T 34.99

3 10
Beko_BSSA2 181.35
HP_M404dn 161.60
Epson_EH_TW610 599

5 3.33
Mi_TV_4S 349
Mi_Band_4 19
Nest_Mini2 19
IdeaPad_3 649
A51_5G 289

3 7
Cyclone_V10 399
iPhone_11 584
TV_QLED_65 1299

2 13
HW_T530 149
MediaPad_M5 175

0 0
```
```output
HW_Hled2 105.0
KLM_403G 10.5
yCat9000 1100.0
SK8_Plus 550.0
TK_CPANA 110.0
UE_Boom_2 67.85
Ezviz_C3T 40.238503
Beko_BSSA2 199.485
HP_M404dn 177.76001
Epson_EH_TW610 658.9
Mi_TV_4S 360.6217
Mi_Band_4 19.6327
Nest_Mini2 19.6327
IdeaPad_3 670.6117
A51_5G 298.6237
Cyclone_V10 426.93
iPhone_11 624.88
TV_QLED_65 1389.93
HW_T530 168.37
MediaPad_M5 197.75
```

### Test private
```input
3 10
yCat9000 1000
SK8_Plus 500
TK_CPANA 100

0 0
```
```output
yCat9000 1100.0
SK8_Plus 550.0
TK_CPANA 110.0
```
