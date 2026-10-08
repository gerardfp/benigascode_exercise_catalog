---
slug: c6-l2-4-butlleti-de-notes
---
# Butlletí de notes

Afegeix els camps i mètodes que falten a la classe ReportCard.

*La variable  indica el pes de l'activitat en la nota final*

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

class Grade {
    String name;
    float grade;
    float weight;

    Grade(String n, float g, float w) {
        name = n;
        grade = g;
        weight = w;
    }
}

class ReportCard {
  
    ReportCard(int numGrades){
        grades = new Grade[numGrades];
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
	    ReportCard reportCard = new ReportCard(n);

        for (int i = 0; i < n; i++) {
            String assignment = scanner.next();
            float grade = scanner.nextFloat();
            float weight = scanner.nextFloat();

            reportCard.grades[i] = new Grade(assignment, grade, weight);
        }

        reportCard.calculateAverageGrade();

        System.out.format("Average Grade: %.2f%n", reportCard.averageGrade);
    }
}
```

## Tests

### Test
```input
3
Practiques 9 20
Exercicis 8 30
Examen 5 50
```
```output
Average Grade: 6.70
```

### Test
```input
2
Projecte 10 50
Examen 0 50
```
```output
Average Grade: 5.00
```

### Test
```input
3
Practiques 9 20
Exercicis 8 30
Examen 5 50
```
```output
Average Grade: 6.70
```

### Test
```input
5
Projecte 8 30
Practica1 9 10
Practica2 7 10
Practica3 6 10
Examen 5 40
```
```output
Average Grade: 6.60
```

### Test
```input
3
Examen1 5 25
Examen2 6.7 25
Examen3 10 50
```
```output
Average Grade: 7.93
```

### Test
```input
1
Examen 7.75 100
```
```output
Average Grade: 7.75
```
