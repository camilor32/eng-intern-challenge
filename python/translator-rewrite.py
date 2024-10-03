import sys

alphas_braille_to_english = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' '
}
alphas_english_to_braille = {j:i for i,j in alphas_braille_to_english.items()}
numbers_braille_to_english = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
}
numbers_english_to_braille = {j:i for i,j in numbers_braille_to_english.items()}
modifiers = [
    '.....O', #capital follows
    '.O...O', #decimal follows
    '.O.OOO'  #number follows
]

def solution(input) -> str:
    if is_braille(input):
        return translate_braille_to_english(input)
    else:
        return translate_english_to_braille(input)

def is_braille(input) -> bool:
    for c in input:
        if c != 'O' and c != '.':
            return False
    return True

def translate_braille_to_english(input) -> str:
    cells = []
    output = ''
    capital = False
    number = False
    
    for x in range(0,len(input),6):
        word = ''
        for y in range(6):
            word += input[x+y]
        cells.append(word)

    for cell in cells:
        if capital:
            output += alphas_braille_to_english[cell].upper()
            capital = False
        elif number:
            output += numbers_braille_to_english[cell]
        
        elif cell == '.....O': #capital follows
            capital = True

        elif cell == '.O...O': #decimal follows
            output += '.'
            number = True

        elif cell == '.O.OOO': #number follows
            number = True

        elif cell == '......':
            output += ' '
            number = False
        
        else:
            output += alphas_braille_to_english[cell]

    return output

def translate_english_to_braille(input) -> str:
    output = ''
    number = False
    for char in input:
        if char == ' ':
            number = False
            output += '......'

        elif number == True:
            output += numbers_english_to_braille[char]

        elif char in numbers_english_to_braille.keys():
            output += '.O.OOO' #number follows
            output += numbers_english_to_braille[char]
            number = True

        elif char.isupper():
            output += '.....O' #capital follows
            output += alphas_english_to_braille[char.lower()]

        else:
            output += alphas_english_to_braille[char]
            

    return output

if __name__ == '__main__':
    var = ''
    for x in range(1, len(sys.argv)):
        var += sys.argv[x]
        
    print(solution(var))

