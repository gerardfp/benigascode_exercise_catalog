---
slug: b46d0-postsstream-class-l0
---
# PostsStream

Crea els objectes necessaris.

## Input

-

## Output

-

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Author {
    String name;
    String photoURL;
}

class Post {
    Author author;
    String content;
}

class Stream {
    Post[] posts;
}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int nPosts = scanner.nextInt();

        Stream stream = new Stream();

        stream.posts = new Post[nPosts];

        for (int i = 0; i < nPosts; i++) {

            // escriu aqui el codi

            stream.posts[i].author.name = scanner.next();
            stream.posts[i].author.photoURL = scanner.next();
            stream.posts[i].content = scanner.next() + scanner.nextLine();
        }

        for (int i = 0; i < nPosts; i++) {
            System.out.println(stream.posts[i].author.name);
            System.out.println(stream.posts[i].content);
            System.out.println("------------------------------");
        }
    }
}
```

## Tests

### Test 50
```input
3
@popeye http://img.io/1234.jpg Hola que tal
@olivia http://img.io/facb.jpg Adios adios
@brutus http://img.io/9k8h.jpg Hasta luego
```
```output
@popeye
Hola que tal
------------------------------
@olivia
Adios adios
------------------------------
@brutus
Hasta luego
------------------------------
```

### Test private 50
```input
2
@user_one null Blank message
@user_two null Empty message
```
```output
@user_one
Blank message
------------------------------
@user_two
Empty message
------------------------------
```
