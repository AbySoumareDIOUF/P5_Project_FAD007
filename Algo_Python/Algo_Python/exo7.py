la_phrase=input("entrer votre phrase : ")
code_aski = {
        'A': '2',
        'B': '22',
        'C': '222',
        'D': '3',
        'E': '33',
        'F': '333',
        'G': '4',
        'H':'44',
        'I': '444',
        'J':'5',
        'K': '55',
        'L': '555',
        'M': '6',
        'N': '66',
        'O': '666',
        'P': '7',
        'Q': '77',
        'R': '777',
        'S': '7777',
        'T': '8',
        'U': '88',
        'V': '888',
        'W': '9',
        'X': '99',
        'Y': '999',
        'Z': '9999',
        '0': 'A',
        '1': 'B',
        '2': 'C',
        '3': 'D',
        '4': 'E',
        '5': 'F',
        '6': 'G',
        '7': 'H',
        '8': 'I',
        '9': 'J',
        ' ': '00'
    }
tab_phrase=[]
phrase_corrige=[]
phrase_aski=''
for i in la_phrase:
    if i in code_aski:
        phrase_aski+=code_aski[i]
tab_phrase.append(phrase_aski)
print(tab_phrase)


for i in range (1,len(tab_phrase)):
    a=tab_phrase[i-1]
    b=tab_phrase[i]   
    if (a[len(a-1)]==b[0]):
        phrase_corrige.append('0')
    phrase_corrige.append(tab_phrase[i])
print(phrase_corrige)
for i in phrase_corrige:
    print(i)



