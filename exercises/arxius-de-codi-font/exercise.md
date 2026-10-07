---
slug: arxius-de-codi-font
---
# Arxius de codi font

![image](1601159416-d284b37cf1-srctypes.png)

Cada llenguatge de programació té les seves pròpies extensions per als arxius de codi font.

Els de Java són `.java`, els JavaScript són `.js`, en Python és `py`, en C++ és `.cpp` ...

Donada una llista d'arxius amb el nom i tipus, imprimeix la llista en l'ordre invers, i les columnes intercanviades (primer tipus i després nom).

## Input

L'entrada consta de **quatre** línies.

En cada línia hi ha una paraula que es el  de l'arxiu (amb l'extensió inclosa), y la resta de la línia és el  d'arxiu.

## Output

S'imprimirà cada arxiu en una línia, primer el  i després el

## Plantillas

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
      	Scanner scanner = new Scanner(System.in);
      
      	
    }
}
```

## Tests

### Test 33.33
```input
main.cpp Archivo C++
Main.java Archivo Java
program.py Archivo Python
script.js Archivo JavaScript
```
```output
Archivo JavaScript script.js 
Archivo Python program.py 
Archivo Java Main.java 
Archivo C++ main.cpp 
```

### Test private 33.33
```input
index.php Archivo PHP
sample.cs Archivo C#
app.swift Archivo Swift
MainActivity.kt Archivo Kotlin
```
```output
Archivo Kotlin MainActivity.kt
Archivo Swift app.swift
Archivo C# sample.cs
Archivo PHP index.php
```

### Test private 33.34
```input
index.ts Archivo TypeScript
out.asm Archivo assembler
query.sql Archivo Structured Query Language
main.rs Archivo Rust
```
```output
Archivo Rust main.rs
Archivo Structured Query Language query.sql
Archivo assembler out.asm
Archivo TypeScript index.ts
```
