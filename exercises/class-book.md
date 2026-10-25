---
slug: class-book
difficulty: 5.0
tags: [class]
---
# Class Book

Defineix la classe `Book`. 

Ha de contenir tres camps: camp string `title`, camp enter `yearOfPublishing` i camp booleà `isAvailable`.

## Plantillas

```java
// crea la classe aqui

public class Main {

    public static void main(String[] args) {
      	Book book = new Book();
      
      	book.title = "Through the looking glass";
      	book.yearOfPublishing = 1871;
      	book.isAvailable = true;
      
      	System.out.println(book.title);
      	System.out.println(book.yearOfPublishing);
      	System.out.println(book.isAvailable);
    }
}
```

## Solutions

```java
class Book {
    String title;
    int yearOfPublishing;
    boolean isAvailable;
}

void main() {
    Book book = new Book();

    book.title = "Through the looking glass";
    book.yearOfPublishing = 1871;
    book.isAvailable = true;

    IO.println(book.title);
    IO.println(book.yearOfPublishing);
    IO.println(book.isAvailable);
}
```

## Tests

### Test
```input
```
```output
Through the looking glass
1871
true
```
