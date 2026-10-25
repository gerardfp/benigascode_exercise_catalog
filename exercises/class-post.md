---
slug: class-post
difficulty: 3.0
tags: [class]
---
# Post

Implementa el constructor de la classe Post.

## Plantillas

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Post {
    String user;
    String content;
    int favs;
    int retweets;

    // escriu el codi aqui
}

public class Main {

    public static void main(String[] args) {
        Post post1 = new Post("@realdonaltrump", "Make America Great Again #MAGA", 10000000, 2000000);
        Post post2 = new Post("@realdonaltrump", "You are fake news", 325646, 5986587);
        Post post3 = new Post("@realdonaltrump", "Global warming is a HOAX", 1000, 200);

        String format = "------------------------------------\n| %-32s |\n| %-32s |\n| <3 %-12d   & %-12d |\n------------------------------------\n";
        System.out.format(format, post1.user, post1.content, post1.retweets, post1.favs);
        System.out.format(format, post2.user, post2.content, post2.retweets, post2.favs);
        System.out.format(format, post3.user, post3.content, post3.retweets, post3.favs);
    }
}
```

## Solutions

```java
class Post {
    String user;
    String content;
    int favs;
    int retweets;

    Post(String user, String content, int favs, int retweets) {
        this.user = user;
        this.content = content;
        this.favs = favs;
        this.retweets = retweets;
    }
}

void main() {
    Post post1 = new Post("@realdonaltrump", "Make America Great Again #MAGA", 10000000, 2000000);
    Post post2 = new Post("@realdonaltrump", "You are fake news", 325646, 5986587);
    Post post3 = new Post("@realdonaltrump", "Global warming is a HOAX", 1000, 200);

    String format = "------------------------------------\n| %-32s |\n| %-32s |\n| <3 %-12d   & %-12d |\n------------------------------------\n";
    IO.print(format.formatted(post1.user, post1.content, post1.retweets, post1.favs));
    IO.print(format.formatted(post2.user, post2.content, post2.retweets, post2.favs));
    IO.print(format.formatted(post3.user, post3.content, post3.retweets, post3.favs));
}
```

## Tests

### Test
```input
```
```output
------------------------------------
| @realdonaltrump                  |
| Make America Great Again #MAGA   |
| <3 2000000        & 10000000     |
------------------------------------
------------------------------------
| @realdonaltrump                  |
| You are fake news                |
| <3 5986587        & 325646       |
------------------------------------
------------------------------------
| @realdonaltrump                  |
| Global warming is a HOAX         |
| <3 200            & 1000         |
------------------------------------
```
