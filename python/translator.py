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
    'O..OOO': 'z'
}
other_braille_to_english = {
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '|',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' '
}
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
alphas_english_to_braille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO'
}
other_english_to_braille = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '|': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}
numbers_english_to_braille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}
ascii_to_english = {
    32: ' ',
    33: '!',
    40: '(',
    41: ')',
    44: ',',
    45: '-',
    46: '.',
    47: '/',
    58: ':',
    59: ';',
    60: '<',
    62: '>',
    63: '?',
    48: '0', #numbers start
    49: '1',
    50: '2',
    51: '3',
    52: '4',
    53: '5',
    54: '6',
    55: '7',
    56: '8',
    57: '9',
    65: 'A', #uppercase starts
    66: 'B',
    67: 'C',
    68: 'D',
    69: 'E',
    70: 'F',
    71: 'G',
    72: 'H',
    73: 'I',
    74: 'J',
    75: 'K',
    76: 'L',
    77: 'M',
    78: 'N',
    79: 'O',
    80: 'P',
    81: 'Q',
    82: 'R',
    83: 'S',
    84: 'T',
    85: 'U',
    86: 'V',
    87: 'W',
    88: 'X',
    89: 'Y',
    90: 'Z',
    97: 'a', #lowercase starts
    98: 'b',
    99: 'c',
    100: 'd',
    101: 'e',
    102: 'f',
    103: 'g',
    104: 'h',
    105: 'i',
    106: 'j',
    107: 'k',
    108: 'l',
    109: 'm',
    110: 'n',
    111: 'o',
    112: 'p',
    113: 'q',
    114: 'r',
    115: 's',
    116: 't',
    117: 'u',
    118: 'v',
    119: 'w',
    120: 'x',
    121: 'y',
    122: 'z'
}

def my_solution(input_text):
    return_text = ''
    if is_braille(input_text):
        cell_index_group = ['', 0]
        input_len = len(input_text)

        def read_next_cell():
            cell_index_group[0] = ''
            for i in range(6):
                cell_index_group[0] += input_text[cell_index_group[1]]
                cell_index_group[1] += 1

        while(input_len-cell_index_group[1]-6 > 0):#if input braille string is not multiple of 6, final characters will be omited
            read_next_cell()
            if is_valid_cell(cell_index_group[0]): #check if it is a valid braille word/cell
                #check if cell is a modifier
                if cell_index_group[0] == '....o': #capital follows (only next character)
                    #capitalize next cell before appending it to return_text
                    read_next_cell()
                    if cell_index_group[0] in alphas_braille_to_english.keys(): 
                        return_text += alphas_braille_to_english[cell_index_group[0]].upper()
                    else: 
                        return_text += '(invalid: "capital follows" not followed by alpha)'

                elif cell_index_group[0] == '.o...o': #decimal follows
                    #append decimal to return_text before appending the next cell
                    read_next_cell()
                    if cell_index_group[0] in numbers_braille_to_english.keys(): 
                        return_text += '.' + numbers_braille_to_english[cell_index_group[0]]
                    else: 
                        return_text += '(invalid: "decimal follows" not followed by number)'
                    
                elif cell_index_group[0] == '.o.ooo': #number follows (until next space)
                    #read next cell as number and append to return_text
                    read_next_cell()
                    if cell_index_group[0] in numbers_braille_to_english.keys(): 
                        return_text += numbers_braille_to_english[cell_index_group[0]]
                    else: 
                        return_text += '(invalid: "number follows" not followed by number)'

                #else append the 'alpha' or 'other' character to return_text
                elif cell_index_group[0] in alphas_braille_to_english.keys(): 
                    return_text += alphas_braille_to_english[cell_index_group[0]]
                elif cell_index_group[0] in other_braille_to_english.keys(): 
                    return_text += other_braille_to_english[cell_index_group[0]]

            else:
                #if not valid word/cell, append 'invlaid' to return_text
                return_text += '(invalid)'

    else:
        #translate from english to braille
        for char in input_text: #check if character is part of required characters to translate
            if ord(char) in ascii_to_english.keys():
                #check if capital
                if ord(char) >= 65 and ord(char) <= 90:
                    print()
                #check if number
                #check if is a period/decimal, and if numbers come after until next space
                #else append character
                print()

            else: return_text += '(invalid character)'

    return return_text

def is_braille(text):
    for x in text:
        if x != 'O' and x != '.':
            return False
    return True

def is_valid_cell(cell) -> bool:
    if cell == 'O.....': return True #a
    if cell == 'O.O...': return True #b
    if cell == 'OO....': return True #c
    if cell == 'OO.O..': return True #d
    if cell == 'O..O..': return True #e
    if cell == 'OOO...': return True #f
    if cell == 'OOOO..': return True #g
    if cell == 'O.OO..': return True #h 
    if cell == '.OO...': return True #i
    if cell == '.OOO..': return True #j
    if cell == 'O...O.': return True #k
    if cell == 'O.O.O.': return True #l
    if cell == 'OO..O.': return True #m
    if cell == 'OO.OO.': return True #n 
    if cell == 'O..OO.': return True #o
    if cell == 'OOO.O.': return True #p
    if cell == 'OOOOO.': return True #q
    if cell == 'O.OOO.': return True #r
    if cell == '.OO.O.': return True #s
    if cell == '.OOOO.': return True #t
    if cell == 'O...OO': return True #u
    if cell == 'O.O.OO': return True #v
    if cell == '.OOO.O': return True #w
    if cell == 'OO..OO': return True #x
    if cell == 'OO.OOO': return True #y
    if cell == 'O..OOO': return True #z
    if cell == 'O.....': return True #1
    if cell == 'O.O...': return True #2
    if cell == 'OO....': return True #3
    if cell == 'OO.O..': return True #4
    if cell == 'O..O..': return True #5
    if cell == 'OOO...': return True #6
    if cell == 'OOOO..': return True #7
    if cell == 'O.OO..': return True #8
    if cell == '.OO...': return True #9
    if cell == '.OOO..': return True #0
    if cell == '.....O': return True #cellapital follows
    if cell == '.O...O': return True #decellimal follows
    if cell == '.O.OOO': return True #number follows
    if cell == '..OO.O': return True #.
    if cell == '..O...': return True #,
    if cell == '..O.OO': return True #?
    if cell == '..OOO.': return True #|
    if cell == '..OO..': return True #:
    if cell == '..O.O.': return True #;
    if cell == '....OO': return True #-
    if cell == '.O..O.': return True #/
    if cell == '.OO..O': return True #<
    if cell == 'O..OO.': return True #>
    if cell == 'O.O..O': return True #(
    if cell == '.O.OO.': return True #)
    if cell == '......': return True #space
    return False

if __name__ == "__main__":
    input = sys.argv[1]
    print(input)