---
slug: arrodonir-la-nota
tags: [casting, operators]
---
# Arrodonir la nota

Al butlletí de notes no es poden posar notes amb decimals, així que el professor ha decidit arrodonir-les. Si els decimals estan per sota de 0.5 es trunca la nota (es lleven els decimals), però si són igual o majors que 0.5 aleshores s'arrodoneix cap amunt.

## Input

Una nota amb o sense decimals

## Tests

### Test 16.67
```input
5.1
```
```output
5
```

### Test 16.67
```input
7.49
```
```output
7
```

### Test private 16.67
```input
10
```
```output
10
```

### Test private 16.67
```input
4.5
```
```output
5
```

### Test private 16.67
```input
7.75
```
```output
8
```

### Test private 16.65
```input
6
```
```output
6
```
