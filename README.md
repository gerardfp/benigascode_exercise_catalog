# benigascode_exercise_catalog
---

Created build_english_catalog.py
Created build_english_catalog.py
Ran command: Test English catalog coverage and stats (`python3 /home/gerard/.gemini/antigravity/brain/46dd8432-1ed3-49b9-a5d9-f4422b6a9e1e/scratch/build_english_catalog.py`)
Ran command: Check consistency of matrix and 2d-arrays tags (`python3 -c "
from build_english_catalog import CATALOG_EN

# Check matrix exercises
matrix_exs = [fn for fn, (d, tags) in CATALOG_EN.items() if 'matrices' in tags]
print('Matrix exercises count:', len(matrix_exs))
# Check if any have 2d-arrays
print('2d-arrays count:', sum(1 for fn, (d, tags) in CATALOG_EN.items() if '2d-arrays' in tags))
"`)
Ran command: Check consistency of matrix and 2d-arrays tags with PYTHONPATH (`PYTHONPATH=/home/gerard/.gemini/antigravity/brain/46dd8432-1ed3-49b9-a5d9-f4422b6a9e1e/scratch python3 -c "
from build_english_catalog import CATALOG_EN

matrix_exs = [fn for fn, (d, tags) in CATALOG_EN.items() if 'matrices' in tags]
print('Matrix exercises count:', len(matrix_exs))
print('2d-arrays count:', sum(1 for fn, (d, tags) in CATALOG_EN.items() if '2d-arrays' in tags))
"`)
Created apply_english_tags.py
Ran command: Run apply_english_tags.py to update files (`PYTHONPATH=/home/gerard/.gemini/antigravity/brain/46dd8432-1ed3-49b9-a5d9-f4422b6a9e1e/scratch python3 /home/gerard/.gemini/antigravity/brain/46dd8432-1ed3-49b9-a5d9-f4422b6a9e1e/scratch/apply_english_tags.py`)
Ran command: View git diff of sample exercises (`git diff exercises/acronimo.md exercises/altura-minima.md exercises/analisis-estadistico-de-temperaturas.md exercises/aprovar-el-modul.md exercises/amaga-les-columnes.md`)
Ran command: View diffs for various categories (`git diff exercises/ascii-world.md exercises/definir-la-classe-comptecorrent.md exercises/evaluate-expression.md exercises/inode-flags.md exercises/bomberman.md`)
Ran command: Validate all unique tags are English (`python3 -c "
import glob, yaml, os

files = sorted(glob.glob('exercises/*.md'))
non_class = [f for f in files if not os.path.basename(f).startswith('class-')]
class_files = [f for f in files if os.path.basename(f).startswith('class-')]

print(f'Total markdown: {len(files)}, non-class: {len(non_class)}, class: {len(class_files)}')

all_tags = set()
for f in non_class:
    with open(f) as fp:
        c = fp.read()
    parts = c.split('---', 2)
    fm = yaml.safe_load(parts[1])
    tags = fm.get('tags', [])
    for t in tags:
        all_tags.add(t)

print('\nAll unique tags in non-class exercises (' + str(len(all_tags)) + '):')
print(sorted(all_tags))
"`)
Ran command: Verify class-* files untouched in git status (`git status --short | grep "class-"`)
Ran command: Check modified file count in git status (`git status --short | wc -l`)
Ran command: Inspect top and bottom of git status (`git status -s | head -n 5 && git status -s | tail -n 5`)

Se han actualizado **todos los ejercicios del catálogo** (277 ejercicios, excluyendo estrictamente los 27 archivos que comienzan por `class-*`) con una **taxonomía de etiquetas en inglés**, rica y descriptiva, orientada específicamente a que el alumnado pueda localizar con precisión qué necesita practicar en cada momento.

---

### 1. Organización del Sistema de Etiquetas (en inglés)

Las etiquetas cubren diferentes niveles de búsqueda complementarios:

#### A. Construcciones del Lenguaje y Sintaxis
* `literals`, `variables`, `types`
* `operators`, `arithmetic`, `modulo`, `booleans`, `logical-operators`, `relational-operators`, `bitwise`
* `casting`, `char`, `char-arithmetic`
* `ternary`
* `scanner`, `io`
* `classes`, `oop` *(para los ejercicios que definen clases y no tienen prefijo `class-`)*

#### B. Control de Flujo (Estructuras de Decisión y Repetición)
* `conditionals`, `if-else`, `switch`
* `loops`, `for-loop`, `while-loop`, `nested-loops`, `sentinel-loop` *(bucles con lectura hasta valor centinela como 0, -1 o EOF)*
* `recursion`

#### C. Estructuras de Datos
* `arrays` *(arrays unidimensionales)*
* `matrices`, `2d-arrays` *(arrays bidimensionales / matrices / rejillas)*
* `strings`

#### D. Biblioteca Estándar y Manipulación
* `string-manipulation`, `formatting` *(uso de `.formatted()`, alineaciones)*, `parsing`
* `math`, `geometry` *(cálculos de distancias, radios, coordenadas)*
* `random`

#### E. Esquemas Algorítmicos y Patrones
* `counters` *(conteo de elementos que cumplen un predicado)*
* `accumulators` *(sumas acumuladas, cálculo de medias, productos)*
* `min-max` *(cálculo de extremos)*
* `flags` *(comprobaciones booleanas de tipo "hay alguno" o "todos cumplen")*
* `search` *(búsqueda lineal, dicotómica, localización de índices)*
* `sorting`, `bubble-sort`, `merge`
* `two-pointers`, `reverse`, `array-rotation`, `partitioning`, `filtering`
* `greedy`, `simulation`, `state-machine`, `backtracking`

#### F. Contextos y Dominios Prácticos
* `game`, `board-game`, `chess`, `cards`
* `ascii-art`, `patterns` *(dibujo de figuras con bucles anidados)*
* `date-time`, `time`
* `cryptography`
* `database` *(simulaciones de JOIN / SELECT)*
* `prime-numbers`, `fibonacci`

---

### 2. Ejemplos de Búsqueda para los Alumnos

Gracias al etiquetado multifacético, cualquier estudiante puede filtrar según su necesidad de práctica:

| Necesidad del alumno | Etiquetas que puede combinar | Ejemplos de ejercicios encontrados |
| :--- | :--- | :--- |
| *Practicar bucles anidados con matrices o tableros* | `matrices`, `2d-arrays`, `nested-loops` | [bomberman.md](file:///home/gerard/benigascode_exercise_catalog/exercises/bomberman.md), [ceros-debajo-de-la-diagonal.md](file:///home/gerard/benigascode_exercise_catalog/exercises/ceros-debajo-de-la-diagonal.md), [amaga-les-columnes.md](file:///home/gerard/benigascode_exercise_catalog/exercises/amaga-les-columnes.md), [cubetris.md](file:///home/gerard/benigascode_exercise_catalog/exercises/cubetris.md) |
| *Practicar bucles `while` que leen hasta valor centinela* | `while-loop`, `sentinel-loop` | [analisis-estadistico-de-temperaturas.md](file:///home/gerard/benigascode_exercise_catalog/exercises/analisis-estadistico-de-temperaturas.md), [combinacion-secreta-de-la-caja-fuerte.md](file:///home/gerard/benigascode_exercise_catalog/exercises/combinacion-secreta-de-la-caja-fuerte.md), [cuenta-numeros.md](file:///home/gerard/benigascode_exercise_catalog/exercises/cuenta-numeros.md), [picos-maximos.md](file:///home/gerard/benigascode_exercise_catalog/exercises/picos-maximos.md) |
| *Practicar el operador módulo `%` y números primos* | `modulo`, `prime-numbers` | [el-primo-del-pueblo.md](file:///home/gerard/benigascode_exercise_catalog/exercises/el-primo-del-pueblo.md), [los-primos-del-pueblo.md](file:///home/gerard/benigascode_exercise_catalog/exercises/los-primos-del-pueblo.md), [numero-primo.md](file:///home/gerard/benigascode_exercise_catalog/exercises/numero-primo.md) |
| *Practicar filtrado y recorrido de arrays* | `arrays`, `filtering` | [altura-minima.md](file:///home/gerard/benigascode_exercise_catalog/exercises/altura-minima.md), [separar-los-grandes-de-los-pequenos.md](file:///home/gerard/benigascode_exercise_catalog/exercises/separar-los-grandes-de-los-pequenos.md), [passar-llista.md](file:///home/gerard/benigascode_exercise_catalog/exercises/passar-llista.md) |
| *Practicar formateo o extracción en cadenas* | `strings`, `string-manipulation`, `formatting` | [acronimo.md](file:///home/gerard/benigascode_exercise_catalog/exercises/acronimo.md), [auto-indent-lines.md](file:///home/gerard/benigascode_exercise_catalog/exercises/auto-indent-lines.md), [case-styles.md](file:///home/gerard/benigascode_exercise_catalog/exercises/case-styles.md), [word-highlight.md](file:///home/gerard/benigascode_exercise_catalog/exercises/word-highlight.md) |
| *Practicar recursividad* | `recursion` | [evaluate-expression.md](file:///home/gerard/benigascode_exercise_catalog/exercises/evaluate-expression.md), [factorial.md](file:///home/gerard/benigascode_exercise_catalog/exercises/factorial.md), [hanoi.md](file:///home/gerard/benigascode_exercise_catalog/exercises/hanoi.md), [maze.md](file:///home/gerard/benigascode_exercise_catalog/exercises/maze.md), [palindrom.md](file:///home/gerard/benigascode_exercise_catalog/exercises/palindrom.md) |

---

### 3. Distribución Cuantitativa

* **Ejercicios evaluados y actualizados:** 277
* **Ejercicios `class-*` omitidos (intactos):** 27
* **Etiquetas únicas en inglés:** 84
* **Distribución de dificultad (1 a 9):**
  * **Dificultad 1:** 37 ejercicios *(conceptos básicos U1, literales, variables, fórmulas directas sin saltos)*
  * **Dificultad 2:** 71 ejercicios *(condicionales simples `if-else`/`switch`, casting, bucles básicos)*
  * **Dificultad 3:** 104 ejercicios *(bucles simples, esquemas de conteo y acumulación, arrays 1D, cadenas estándar)*
  * **Dificultad 4:** 40 ejercicios *(bucles anidados, matrices 2D, ordenación, ventanas deslizantes)*
  * **Dificultad 5:** 17 ejercicios *(simulaciones complejas, algoritmos sobre tableros o matrices multietapa)*
  * **Dificultad 6:** 7 ejercicios *(simuladores de bases de datos/JOIN, analizador de logs, resolución de laberintos)*
  * **Dificultad 9:** 1 ejercicio *(geometría computacional e intersección de círculos: [cercles-rgb.md](file:///home/gerard/benigascode_exercise_catalog/exercises/cercles-rgb.md))*