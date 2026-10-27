---
slug: class-comptecorrent
difficulty: 1.0
tags: [class]
---
# Definir la classe CompteCorrent

Defineix una classe anomenada `CompteCorrent`. Ha de tenir tres camps: un enter `saldo`, un String `nomPropietari`, i un boolean `bloquejada`.

## Plantillas

```java

// Defineix aqui la classe

public class Main {
    public static void main(String[] args) {
		CompteCorrent cc = new CompteCorrent();
      
      	cc.saldo = 999.9f;
        cc.nomPropietari = "Jeff Bezos";
      	cc.bloquejada = false;
    }
}
```

## Solutions

```java
class CompteCorrent {
    double saldo;
    String nomPropietari;
    boolean bloquejada;
}

void main() {
    CompteCorrent cc = new CompteCorrent();
    cc.saldo = 999.9f;
    cc.nomPropietari = "Jeff Bezos";
    cc.bloquejada = false;
}
```

## Tests

### Test
```input
```
```output
```
