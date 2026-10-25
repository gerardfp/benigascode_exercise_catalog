---
slug: trendingtopic
difficulty: 5.0
tags: [arrays, strings, counters, sorting]
---
# TrendingTopic

Una forma de veure la popularitat dels llenguatges de programació, es veure els cops que es mencionen a les xarxes socials.

A partir d'una sèrie de missatges publicats, volem fer un ranking dels hashtags més utilitzats.

## Input

En primer lloc ve el nombre de missatges. 

A continuació venen els missatges.

Cada missatge està encabit dintre d'unes claus `{}`

El missatge pot ocupar vàries línies, però totes elles tenen 1 grau de tabulació.

## Output

S'imprimirà la llista de Hashtags i les vegades que apareix als missatges

## Solutions

```java
void main() {
    Scanner sc = new Scanner(System.in);
    String[] tags = new String[1000];
    int[] counts = new int[1000];
    int tagCount = 0;

    while (sc.hasNext()) {
        String token = sc.next();
        int idx = 0;
        while (idx < token.length()) {
            int hashIdx = -1;
            for (int i = idx; i < token.length(); i++) {
                if (token.charAt(i) == '#') {
                    hashIdx = i;
                    break;
                }
            }
            if (hashIdx == -1) {
                break;
            }
            int end = hashIdx + 1;
            while (end < token.length()) {
                char c = token.charAt(end);
                if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {
                    end++;
                } else {
                    break;
                }
            }
            if (end > hashIdx + 1) {
                String tag = token.substring(hashIdx, end).toLowerCase();
                int found = -1;
                for (int i = 0; i < tagCount; i++) {
                    if (tags[i].equals(tag)) {
                        found = i;
                        break;
                    }
                }
                if (found != -1) {
                    counts[found]++;
                } else {
                    tags[tagCount] = tag;
                    counts[tagCount] = 1;
                    tagCount++;
                }
            }
            idx = end;
        }
    }

    // Stable sort descending by count
    for (int i = 0; i < tagCount - 1; i++) {
        for (int j = 0; j < tagCount - 1 - i; j++) {
            if (counts[j] < counts[j + 1]) {
                int tempC = counts[j];
                counts[j] = counts[j + 1];
                counts[j + 1] = tempC;

                String tempT = tags[j];
                tags[j] = tags[j + 1];
                tags[j + 1] = tempT;
            }
        }
    }

    for (int i = 0; i < tagCount; i++) {
        IO.println(tags[i] + " " + counts[i]);
    }
}
```

## Tests

### Test
```input
4
{
    #Java
}
{
    #Python #Java
}
{
    #Java
}
{
    #Python
}
```
```output
#java 3
#python 2
```

### Test
```input
4
{
    #Java
}
{
    #Python #Java
}
{
    #Java
}
{
    #Python
}
```
```output
#java 3
#python 2
```

### Test
```input
4
{
    The #Java world
}
{
    Programming in #Python #Java
}
{
    Everybody loves #PHP
}
{
    #Python is easy, #Java mmmm
}
```
```output
#java 3
#python 2
#php 1
```

### Test
```input
4
{
    What if... Oh, it actually works. #javascript
}
{
    #Java: New Developments & Features.
}
{
    Anyone out there know if there are any good books on #java?
}
{
    All computers wait at same speed #java, #JavaScript
}
```
```output
#java 3
#javascript 2
```

### Test
```input
6
{
    Everything you need to know about the newest garbage collectors in #Java.
}
{
    #python:  The boolean values False and True are equal to zero and one.
}
{
    Write everything in #JavaScript?
}
{
    Yet Another #javascript Framework
}
{
    got photo bombed by Guido van Rossum creator of #python
}
{
    Tonight I manipulated the DOM to add elements to a webpage using #javascript!
    Mind freaking blown!
}
```
```output
#javascript 3
#python 2
#java 1
```

### Test private
```input
40
{
    #Java: New Developments & Features. #Java is growing and changing quickly,
    and there's a lot to keep up with.
}
{
    Everything you need to know about the newest garbage collectors in #Java.
}
{
    For #Java developers, learning Spring Boot is the first step to learning to developer
    applications for the cloud.
}
{
    A Reading List for #Java Programmers
}
{
    I used the last two days to complete the JUnit tutorial. #java
}
{
    Starting with my first #Java app
}
{
    Now I know #Java
}
{
    #Python is the most popular language in 2019
}
{
    How To: Configure #Python Virtual Environment
}
{
    console.log("good morning"); #JavaScript
    System.out.println("good morning"); #JAVA
    print "good morning"; #Python
    echo "good morning"; #PHP
    Good morning. #Human
}
{
    1 Minute #Python - String Indexing: Positive Indexes Enjoy! :)
}
{
    Creating a Neural Network from Scratch in #Python
}
{
    #python tip:  The boolean values False and True are equal to zero and one.
}
{
    got photo bombed by Guido van Rossum creator of #python
}
{
    Tonight I manipulated the DOM to add elements to a webpage using #javascript!
    Mind freaking blown!
}
{
    Today was spent going over regular expressions in #JavaScript
}
{
    I started learning React before having a solid grasp of #JavaScript and I regretted it.
}
{
    What if... Oh, it actually works. #javascript
}
{
    Write everything in #JavaScript
}
{
    This is going to change my entire workflow of building #javascript
}
{
    Yet Another #javascript Framework
}
{
    Time to relax after work and not think about #JavaScript Errors.
}
{
    if an image failed to load, show a customized broken image #javascript
}
{
    all about Machine Learning with #JavaScript
}
{
    Can you spot the vulnerability? #PHP
}
{
    Improve the security of your #PHP app
}
{
    <? this tweet is not parsed as #PHP anymore: get over it
}
{
    Vue and Laravel To-Do App - Restful API Project #PHP
}
{
    What #PHP version are you running?
}
{
    Learn to Create a #PHP MVC Framework
}
{
    That #PHP clip too crazy!!!
}
{
    Hello, naming convention:
    camelCase
    kebab-case
    PascalCase
    snake_case
    #java #javascript #python #CSharp #PHP
}
{
    Languages to learn this year;
    #Python #JavaScript #PHP #CSharp
    Maybe;
    #Java
}
{
    Looks like PAUSE has taken a pause. #Java
}
{
    Which programming language would you recommend to start learning first?
    #Python #Java #CSharp #PHP #Javascript
}
{
    All computers wait at same speed #CSharp
}
{
    Do #CSharp developers have 20/20 vision?
}
{
    Anyone out there know if there are any good books on #CSharp?
}
{
    Wish I could declare local variables as `readonly` in #csharp so I can't accidentally overwrite them.
}
{
    It doesn't seem to be #csharp
}
```
```output
#javascript 14
#java 13
#php 11
#python 10
#csharp 8
#human 1
```
