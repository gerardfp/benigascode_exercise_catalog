import os
import fileinput
for root, dirs, files in os.walk('exercises'):
    for f in files:
        if f.endswith('.md'):
            with fileinput.input(os.path.join(root, f), inplace=True) as file:
                for line in file:
                    if line.startswith('### Test'):
                        print('### Test', end='\n')
                    else:
                        print(line, end='')

