---
slug: c4-l1-2-apunts
tags: [arrays]
---
# Apunts

![image](1575464228-fd15617696-papers-flying-graphic-1024x767.jpg)

En Joan anava a l'institut en monopatí i portava la motxilla oberta... tots els apunts de programació li han sortit volant.

Per sort, tenia les pàgines numerades, pots ajudar-li a ordenar-los?

## Input

El primer nombre <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> indica la quantitat de pàgines.

A continuació venen les pàgines. Cada pàgina va en una línia: en primer lloc el número de pàgina, i després el contingut de la pàgina.

## Output

S'imprimiràn totes les pàgines ordenades segons el número de pàgina.

## Tests

### Test
```input
4
3 La sentencia if tiene esta forma: if {} else {}
2 Los operadores booleanos son OR || y AND &&
1 Los datos primitivos en Java son: byte, short, int, long, float, double, boolean y char
4 La sentencia for tiene esta forma: for(;;) {}
```
```output
1 Los datos primitivos en Java son: byte, short, int, long, float, double, boolean y char
2 Los operadores booleanos son OR || y AND &&
3 La sentencia if tiene esta forma: if {} else {}
4 La sentencia for tiene esta forma: for(;;) {}
```

### Test
```input
4
2 Los operadores booleanos son OR || y AND &&
1 Los datos primitivos en Java son: byte, short, int, long, float, double, boolean y char
4 La sentencia for tiene esta forma: for(;;) {}
3 La sentencia if tiene esta forma: if {} else {}
```
```output
1 Los datos primitivos en Java son: byte, short, int, long, float, double, boolean y char
2 Los operadores booleanos son OR || y AND &&
3 La sentencia if tiene esta forma: if {} else {}
4 La sentencia for tiene esta forma: for(;;) {}
```

### Test
```input
5
5 La sentencia while tiene esta sintaxis: while(){}
2 Los operadores booleanos son OR || y AND &&
1 Los datos primitivos en Java son: byte, short, int, long, float, double, boolean y char
4 La sentencia for tiene esta sintaxis: for(;;) {}
3 La sentencia if tiene esta sintaxis: if {} else {}
```
```output
1 Los datos primitivos en Java son: byte, short, int, long, float, double, boolean y char
2 Los operadores booleanos son OR || y AND &&
3 La sentencia if tiene esta sintaxis: if {} else {}
4 La sentencia for tiene esta sintaxis: for(;;) {}
5 La sentencia while tiene esta sintaxis: while(){}
```

### Test private
```input
10
7 Kotlin es un lenguaje que corre sobre la maquina virtual Java
1 Java es un lenguaje de programacion y una plataforma informatica
3 Las aplicaciones Java son compiladas a bytecode
8 La ultima version estable de Java es la 12
10 0.1 + 0.2 != 0.3
5 Java es un lenguaje Orientado a Objetos
6 La sintaxis de Java esta inspirada en C y C++
2 Java fue originalmente disenado por James Gosling
4 El compilador de Java es javac y el interprete java
9 La mascota de Java se llama Duke
```
```output
1 Java es un lenguaje de programacion y una plataforma informatica
2 Java fue originalmente disenado por James Gosling
3 Las aplicaciones Java son compiladas a bytecode
4 El compilador de Java es javac y el interprete java
5 Java es un lenguaje Orientado a Objetos
6 La sintaxis de Java esta inspirada en C y C++
7 Kotlin es un lenguaje que corre sobre la maquina virtual Java
8 La ultima version estable de Java es la 12
9 La mascota de Java se llama Duke
10 0.1 + 0.2 != 0.3
```
