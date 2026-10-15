---
slug: diccionari
tags: [arrays, strings, io, search]
difficulty: 3
---
# Diccionari

Quan programem jocs que utilitzen paraules (com l'Scrabble, Sopa de lletres, Penjat, ... ), ens pot ser molt útil tenir una llista amb totes les possibles paraules.

A Linux, tenim l'arxiu /usr/share/dict amb una completa llista de paraules, i podríem progamar un mètode per a cercar-hi una paraula.

També disposem del recurs de la metaprogramació, que consisteix en programes que escriuen altres programes. Fent ús d'aquesta eina, podem fer un programa que generi un programa en Java que contingui un array amb les paraules del diccionari.

## Input

Una llista de paraules, separades per salts de línia.

La llista de paraules acaba amb '**END**'

## Output

Es generarà una programa Java amb una classe anomenada "Dictionari", que inicialitzi un array d'strings amb les paraules, anomenat "words".

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    String[] words = new String[10000];
    int n = 0;
    while (sc.hasNext()) {
        String line = sc.next();
        if (line.equals("__END__")) {
            break;
        }
        words[n++] = line;
    }
    IO.println("class Dictionari {");
    IO.println("    String[] words = {");
    for (int i = 0; i < n; i++) {
        if (i < n - 1) {
            IO.println("        \"" + words[i] + "\",");
        } else {
            IO.println("        \"" + words[i] + "\"");
        }
    }
    IO.println("    };");
    IO.println("}");
}
```

## Tests

### Test
```input
hola
adeu
mama
__END__
```
```output
class Dictionari {
    String[] words = {
        "hola",
        "adeu",
        "mama"
    };
}
```

### Test
```input
una
llista
de
paraules
__END__
```
```output
class Dictionari {
    String[] words = {
        "una",
        "llista",
        "de",
        "paraules"
    };
}
```

### Test
```input
festival
triangle
municipi
batalla
voleibol
__END__
```
```output
class Dictionari {
    String[] words = {
        "festival",
        "triangle",
        "municipi",
        "batalla",
        "voleibol"
    };
}
```

### Test
```input
metaprogramming
__END__
```
```output
class Dictionari {
    String[] words = {
        "metaprogramming"
    };
}
```

### Test private
```input
metaprogramming
rocks
__END__
```
```output
class Dictionari {
    String[] words = {
        "metaprogramming",
        "rocks"
    };
}
```
