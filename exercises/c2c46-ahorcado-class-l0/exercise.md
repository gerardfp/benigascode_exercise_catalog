---
slug: c2c46-ahorcado-class-l0
tags: [classes]
---
# Ahorcado

Crea la clase `Ahorcado`

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


// escriu el codi aqui

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Ahorcado ahorcado = new Ahorcado(scanner.next());

        while(ahorcado.fallos < 6 && !ahorcado.completado){
            for (int i = 0; i < ahorcado.descubierta.length; i++) {
                System.out.print(" " + ahorcado.descubierta[i] + " ");
            }
            System.out.println();

            char letra = scanner.next().charAt(0);

            ahorcado.completado = true;
            boolean estaLaLetra = false;
            for (int i = 0; i < ahorcado.palabra.length(); i++) {
                if(ahorcado.palabra.charAt(i) == letra){
                    ahorcado.descubierta[i] = letra;
                    estaLaLetra = true;
                }
                if(ahorcado.descubierta[i] == '_'){
                    ahorcado.completado = false;
                }
            }
            if(!estaLaLetra){
                ahorcado.fallos++;
            }

            if(ahorcado.fallos == 5)      System.out.println("\n  __    \n |  |   \n |  0   \n | /|\\ \n | /    \n |____    \n");
            else if(ahorcado.fallos == 4) System.out.println("\n  __    \n |  |   \n |  0   \n | /|\\ \n |      \n |____    \n");
            else if(ahorcado.fallos == 3) System.out.println("\n  __    \n |  |   \n |  0   \n | /|   \n |      \n |____    \n");
            else if(ahorcado.fallos == 2) System.out.println("\n  __    \n |  |   \n |  0   \n | /    \n |      \n |____    \n");
            else if(ahorcado.fallos == 1) System.out.println("\n  __    \n |  |   \n |  0   \n |      \n |      \n |____    \n");
            else if(ahorcado.fallos == 0) System.out.println("\n  __    \n |  |   \n |      \n |      \n |      \n |____    \n");
        }

        if(ahorcado.fallos == 6) System.out.println("\n  __    \n |  |   \n |  0   \n | /|\\ \n | / \\ \n |____    \n");
        else System.out.println("YOU WIN");
    }
}
```

## Tests

### Test 25
```input
hola
h
o
l
a
```
```output
 _  _  _  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 h  _  _  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 h  o  _  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 h  o  l  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

YOU WIN
```

### Test 25
```input
java
j
a
v
```
```output
 _  _  _  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 j  _  _  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 j  a  _  a 

  __    
 |  |   
 |      
 |      
 |      
 |____    

YOU WIN
```

### Test private 25
```input
constructor
c o n s t r u
```
```output
 _  _  _  _  _  _  _  _  _  _  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 c  _  _  _  _  _  _  c  _  _  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 c  o  _  _  _  _  _  c  _  o  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 c  o  n  _  _  _  _  c  _  o  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 c  o  n  s  _  _  _  c  _  o  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 c  o  n  s  t  _  _  c  t  o  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 c  o  n  s  t  r  _  c  t  o  r 

  __    
 |  |   
 |      
 |      
 |      
 |____    

YOU WIN
```

### Test private 25
```input
classe
c l a e z x v b n m
```
```output
 _  _  _  _  _  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 c  _  _  _  _  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 c  l  _  _  _  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 c  l  a  _  _  _ 

  __    
 |  |   
 |      
 |      
 |      
 |____    

 c  l  a  _  _  e 

  __    
 |  |   
 |  0   
 |      
 |      
 |____    

 c  l  a  _  _  e 

  __    
 |  |   
 |  0   
 | /    
 |      
 |____    

 c  l  a  _  _  e 

  __    
 |  |   
 |  0   
 | /|   
 |      
 |____    

 c  l  a  _  _  e 

  __    
 |  |   
 |  0   
 | /|\ 
 |      
 |____    

 c  l  a  _  _  e 

  __    
 |  |   
 |  0   
 | /|\ 
 | /    
 |____    

 c  l  a  _  _  e 

  __    
 |  |   
 |  0   
 | /|\ 
 | / \ 
 |____  
```
