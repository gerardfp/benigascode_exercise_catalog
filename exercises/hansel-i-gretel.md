---
slug: hansel-i-gretel
difficulty: 5.0
tags: [matrices, 2d-arrays, loops, nested-loops]
---
# Hansel i Gretel

Hänsel i Gretel són dos germans d'una família de llenyataires molt pobra. La madrastra convenç el seu pare d'abandonar-los al bosc per no haver de repartir amb ells el menjar familiar però ells poden tornar a casa seguint un rastre de pedretes que havien deixat al camí. Els nens repeteixen l'operació i aquest cop el rastre està fet d'engrunes de pa, que es mengen els ocells i per tant els nens es perden...

Ajuda a Hansel i Gretel a fer el camí de tornada a casa!

## Input

La entrada consisteix en un mapa del bosc on es marca la casa, les engrunes de pa i el lloc on s'han perdut Hansel i Gretel.

La casa està marcada amb la lletra 'A', les engrunes amb un punt '.', i Hansel i Gretel amb una 'H'.

El mapa està envoltat d'un marc amb coixinets '#'.

## Output

S'imprimirà el mapa del bosc a cada passa que hagin donat Hansel i Gretel recuperant les engrunes de pa.

## Solutions

```java
void printGrid(char[][] grid) {
    for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid[i].length; j++) {
            IO.print(grid[i][j]);
        }
        IO.println();
    }
}

void main() {
    Scanner sc = new Scanner(System.in);
    if (!sc.hasNextLine()) return;
    String firstLine = sc.nextLine().trim();
    if (firstLine.isEmpty()) return;
    int R = Integer.parseInt(firstLine);

    char[][] grid = new char[R][];
    for (int i = 0; i < R; i++) {
        grid[i] = sc.nextLine().toCharArray();
    }

    int hr = -1, hc = -1;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < grid[r].length; c++) {
            if (grid[r][c] == 'H') {
                hr = r;
                hc = c;
                break;
            }
        }
        if (hr != -1) break;
    }

    printGrid(grid);

    int[] dr = {-1, 1, 0, 0};
    int[] dc = {0, 0, -1, 1};

    while (true) {
        int nextR = -1, nextC = -1;
        for (int d = 0; d < 4; d++) {
            int nr = hr + dr[d];
            int nc = hc + dc[d];
            if (nr >= 0 && nr < R && nc >= 0 && nc < grid[nr].length) {
                if (grid[nr][nc] == '.') {
                    nextR = nr;
                    nextC = nc;
                    break;
                }
            }
        }
        if (nextR == -1) {
            break;
        }
        grid[hr][hc] = ' ';
        grid[nextR][nextC] = 'H';
        hr = nextR;
        hc = nextC;
        printGrid(grid);
    }
}
```

## Tests

### Test
```input
7
#########
#       #
# A..   #
#   .   #
#   ..H #
#       #
#########
```
```output
#########
#       #
# A..   #
#   .   #
#   ..H #
#       #
#########
#########
#       #
# A..   #
#   .   #
#   .H  #
#       #
#########
#########
#       #
# A..   #
#   .   #
#   H   #
#       #
#########
#########
#       #
# A..   #
#   H   #
#       #
#       #
#########
#########
#       #
# A.H   #
#       #
#       #
#       #
#########
#########
#       #
# AH    #
#       #
#       #
#       #
#########
```

### Test
```input
7
#########
#       #
# A..   #
#   .   #
#   ..H #
#       #
#########
```
```output
#########
#       #
# A..   #
#   .   #
#   ..H #
#       #
#########
#########
#       #
# A..   #
#   .   #
#   .H  #
#       #
#########
#########
#       #
# A..   #
#   .   #
#   H   #
#       #
#########
#########
#       #
# A..   #
#   H   #
#       #
#       #
#########
#########
#       #
# A.H   #
#       #
#       #
#       #
#########
#########
#       #
# AH    #
#       #
#       #
#       #
#########
```

### Test
```input
5
######
#A.. #
#  . #
#H.. #
######
```
```output
######
#A.. #
#  . #
#H.. #
######
######
#A.. #
#  . #
# H. #
######
######
#A.. #
#  . #
#  H #
######
######
#A.. #
#  H #
#    #
######
######
#A.H #
#    #
#    #
######
######
#AH  #
#    #
#    #
######
```

### Test
```input
7
#########
# A     #
# ...   #
#   .   #
#   ... #
#     H #
#########
```
```output
#########
# A     #
# ...   #
#   .   #
#   ... #
#     H #
#########
#########
# A     #
# ...   #
#   .   #
#   ..H #
#       #
#########
#########
# A     #
# ...   #
#   .   #
#   .H  #
#       #
#########
#########
# A     #
# ...   #
#   .   #
#   H   #
#       #
#########
#########
# A     #
# ...   #
#   H   #
#       #
#       #
#########
#########
# A     #
# ..H   #
#       #
#       #
#       #
#########
#########
# A     #
# .H    #
#       #
#       #
#       #
#########
#########
# A     #
# H     #
#       #
#       #
#       #
#########
```

### Test private
```input
8
##########
#  ....H #
#  .     #
#  ......#
#A      .#
#.      .#
#........#
##########
```
```output
##########
#  ....H #
#  .     #
#  ......#
#A      .#
#.      .#
#........#
##########
##########
#  ...H  #
#  .     #
#  ......#
#A      .#
#.      .#
#........#
##########
##########
#  ..H   #
#  .     #
#  ......#
#A      .#
#.      .#
#........#
##########
##########
#  .H    #
#  .     #
#  ......#
#A      .#
#.      .#
#........#
##########
##########
#  H     #
#  .     #
#  ......#
#A      .#
#.      .#
#........#
##########
##########
#        #
#  H     #
#  ......#
#A      .#
#.      .#
#........#
##########
##########
#        #
#        #
#  H.....#
#A      .#
#.      .#
#........#
##########
##########
#        #
#        #
#   H....#
#A      .#
#.      .#
#........#
##########
##########
#        #
#        #
#    H...#
#A      .#
#.      .#
#........#
##########
##########
#        #
#        #
#     H..#
#A      .#
#.      .#
#........#
##########
##########
#        #
#        #
#      H.#
#A      .#
#.      .#
#........#
##########
##########
#        #
#        #
#       H#
#A      .#
#.      .#
#........#
##########
##########
#        #
#        #
#        #
#A      H#
#.      .#
#........#
##########
##########
#        #
#        #
#        #
#A       #
#.      H#
#........#
##########
##########
#        #
#        #
#        #
#A       #
#.       #
#.......H#
##########
##########
#        #
#        #
#        #
#A       #
#.       #
#......H #
##########
##########
#        #
#        #
#        #
#A       #
#.       #
#.....H  #
##########
##########
#        #
#        #
#        #
#A       #
#.       #
#....H   #
##########
##########
#        #
#        #
#        #
#A       #
#.       #
#...H    #
##########
##########
#        #
#        #
#        #
#A       #
#.       #
#..H     #
##########
##########
#        #
#        #
#        #
#A       #
#.       #
#.H      #
##########
##########
#        #
#        #
#        #
#A       #
#.       #
#H       #
##########
##########
#        #
#        #
#        #
#A       #
#H       #
#        #
##########
```
