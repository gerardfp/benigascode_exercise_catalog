---
slug: esquemes-cerca-lineal-prefix
difficulty: 3.0
tags: [arrays, strings, loops, for-loop, search]
---
# Cerca lineal: paraula amb prefix

Donada una seqüència de $N$ cadenes de text i un caràcter $C$, cerca i imprimeix la primera cadena que comenci pel caràcter $C$. Si cap cadena comença per aquest caràcter, imprimeix `NO TROBAT`.

## Entrada

A la primera línia hi ha el número $N$.

A continuació venen les $N$ cadenes de text, cadascuna en una línia.

A l'última línia hi ha el caràcter $C$.

## Salida

Imprimeix la primera cadena que comença per $C$, o `NO TROBAT` si no n'hi ha cap.

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    String[] words = new String[n];
    for (int i = 0; i < n; i++) words[i] = sc.next();
    String c = sc.next();

    String resultat = "NO TROBAT";
    for (int i = 0; i < n; i++) {
        if (words[i].startsWith(c)) {
            resultat = words[i];
            break;
        }
    }
    IO.println(resultat);
}
```

## Tests

### Test
```input
4
blau
verd
groc
vermell
v
```
```output
verd
```

### Test
```input
3
alfa
beta
gamma
z
```
```output
NO TROBAT
```

### Test
```input
3
sol
sopa
sort
s
```
```output
sol
```

### Test
```input
1
java
j
```
```output
java
```
