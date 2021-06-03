def HowMore(f1, f2):
    if len(f1) >= len(f2):
        return len(f1)
    else:
        return len(f2)
try:
    file1 = open('tekst1.txt','r')
    file2 = open('tekst2.txt','r')
except FileNotFoundError:
    print('Nie udało otworzyć pliki')
fread1 = file1.readlines()
fread2 = file2.readlines()
for x in range(0, HowMore(fread1, fread2)):
    try:
        print('plik1: ' + fread1[x].strip('\n'))
    except IndexError:
        print('plik 1 już pusty')
    try:
        print('plik2: ' + fread2[x].strip('\n'))
    except IndexError:
        print('plik2 już pusty')
file1.close()
file2.close()
