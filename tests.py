import os
import fileinput


for dir in os.listdir('exercises'):
    pngnum = 0
    for f in os.listdir(os.path.join('exercises', dir)):
        if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.webp') or f.endswith('.gif'):
            newname = f'{dir}-img{pngnum}.{f.split(".")[-1]}'
            os.rename(os.path.join('exercises', dir, f), os.path.join('exercises', dir, newname))
            pngnum += 1
            with fileinput.input(os.path.join('exercises', dir, 'exercise.md'), inplace=True) as mdfile:
                for line in mdfile:
                    if f in line:
                        line = line.replace(f, newname)
                        print(line, end='')
                    else:
                        print(line, end='')