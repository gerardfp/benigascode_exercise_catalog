---
slug: d5d1e-creditcard-class-l0
---
# CreditCard

Crea la classe `CreditCard`.

## Input

-

## Output

-

## Plantillas

```java
import java.util.Scanner;


// escriu aqui el codi



public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        CreditCard creditCard = new CreditCard();

        creditCard.holderName = scanner.nextLine();
        creditCard.cardNumber = scanner.nextLong();
        creditCard.accountBalance = scanner.nextFloat();
        creditCard.spendingLimit = scanner.nextFloat();

        System.out.println(creditCard.holderName.toUpperCase());
        System.out.println(String.valueOf(creditCard.cardNumber).replaceAll(".{4}","$0 "));
        System.out.println("Saldo: " + creditCard.accountBalance);
        System.out.println("Limit: " + creditCard.spendingLimit);
    }
}
```

## Tests

### Test
```input
Lola Mento
1234567812345678
2000.5
300
```
```output
LOLA MENTO
1234 5678 1234 5678 
Saldo: 2000.5
Limit: 300.0
```

### Test
```input
Elena Nito
9876543219876543
0
1000000
```
```output
ELENA NITO
9876 5432 1987 6543 
Saldo: 0.0
Limit: 1000000.0
```

### Test
```input
Penelope Luda
1234567891234567
9999999
0.9
```
```output
PENELOPE LUDA
1234 5678 9123 4567 
Saldo: 9999999.0
Limit: 0.9
```
