---
slug: un-cavall-contra-2-peons
difficulty: 2.0
tags: [operators, booleans, math]
---
# Un cavall contra dos peons

Als escacs el cavall pot saltar fent una "L", així:

![image](assets/un-cavall-contra-2-peons-img0.png)

Donada la posició d'un cavall i de dos peons al tauler, digues quants peons està amenaçant el cavall.

## Input

La posició del cavall, i del dos peons

## Output

`0` | `1` | `2`

## Tests

### Test
```input
4 5
3 3
5 4
```
```output
1
```
#### Explanation
![image](assets/un-cavall-contra-2-peons-img1.png)

### Test
```input
4 5
2 4
6 4
```
```output
2
```
#### Explanation
![image](assets/un-cavall-contra-2-peons-img2.png)

### Test
```input
6 2
6 4
7 1
```
```output
0
```
#### Explanation
![image](assets/un-cavall-contra-2-peons-img3.png)

### Test
```input
1 1
2 3
3 2
```
```output
2
```
#### Explanation
![image](assets/un-cavall-contra-2-peons-img4.png)

### Test
```input
7 6
3 4
8 8
```
```output
1
```
#### Explanation
![image](assets/un-cavall-contra-2-peons-img5.png)

### Test
```input
3 5
2 2
1 1
```
```output
0
```

### Test private
```input
8 2
7 4
5 3
```
```output
1
```
