import re

string = input('Wprowadź ciąg: ')

regex = re.compile('\d{2}-\d{3}')

indexy = regex.findall(string)

if not indexy:
    print('Nie ma żadnego indeksu!')
else: 
    try:
        file = open('indexy.txt', 'a')
        file.write('\n'.join(indexy))
        print('Są nagranę indexy: ' + ' '.join(indexy))
    except FileNotFoundError:
        print('Nie ma pliku dla zapisywania!')
